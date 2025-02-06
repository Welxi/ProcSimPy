from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.baseClasses import StoreObject
from hepyaestus.Entity import Entity
from hepyaestus.RandomNumberGenerator import RandomNumberGenerator

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Line import Line
    from hepyaestus.ProbDistribution import ProbDistribution
    from simpy import Environment


class Machine(StoreObject):
    def __init__(self, id: str, name: str, processingTime: ProbDistribution) -> None:
        super().__init__(id, name)
        self.processingTime: RandomNumberGenerator = RandomNumberGenerator(
            distribution=processingTime
        )

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)

    def run(self) -> Generator:
        while True:
            while True:
                receivedEvents = yield self.env.any_of(
                    [self.isRequested, self.canDispose]
                )
                assert receivedEvents is not None
                if self.isRequested in receivedEvents:
                    assert self.isRequested.value is not None
                    assert self.receiver is not None
                    assert self.giver is not None

                    transmitter, eventTime = self.isRequested.value
                    self.printTrace(isRequested=transmitter.id, eventTime=eventTime)
                    self.isRequested = self.env.event()

                    assert isinstance(transmitter, Entity)
                    self.receive(transmitter)
                    break

            yield self.env.timeout(delay=self.processingTime.generateNumber())

            if self.receiver.canReceive():
                entity = yield self.give()
                assert isinstance(entity, Entity)
                assert self.receiver is not None
                self.receiver.isRequested.succeed((entity, self.env.now))

            if self.giver.canGive():
                self.giver.canDispose.succeed((self, self.env.now))
