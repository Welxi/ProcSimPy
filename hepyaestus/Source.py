from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from hepyaestus.baseClasses import StoreObject
from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData
from hepyaestus.RandomNumberGenerator import RandomNumberGenerator

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Line import Line
    from hepyaestus.ProbDistribution import ProbDistribution
    from simpy import Environment


class EntityGenerator:
    def __init__(self, victim: Source, env: Environment, line: Line) -> None:
        self.env: Environment = env
        self.line: Line = line
        self.type = 'EntityGenerator'
        self.victim: Source = victim

    def run(self) -> Generator:
        while True:
            entity: Entity = self.victim.createEntity()
            entity.initialize(self.env, self.line, currentStation=self.victim)

            if self.victim.canReceive() and not self.victim.entityCreated.triggered:
                self.victim.entityCreated.succeed(
                    EventData(
                        caller=self.victim, time=self.env.now, transmission=entity
                    )
                    # Adding caller as self.victim because caller needs to be a CoreObject
                )

            yield self.env.timeout(self.victim.calculateInterArrivalTime())


class Source(StoreObject):
    def __init__(
        self,
        id: str,
        name: str,
        interArrivalTime: ProbDistribution,
        entity: Optional[type[Entity]] = None,
    ) -> None:
        super().__init__(id, name)
        self.partNumber: int = 0
        self.item = entity if entity else Entity

        self.type = 'Source'
        self.rng = RandomNumberGenerator(interArrivalTime)
        self.times = 0

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.entityCreated = self.env.event()

        self.entityGenerator = EntityGenerator(
            victim=self, env=self.env, line=self.line
        )
        self.env.process(self.entityGenerator.run())

    def run(self) -> Generator:
        while True:
            receivedEvents = yield self.env.any_of([self.entityCreated])
            assert receivedEvents is not None
            if self.entityCreated in receivedEvents:
                assert self.entityCreated.value is not None

                eventData = self.entityCreated.value
                assert isinstance(eventData, EventData)
                assert isinstance(eventData.transmission, Entity)
                assert eventData.time == self.env.now
                self.printTrace(enter=eventData)
                self.entityCreated = self.env.event()

                self.receive(eventData.transmission)

                assert self.receiver is not None
                if self.receiver.canReceive():
                    entity = yield self.give()
                    assert isinstance(entity, Entity)
                    assert self.receiver is not None
                    self.receiver.isRequested.succeed(
                        EventData(caller=self, time=self.env.now, transmission=entity)
                    )

    def createEntity(self) -> Entity:
        self.partNumber += 1
        entityId = f'{self.item.type[0]}{self.partNumber}'
        entityName = f'{self.item.type}{self.partNumber}'
        return self.item(id=entityId, name=entityName)

    def calculateInterArrivalTime(self) -> float:
        return self.rng.generateNumber()
