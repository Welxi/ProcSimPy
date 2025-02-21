from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Self

from hepyaestus.EventData import EventData
from simpy import Environment, Resource, Store
from simpy.core import Infinity

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus.Entity import Entity
    from hepyaestus.Line import Line


class BaseObject:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name

    def initialize(self, env: Environment, line: Line) -> None:
        self.env = env
        self.line = line

    def printTrace(self, **kw) -> None:
        if not self.line.canTrace(self):
            return
        from hepyaestus.printTrace import printTrace

        for key, eventData in kw.items():
            if eventData is None:
                kw[key] = EventData(caller=self, time=self.env.now, trace=False)
        printTrace(self, **kw)


class CoreObject(BaseObject, ABC):
    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)
        self.next: list[Self] = []
        self.previous: list[Self] = []

        # Needs to be in init so initialize can check for circular imports
        # in objects not yet initialized
        self.giver: Self | None = None
        self.receiver: Self | None = None

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.printTrace(init=None)
        self.canDispose = self.env.event()
        self.isRequested = self.env.event()

        self.giver: Self | None = self.previous[0] if self.previous else None
        self.receiver: Self | None = self.next[0] if self.next else None

        if self.giver is not None:
            assert self.giver.giver is not self, 'Circular Process Chain'
        if self.receiver is not None:
            assert self.receiver.receiver is not self, 'Circular Process Chain'

        self.totalWaitingTime = 0
        self.totalWorkingTime = 0

    def defineRouting(
        self,
        predecessorList: Optional[list] = None,
        successorList: Optional[list] = None,
    ) -> None:
        self.previous: list[Self] = predecessorList if predecessorList else []
        self.next: list[Self] = successorList if successorList else []

    @abstractmethod
    def run(self) -> Generator:
        raise NotImplementedError

    # abstract methods need to have the same return type
    # need to create generic of give and recieve for store ans resource

    # @abstractmethod
    # def receive(self, entity: Entity) -> None:
    #     pass

    # @abstractmethod
    # def give(self):
    #     pass

    @abstractmethod
    def canReceive(self) -> bool:
        return False

    @abstractmethod
    def canGive(self) -> bool:
        return False

    def anyEventsTriggered(self) -> bool:
        return self.canDispose.triggered or self.isRequested.triggered

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


class StoreObject(CoreObject):
    def __init__(self, id: str, name: str, capacity: float = Infinity) -> None:
        super().__init__(id, name)
        assert capacity >= 0, 'capacity must be possitive'
        self.capacity: float = capacity

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.store = Store(env, capacity=self.capacity)

    def give(self):
        return self.store.get()

    def receive(self, entity: Entity) -> None:
        entity.updateStation(station=self)
        self.store.put(entity)

    def canReceive(self) -> bool:
        return len(self.store.items) < self.capacity and not self.anyEventsTriggered()

    def canGive(self) -> bool:
        return len(self.store.items) > 0 and not self.canDispose.triggered


class ResourceObject(CoreObject):
    def __init__(self, id: str, name: str, capacity: int = 1) -> None:
        super().__init__(id, name)
        assert capacity >= 0, 'capacity must be possitive'
        self.capacity: int = capacity

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.res = Resource(env, capacity=self.capacity)

    def give(self):
        return NotImplementedError

    def receive(self, entity: Entity):
        return NotImplementedError

    def canReceive(self) -> bool:
        return len(self.res.users) < self.capacity and not self.isRequested.triggered
