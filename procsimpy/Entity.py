from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from procsimpy.Base import Base
from procsimpy.EventData import CreateEvent, EnterEvent
from procsimpy.RandomNumberGenerator import RandomNumberGenerator

if TYPE_CHECKING:
    from procsimpy.Line import Line
    from procsimpy.Node import Node
    from procsimpy.ProbDistribution import ProbDistribution
    from simpy import Environment
    from simpy.core import SimTime


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
        remainingProcessingTime: Optional[ProbDistribution] = None,
    ) -> None:
        super().__init__(id, name)
        self.startingNode: Optional[Node] = startingNode
        self.remainingProcessingTime: Optional[RandomNumberGenerator] = (
            RandomNumberGenerator(distribution=remainingProcessingTime)
            if remainingProcessingTime is not None
            else None
        )

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
        self.printTrace(CreateEvent(time=self.env.now, caller=self))

        if self.startingNode is not None:
            assert currentNode == self.startingNode, 'Must begin at Starting Node'
            # can this ever fail? only if user changes libary

        self.currentNode = currentNode

        self.creationTime: SimTime = self.env.now
        self.startTime: SimTime = self.env.now

        # TODO keep list of stations visited

    def updateStation(self, station: Node) -> None:
        """
        Must be called when Entity has entered new Node, updates current station

        :param station: New Station entered
        :type station: Node
        """
        self.printTrace(EnterEvent(time=self.env.now, caller=self, station=station))
        self.currentNode = station
        # TODO add log of stations entered with times
