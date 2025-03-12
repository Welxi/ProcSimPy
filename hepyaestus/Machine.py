from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData
from hepyaestus.RandomNumberGenerator import RandomNumberGenerator
from hepyaestus.Store import StoreNode

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Line import Line
    from hepyaestus.ProbDistribution import ProbDistribution
    from simpy import Environment


class Machine(StoreNode):
    def __init__(
        self,
        id: str,
        name: str,
        processingTime: ProbDistribution,
        capacity: int = 1,
        priority: int = 0,
    ) -> None:
        super().__init__(id, name, capacity=capacity, priority=priority)
        self.processingTime: RandomNumberGenerator = RandomNumberGenerator(
            distribution=processingTime
        )

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)

    def run(self) -> Generator:
        while True:
            while True:
                receivedEvents = yield self.env.any_of(
                    [self.isRequested, self.canDispose, self.initialWIP]
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

                    self._receive(eventData.transmission)

                if self.canDispose in receivedEvents:
                    eventData = self.canDispose.value
                    assert isinstance(eventData, EventData)
                    # assert eventData.time == self.env.now
                    self.canDispose = self.env.event()
                    self.printTrace(canDispose=eventData)

                    entity = yield self._give()
                    assert isinstance(entity, Entity)

                    self.giveReceiverEntity(
                        EventData(
                            caller=self,
                            time=self.env.now,
                            transmission=entity,
                            attempt=eventData.attempt,
                        )
                    )
                if self.initialWIP in receivedEvents:
                    eventData = self.initialWIP.value
                    assert isinstance(eventData, EventData)
                    assert self.notEmpty(), (
                        'Line needs to populate store before calling WIP'
                    )

                    # should only ever be called once by Line
                    self.initialWIP = self.env.event()
                    # needs to be reset to remove it from receivedEvents

                    self.printTrace(initialWIP=eventData)

                break

            self.stats.startingProcessing()
            yield self.env.timeout(delay=self.calculateProcessingTime())
            self.stats.finishedProcessing()

            self.canReceiversReceive()
            self.canGiversGive()

    def calculateProcessingTime(self) -> float:
        # TODO check greater than zero
        activeEntity: Entity | None = self._getActiveEntity()
        if (
            activeEntity is not None
            and activeEntity.remainingProcessingTime is not None
        ):
            return activeEntity.remainingProcessingTime.generateNumber()
        return self.processingTime.generateNumber()
