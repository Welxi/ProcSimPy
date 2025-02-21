from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from hepyaestus.baseClasses import BaseObject, CoreObject
from hepyaestus.EventData import EventData

if TYPE_CHECKING:
    from hepyaestus.Line import Line
    from simpy import Environment


class Entity(BaseObject):
    type = 'Entity'

    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)

    def initialize(
        self, env: Environment, line: Line, currentStation: Optional[CoreObject] = None
    ) -> None:
        super().initialize(env, line)
        self.printTrace(create=None)
        self.creationTime = self.env.now
        self.startTime = self.env.now
        self.stations: list[tuple[float, Optional[CoreObject]]] = [
            (self.env.now, currentStation)
        ]
        self.currentStation: Optional[CoreObject] = currentStation

    def updateStation(self, station: CoreObject) -> None:
        self.printTrace(enter=EventData(caller=station, time=self.env.now))
        self.currentStation = station
        # ? will I need a list of stations visited for output tracing
