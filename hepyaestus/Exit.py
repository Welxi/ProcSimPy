from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData
from hepyaestus.StoreNode import StoreNode

if TYPE_CHECKING:
    from collections.abc import Generator


class Exit(StoreNode):
    def __init__(
        self,
        id: str,
        name: str,
        *,
        priority: int = 0,
    ) -> None:
        super().__init__(id, name, priority=priority)
        self.exits: list[Entity] = []

    def run(self) -> Generator:
        while True:
            yield self.isRequested
            assert self.isRequested.value is not None

            eventData = self.isRequested.value
            assert isinstance(eventData, EventData)
            assert isinstance(eventData.transmission, Entity)
            assert eventData.time == self.env.now
            self.isRequested = self.env.event()
            self.printTrace(isRequested=eventData)

            self._receive(eventData.transmission)

            self.canGiversGive()
