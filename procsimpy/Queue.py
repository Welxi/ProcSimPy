from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.Entity import Entity
from procsimpy.EventData import EventData
from procsimpy.StoreNode import StoreNode

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Line import Line
    from simpy import Environment


class Queue(StoreNode):
    def __init__(
        self,
        id: str,
        name: str,
        *,
        capacity: int = 1,
        priority: int = 0,
    ) -> None:
        super().__init__(id, name, capacity=capacity, priority=priority)
        self.times = 0

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)

    def run(self) -> Generator:
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
                assert eventData.time == self.env.now
                self.isRequested = self.env.event()
                self.printTrace(isRequested=eventData)

                self._receive(eventData.transmission)

                if self.receiver.canReceive():
                    self.canDispose.succeed(EventData(caller=self, time=self.env.now))

            if self.canDispose in receivedEvents:
                assert self.canDispose.value is not None

                eventData = self.canDispose.value
                assert isinstance(eventData, EventData)
                assert eventData.time == self.env.now
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
                assert isinstance(eventData.transmission, Entity)
                self.initialWIP = self.env.event()
                self.printTrace(initialWIP=eventData)

                self._receive(eventData.transmission)
            self.canReceiversReceive()
            self.canGiversGive()
