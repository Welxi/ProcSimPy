from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData
from hepyaestus.Store import StoreNode

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Line import Line
    from simpy import Environment


class Exit(StoreNode):
    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)
        self.exits: list[Entity] = []

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.numOfExits: int = 0
        self.timeLastEntityLeft: float = 0

    def run(self) -> Generator:
        while True:
            yield self.isRequested
            assert self.isRequested.value is not None

            eventData = self.isRequested.value
            self.isRequested = self.env.event()
            assert isinstance(eventData, EventData)
            assert isinstance(eventData.transmission, Entity)
            assert eventData.time == self.env.now
            self.printTrace(isRequested=eventData)

            self._receive(eventData.transmission)

            self.canGiversGive()

    def _receive(self, entity: Entity) -> None:
        self.exits.append(entity)
        self.numOfExits += 1
        self.timeLastEntityLeft = self.env.now
        super()._receive(entity)
