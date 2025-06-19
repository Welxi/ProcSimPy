from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Optional

from procsimpy.Base import Base

if TYPE_CHECKING:
    from procsimpy.Failure import Failure
    from procsimpy.Line import Line
    from procsimpy.Node import Node
    from procsimpy.ShiftChange import ShiftChange
    from simpy import Environment
    from simpy.core import SimTime


class EntityStatus(Enum):
    INIT = 'Init'
    ARRIVED = 'Arrived'
    PAUSED = 'Paused'
    PROCESSING = 'Processing'
    PROCESSED = 'Processed'
    TRANSIT = 'Transit'
    SCRAPPED = 'Scrapped'


class Entity(Base):
    type = 'Entity'  # used for ID creation in source
    """
    Generic for Component that is being processed / transferred between Nodes.

    It is created by a Source Node or by experiment setup with Work in Progress,
      in which case a Starting Station must be provided

    :param Base: _description_
    :type Base: _type_
    """

    def __init__(
        self,
        id: str,
        name: str,
        *,
        startingNode: Optional[Node] = None,
        remainingProcessingTime: Optional[SimTime] = None,
    ) -> None:
        super().__init__(id, name)
        self.startingNode: Optional[Node] = startingNode
        self.processTime: Optional[SimTime] = remainingProcessingTime
        self.status: EntityStatus = EntityStatus.INIT

    def initialize(self, env: Environment, line: Line, *, currentNode: Node) -> None:  # type: ignore
        """
        sets/resets Entity for new simulation

        :param env: SimPy Enviroment
        :type env: Environment
        :param line: Line Orchestration Module
        :type line: LineNode
        :param currentNode: Node the Entity begins at
        :type currentNode: Node
        """
        super().initialize(env, line)
        # self.printTrace(CreateEvent(time=self.env.now, caller=self))

        if self.startingNode is not None:
            assert currentNode == self.startingNode, 'Must begin at Starting Node'

        self.currentNode = currentNode

        self.creationTime: SimTime = self.env.now
        self.startTime: SimTime = self.env.now

    def updateStation(self, station: Node) -> None:
        """
        Must be called when Entity has entered new Node, updates current station

        :param station: New Station entered
        :type station: Node
        """
        # for work in progress can be called before initialised
        # time = self.env.now if hasattr(self, 'env') else 0
        # self.printTrace(EnterEvent(time=time, caller=self, station=station))
        self.currentNode = station
        self.status = EntityStatus.ARRIVED

        if self.processTime is None:
            self.processTime = self.currentNode.processingTime()

    def startProcessing(self) -> None:
        self.status = EntityStatus.PROCESSING
        self.currentNode.stats.startingProcessing()
        self.timeStarted = self.env.now

    def finishedProcessing(self) -> None:
        self.status = EntityStatus.PROCESSED
        self.processTime = None
        self.currentNode.stats.finishedProcessing()

        if not self.currentNode.pendingHandover.triggered:
            self.currentNode.pendingHandover.succeed()

    def pause(self, cause: Failure | ShiftChange) -> None:
        self.status = EntityStatus.PAUSED
        assert self.processTime is not None
        self.processTime -= self.env.now - self.timeStarted
        self.currentNode.stats.finishedProcessing()

    def transit(self) -> None:
        self.status = EntityStatus.TRANSIT

    def isProcessed(self) -> bool:
        return self.status == EntityStatus.PROCESSED

    def toBeProcessed(self) -> bool:
        return self.status in (EntityStatus.ARRIVED, EntityStatus.PAUSED)

    def processingTime(self) -> SimTime | None:
        return self.processTime
