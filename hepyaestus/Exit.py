from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.baseClasses import StoreObject
from hepyaestus.Entity import Entity

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Line import Line
    from simpy import Environment


class Exit(StoreObject):
    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)
        self.exits: list[Entity] = []

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.numOfExits: int = 0

    def run(self) -> Generator:
        while True:
            yield self.isRequested
            assert self.isRequested.value is not None
            transmitter, eventTime = self.isRequested.value
            self.printTrace(isRequested=transmitter.id, eventTime=eventTime)
            self.isRequested = self.env.event()

            assert isinstance(transmitter, Entity)
            self.receive(transmitter)
            self.exits.append(transmitter)
            self.numOfExits += 1
