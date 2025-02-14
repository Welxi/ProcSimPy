from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.baseClasses import StoreObject
from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Line import Line
    from simpy import Environment


class Queue(StoreObject):
    def __init__(self, id: str, name: str, capacity: int = 1) -> None:
        super().__init__(id, name, capacity)
        self.times = 0

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)

    def run(self) -> Generator:
        while True:
            receivedEvents = yield self.env.any_of([self.isRequested, self.canDispose])
            assert receivedEvents is not None
            assert self.receiver is not None
            if self.isRequested in receivedEvents:
                assert self.isRequested.value is not None

                transmitter, eventTime = self.isRequested.value
                self.printTrace(isRequested=transmitter.id, eventTime=eventTime)
                self.isRequested = self.env.event()

                assert isinstance(transmitter, Entity)
                self.receive(transmitter)
                # self.canDispose.succeed((self, self.env.now))
                if self.receiver.canReceive():
                    entity = yield self.give()
                    assert isinstance(entity, Entity)
                    assert self.receiver is not None
                    self.receiver.isRequested.succeed((entity, self.env.now))

            if self.canDispose in receivedEvents and self.receiver.canReceive():
                assert self.canDispose.value is not None

                transmitter, eventTime = self.canDispose.value
                self.printTrace(canDispose=transmitter.id, eventTime=eventTime)
                self.canDispose = self.env.event()

                if self.receiver.canReceive():
                    entity = yield self.give()
                    assert isinstance(entity, Entity)
                    assert self.receiver is not None
                    self.receiver.isRequested.succeed((entity, self.env.now))
