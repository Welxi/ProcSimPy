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
    from hepyaestus.ShiftScheduler import Shift
    from simpy.resources.store import StoreGet


class StoreNode(BaseObject, ABC):
    def __init__(
        self,
        id: str,
        name: str,
        capacity: float = Infinity,
        shift: Optional[Shift] = None,
        priority: int = 0,
    ) -> None:
        super().__init__(id, name)
        self.next: list[Self] = []
        self.previous: list[Self] = []

        # Needs to be in init so initialize can check for circular imports
        # in objects not yet initialized
        self.giver: Self | None = None
        self.receiver: Self | None = None

        self.priority: int = priority

        assert capacity >= 0, 'capacity must be possitive'
        self.capacity: float = capacity

        self.shift: Optional[Shift] = shift
        self.onShift = self.shift.isOnShift(0) if self.shift is not None else None

    def initialize(self, env: Environment, line: Line) -> None:
        """
        Initialize called by Line to preform setup
        or reseting between Experiment Iterations

        :param env: SimPy Environment, mainly used for creating events and knowing current time
        :type env: Environment
        :param line: Line Object for Learning about word state or general info
        :type line: Line
        """
        super().initialize(env, line)
        self.printTrace(init=None)
        self.canDispose: Event = self.env.event()
        self.isRequested: Event = self.env.event()
        self.initialWIP: Event = self.env.event()

        self.interruptionEnd = self.env.event()
        self.interruptionStart = self.env.event()

        self.events: list[Event] = [self.canDispose, self.isRequested]

        self.giver: Self | None = self.previous[0] if self.previous else None
        self.receiver: Self | None = self.next[0] if self.next else None

        # TODO Check whole list
        if self.giver is not None:
            assert self.giver.giver is not self, 'Circular Process Chain'
        if self.receiver is not None:
            assert self.receiver.receiver is not self, 'Circular Process Chain'

        self.store = Store(env, capacity=self.capacity)

    def defineRouting(
        self,
        predecessorList: Optional[list[Self]] = None,
        successorList: Optional[list[Self]] = None,
    ) -> None:
        """
        Setting up the Linked List for this Node, connecting it to its neighbours

        :param predecessorList: Nodes Preceding this Node, defaults to None
        :type predecessorList: Optional[list], optional
        :param successorList: Nodes After this Node, defaults to None
        :type successorList: Optional[list], optional
        """

        self.previous: list[Self] = predecessorList if predecessorList else []
        self.next: list[Self] = successorList if successorList else []

        # Check there is a link to at least one other node
        assert len(self.previous) + len(self.next) >= 1, (
            'Needs to be connected to at leat one other Node'
        )

    def _give(self) -> StoreGet:
        return self.store.get()

    def _receive(self, entity: Entity) -> None:
        entity.updateStation(station=self)
        self.store.put(entity)

    def canReceive(self) -> bool:
        """
        if the Node is able to Receive an Entity

        :return: True if can Receive
        :rtype: bool
        """
        return (
            len(self.store.items) < self.store.capacity
            and not self.anyEventsTriggered()
        )

    def canGive(self) -> bool:
        """
        if the Node can Give an Entity

        :return: True if can Give
        :rtype: bool
        """
        return self.notEmpty() and not self.canDispose.triggered

    def notEmpty(self) -> bool:
        """
        if the Node has Entities as Items in its SimPy Store

        :return: True if Entities are present
        :rtype: bool
        """
        return len(self.store.items) > 0

    def _getActiveEntity(self) -> Entity | None:
        """
        Return the Entity of that is to be Processed/Transferred next
        Should be used when a fact about the Entity should inform a decision

        :return: Entity first in queue
        :rtype: Entity | None
        """
        if self.notEmpty():
            entity = self.store.items[0]
            assert isinstance(entity, Entity)
            return entity
        else:
            return None

    @abstractmethod
    def run(self) -> Generator:
        raise NotImplementedError("Subclass must define 'run' method")

    def anyEventsTriggered(self) -> bool:
        """
        Checks all the SimPy Events registered
        and return whether they have been triggered and have yet to be processed

        :return: True if any e
        :rtype: bool
        """
        # could check attributes for events and add to list
        return any(
            (
                self.canDispose.triggered,
                self.isRequested.triggered,
                self.initialWIP.triggered,
            )
        )

    def canGiversGive(self) -> None:
        """
        Checks if Givers are available for handover
        and triggers a canDispose event if it is
        """
        if not self.canReceive():
            return
        for giver in self.previous:
            if giver.canGive():
                self.giver = giver
                giver.canDispose.succeed(EventData(caller=self, time=self.env.now))
                break  # can only accept one at a time so once receiving break

    def canReceiversReceive(self) -> None:
        """
        Checks if Receivers are available for handover
        and triggers a isRequested event if it is
        """
        if not self.canGive():
            return
        self.sortReceivers()
        for receiver in self.next:
            if receiver.canReceive():
                self.receiver = receiver
                self.canDispose.succeed(EventData(caller=self, time=self.env.now))
                break  # can only give one at a time so once requesting break

    def sortReceivers(self) -> None:
        """
        Sorts Receivers based on Priority or Line.routingPriority if set
        it is called each time canReceiversReceive is called
        You are incouraged to redefine this function if alternate sorting rules are required
        """
        if self.line.routingPriority is not None:
            self.next.sort(key=self.line.routingPriority)
        else:
            self.next.sort(key=lambda x: x.priority)

    def giveReceiverEntity(self, event: EventData) -> None:
        """
        Called during a can Dispose event, main purpose is to handle the
        race condition in the case of Parallel nodes

        :param event: Event to send or retry
        :type event: EventData
        """
        assert self.receiver is not None
        assert event.transmission is not None
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
