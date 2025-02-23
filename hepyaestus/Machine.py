from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.baseClasses import StoreObject
from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData
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

        self.totalWorkingTime: float = 0
        self.totalBlockageTime: float = 0
        self.timeLastOperationStarted: float = 0

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)

    def run(self) -> Generator:
        while True:
            while True:
                receivedEvents = yield self.env.any_of(
                    [self.isRequested, self.canDispose]
                )
                assert receivedEvents is not None
                assert self.receiver is not None
                assert self.giver is not None

                if self.isRequested in receivedEvents:
                    assert self.isRequested.value is not None

                    eventData = self.isRequested.value
                    assert isinstance(eventData, EventData)
                    assert isinstance(eventData.transmission, Entity)
                    # assert eventData.time == self.env.now
                    self.isRequested = self.env.event()
                    self.printTrace(isRequested=eventData)

                    self.receive(eventData.transmission)

                if self.canDispose in receivedEvents:
                    eventData = self.canDispose.value
                    assert isinstance(eventData, EventData)
                    # assert eventData.time == self.env.now
                    self.canDispose = self.env.event()
                    self.printTrace(canDispose=eventData)

                    entity = yield self.give()
                    assert isinstance(entity, Entity)

                    self.giveReceiverEntity(
                        EventData(
                            caller=self,
                            time=self.env.now,
                            transmission=entity,
                            attempt=eventData.attempt,
                        )
                    )
                break

            yield self.env.timeout(delay=self.processingTime.generateNumber())

            self.canReceiversReceive()
            self.canGiversGive()

    def give(self):
        self.totalWorkingTime += self.env.now - self.timeLastOperationStarted
        return super().give()

    def receive(self, entity: Entity) -> None:
        self.timeLastOperationStarted = self.env.now
        super().receive(entity)
