from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Self

from hepyaestus.Base import BaseObject
from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData
from simpy import Environment, Event, Store
from simpy.core import Infinity

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Line import Line
    from simpy.resources.store import StoreGet


class StoreNode(BaseObject, ABC):
    def __init__(self, id: str, name: str, capacity: float = Infinity) -> None:
        super().__init__(id, name)
        assert capacity >= 0, 'capacity must be possitive'
        self.capacity: float = capacity

        self.next: list[Self] = []
        self.previous: list[Self] = []

        # Needs to be in init so initialize can check for circular imports
        # in objects not yet initialized
        self.giver: Self | None = None
        self.receiver: Self | None = None

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.printTrace(init=None)
        self.canDispose: Event = self.env.event()
        self.isRequested: Event = self.env.event()
        self.initialWIP: Event = self.env.event()

        self.events: list[Event] = [self.canDispose, self.isRequested]

        self.giver: Self | None = self.previous[0] if self.previous else None
        self.receiver: Self | None = self.next[0] if self.next else None

        if self.giver is not None:
            assert self.giver.giver is not self, 'Circular Process Chain'
        if self.receiver is not None:
            assert self.receiver.receiver is not self, 'Circular Process Chain'

        self.totalWaitingTime = 0
        self.totalWorkingTime = 0
        self.store = Store(env, capacity=self.capacity)

    def defineRouting(
        self,
        predecessorList: Optional[list] = None,
        successorList: Optional[list] = None,
    ) -> None:
        self.previous: list[Self] = predecessorList if predecessorList else []
        self.next: list[Self] = successorList if successorList else []

    def give(self) -> StoreGet:
        return self.store.get()

    def receive(self, entity: Entity) -> None:
        entity.updateStation(station=self)
        self.store.put(entity)

    def canReceive(self) -> bool:
        return len(self.store.items) < self.capacity and not self.anyEventsTriggered()

    def canGive(self) -> bool:
        return len(self.store.items) > 0 and not self.canDispose.triggered

    def notEmpty(self) -> bool:
        return len(self.store.items) > 0

    def getActiveEntity(self) -> Entity | None:
        if self.notEmpty():
            entity = self.store.items[0]
            assert isinstance(entity, Entity)
            return entity
        else:
            return None

    @abstractmethod
    def run(self) -> Generator:
        raise NotImplementedError

    def anyEventsTriggered(self) -> bool:
        return (
            self.canDispose.triggered
            or self.isRequested.triggered
            or self.initialWIP.triggered
        )

    def canGiversGive(self) -> None:
        for giver in self.previous:
            if giver.canGive():
                self.giver = giver
                giver.canDispose.succeed(EventData(caller=self, time=self.env.now))
                break  # can only accept one at a time so once receiving break

    def canReceiversReceive(self) -> None:
        if not self.canGive():
            return
        for receiver in self.next:
            if receiver.canReceive():
                self.receiver = receiver
                self.canDispose.succeed(EventData(caller=self, time=self.env.now))
                break  # can only give one at a time so once requesting break

    def giveReceiverEntity(self, event: EventData) -> None:
        assert self.receiver is not None
        if self.receiver.canReceive():
            self.receiver.isRequested.succeed(event)
        else:
            # Race Condition during yield of Store Retry handover
            # if event.attempt > 10:
            #     raise
            self.canDispose.succeed(
                EventData(
                    caller=event.caller, time=self.env.now, attempt=event.attempt + 1
                )
            )
