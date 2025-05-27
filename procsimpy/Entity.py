from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from procsimpy.Base import BaseObject
from procsimpy.EventData import EventData
from procsimpy.RandomNumberGenerator import RandomNumberGenerator

if TYPE_CHECKING:
    from procsimpy.Line import Line
    from procsimpy.ProbDistribution import ProbDistribution
    from procsimpy.StoreNode import StoreNode
    from simpy import Environment


class Entity(BaseObject):
    type = 'Entity'

    def __init__(
        self,
        id: str,
        name: str,
        *,
        startingStation: Optional[StoreNode] = None,
        remainingProcessingTime: Optional[ProbDistribution] = None,
    ) -> None:
        super().__init__(id, name)
        self.startingStation: Optional[StoreNode] = startingStation
        self.remainingProcessingTime: Optional[RandomNumberGenerator] = (
            RandomNumberGenerator(distribution=remainingProcessingTime)
            if remainingProcessingTime is not None
            else None
        )

    def initialize(
        self,
        env: Environment,
        line: Line,
        currentStation: Optional[StoreNode] = None,
    ) -> None:
        # Need to check here because of Inheritance rules need same parameters
        assert currentStation is not None, 'currentStation needed for starting node'

        super().initialize(env, line)
        self.printTrace(create=None)
        self.creationTime: float = self.env.now
        self.startTime: float = self.env.now

        if self.startingStation is not None:
            assert currentStation == self.startingStation, (
                'currentStation must begin the same as startingStation'
            )

        self.currentStation: Optional[StoreNode] = currentStation
        self.stations: list[tuple[float, Optional[StoreNode]]] = [
            (self.env.now, currentStation)
        ]

    def updateStation(self, station: StoreNode) -> None:
        """
        Called by store node when accepting new entity

        :param station: the new StoreNode that has this entity
        :type station: StoreNode
        """
        self.printTrace(enter=EventData(caller=station, time=self.env.now))
        self.currentStation = station
        # ? will I need a list of stations visited for output tracing
