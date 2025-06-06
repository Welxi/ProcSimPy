from __future__ import annotations

from collections.abc import Generator
from typing import TYPE_CHECKING, Callable, Optional

from procsimpy.AvailabilityToken import AvailabilityToken
from procsimpy.Base import Base
from procsimpy.EventData import GiveEvent, InitEvent, ReceiveEvent
from procsimpy.Operation import Operation
from procsimpy.ProcessEntity import ProcessEntity
from procsimpy.RandomNumberGenerator import RandomNumberGenerator
from procsimpy.ShiftScheduler import Shift, ShiftBuilder
from procsimpy.Statistics import Statistics
from simpy import Store
from simpy.resources.store import StoreGet, StorePut

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Entity import Entity
    from procsimpy.Line import Line
    from procsimpy.ProbDistribution import ProbDistribution
    from simpy import Environment
    from simpy.core import SimTime
    from simpy.resources.store import StoreGet, StorePut


class Node(Base):
    """
    Component that proforms a step in the Process, this is a Generic that
     many of your components may inherit from
    """

    def __init__(
        self,
        id: str,
        name: str,
        *,
        capacity: int | float = 1,
        priority: Optional[int] = None,
        processingTime: Optional[ProbDistribution] = None,
        shift: Optional[Shift] = None,
    ) -> None:
        super().__init__(id, name)
        self.capacity: int | float = capacity
        self.priority: Optional[int] = priority

        self.processingTimeGenerator = (
            RandomNumberGenerator(processingTime) if processingTime else None
        )
        self.canPrint: bool = False

    def initialize(  # type: ignore
        self,
        env: Environment,
        line: Line,
        *,
        processEntity: Callable[[Node], Generator] = ProcessEntity,
        processes: Optional[list[Callable[[Node], Generator]]] = None,
    ) -> None:
        """
        Initialize called by Line to preform setup
        or reseting between Experiment Iterations

        :param env: SimPy Environment, for engaging with SimPy Simulaion tools
        :type env: Environment
        :param line: Collection of Nodes and Resources
        :type line: Line
        :param processEntity: Process called when receiving Entity, defaults to ProcessEntity
        :type processEntity: Callable[[Node], Generator], optional
        :param processes: Optional Processes to describe Node, defaults to None
        :type processes: Optional[list[Callable[[Node], Generator]]], optional
        """
        super().initialize(env, line)
        self.stats = Statistics(env=self.env)

        self.store = Store(env=self.env, capacity=self.capacity)

        self.maxTransactions = max(len(self.previous), 1)
        # in case of Source no previous is provided
        # could overload methods to not need availabilityStore
        self.availabilityStore = Store(env=self.env, capacity=self.maxTransactions)
        self.fillAvailability()

        self.processEntity = processEntity
        self.processes = []

        if processes is not None:
            for process in processes:
                self.processes.append(self.env.process(process(self)))

        self.shift = ShiftBuilder(pattern=(10, 5))
        self.operation = Operation(self)

        self.printTrace(InitEvent(time=self.env.now, caller=self))

        # TODO Check for Circular Routing

    def defineRouting(
        self,
        predecessorList: Optional[list[Node]] = None,
        successorList: Optional[list[Node]] = None,
    ) -> None:
        self.previous: list[Node] = predecessorList if predecessorList else []
        self.next: list[Node] = successorList if successorList else []

        # rest of this is not used anymore

        # Check there is a link to at least one other node
        assert len(self.previous) + len(self.next) >= 1, (
            f'{self.name} needs to be connected to at leat one other Node'
        )
        self.giver: Node | None = self.previous[0] if self.previous else None
        self.receiver: Node | None = self.next[0] if self.next else None

    def get(self) -> StoreGet:
        request = self.store.get()
        request.callbacks.append(lambda eventType: self.addAvailability(eventType))
        request.callbacks.append(
            lambda eventType: self.printTrace(GiveEvent(time=self.env.now, caller=self))
        )
        # Could add active entity function to enable tracking of entity exits
        request.callbacks.append(lambda eventType: self.stats.givenEntity())
        return request

    def put(self, item: Entity) -> StorePut:
        self.printTrace(ReceiveEvent(time=self.env.now, caller=self, entity=item))

        item.updateStation(station=self)
        self.stats.receivedEntity(entity=item)

        putRequest = self.store.put(item)
        putRequest.callbacks.append(lambda eventType: self.process())
        # can move to process for operation that triggers, process entity
        return putRequest

    def process(self) -> None:
        # need this function as request callbacks need a return type of None
        process = self.env.process(self.processEntity(self))
        self.processes.append(process)
        process.callbacks.append(lambda eventType: self.processes.remove(process))

    def processingTime(self) -> SimTime | None:
        activeEntity = self._getActiveEntity()
        if activeEntity.remainingProcessingTime is not None:
            return activeEntity.remainingProcessingTime.generateNumber()
        if self.processingTimeGenerator is not None:
            return self.processingTimeGenerator.generateNumber()
        return None

    def _getActiveEntity(self) -> Entity:
        return self.store.items[0]

    @property
    def availability(self) -> int:
        """
        # Availability is amount of space available or max no of transactions
        # whichever is smaller
        # for the case of a store with infinite capacity a limit is required

        :return: _description_
        :rtype: int
        """
        currentCapacity = self.capacity - len(self.store.items)
        return int(min(currentCapacity, self.maxTransactions))

    def createToken(self) -> AvailabilityToken:
        return AvailabilityToken(timeCreated=self.env.now, node=self)

    def getToken(self) -> StoreGet:
        return self.availabilityStore.get()

    def addAvailability(self, eventType) -> None:
        self.availabilityStore.put(self.createToken())

    def fillAvailability(self) -> None:
        # this currently assumes an empty store
        for _ in range(self.availability):
            self.availabilityStore.items.append(self.createToken())
            # ? any advantage to using put Request?
            # trigger get Requests?

    def clearAvailability(self) -> None:
        for token in self.availabilityStore.items:
            self.availabilityStore.items.remove(token)

    def routeEntity(self, targets: list[AvailabilityToken]) -> AvailabilityToken:
        """
        Is call in Process Enitity to decide between availale targets for handover of entity.
        First checking Line for User defined function
        Second checks if Priority is set on any node
        Defaults to longest waiting

        if Different routing is required it is encouraged to overload this method for the node in question

        :param targets: the list of succerssor node that are currently available
        :type targets: list[AvailabilityToken]
        :return: the token to targets with handover
        :rtype: AvailabilityToken
        """
        assert len(targets) >= 1, 'Must have targets to route'
        if len(targets) == 1:
            return targets[0]

        if self.line.routingPriority is not None:
            return self.line.routingPriority(targets)

        if any(target.node.priority is not None for target in targets):
            targets.sort(
                reverse=True, key=lambda t: t.node.priority if t.node.priority else 0
            )
            return targets[0]

        else:
            # Defaults to node longest waiting
            targets.sort(key=lambda t: t.node.stats.timeLastEntityExited)
            return targets[0]
