from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData
from hepyaestus.RandomNumberGenerator import RandomNumberGenerator
from hepyaestus.Store import StoreNode

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Line import Line
    from hepyaestus.ProbDistribution import ProbDistribution
    from simpy import Environment, Event


class EntityGenerator:
    def __init__(self, source: Source, env: Environment, line: Line) -> None:
        self.env: Environment = env
        self.line: Line = line
        self.type = 'EntityGenerator'
        self.source: Source = source

    def run(self) -> Generator:
        while True:
            self.source.entityCreated.succeed(
                # Adding caller as source because caller needs to be a Node
                EventData(
                    caller=self.source,
                    time=self.source.env.now,
                    transmission=self.source.createEntity(),
                    trace=False,
                )
            )

            yield self.env.timeout(self.source.calculateInterArrivalTime())


class Source(StoreNode):
    def __init__(
        self,
        id: str,
        name: str,
        interArrivalTime: ProbDistribution,
        entity: Optional[type[Entity]] = None,
        priority: int = 0,
    ) -> None:
        super().__init__(id, name, priority=priority)
        self.partNumber: int = 0
        self.item = entity if entity else Entity

        self.type = 'Source'
        self.rng = RandomNumberGenerator(interArrivalTime)
        self.times = 0

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.entityCreated: Event = self.env.event()
        self.events.append(self.entityCreated)

        self.entityGenerator = EntityGenerator(
            source=self, env=self.env, line=self.line
        )
        self.env.process(self.entityGenerator.run())

    def run(self) -> Generator:
        while True:
            yield self.entityCreated
            assert self.entityCreated.value is not None

            eventData = self.entityCreated.value
            assert isinstance(eventData, EventData)
            assert isinstance(eventData.transmission, Entity)
            assert eventData.time == self.env.now
            self.entityCreated = self.env.event()

            self._receive(eventData.transmission)

            assert self.receiver is not None
            if self.receiver.canReceive():
                entity = yield self._give()
                assert isinstance(entity, Entity)
                assert self.receiver is not None
                self.receiver.isRequested.succeed(
                    EventData(caller=self, time=self.env.now, transmission=entity)
                )

    def createEntity(self):
        self.partNumber += 1
        entityId = f'{self.item.type[0]}{self.partNumber}'
        entityName = f'{self.item.type}{self.partNumber}'
        item = self.item(id=entityId, name=entityName)
        item.initialize(self.env, self.line, currentStation=self)
        return item

    def calculateInterArrivalTime(self) -> float:
        return self.rng.generateNumber()
