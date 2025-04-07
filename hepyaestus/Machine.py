from __future__ import annotations

from itertools import count
from typing import TYPE_CHECKING, Callable

from hepyaestus.Entity import Entity
from hepyaestus.EventData import EventData
from hepyaestus.Line import Line
from hepyaestus.RandomNumberGenerator import RandomNumberGenerator
from hepyaestus.StoreNode import StoreNode
from simpy import Environment, Store

if TYPE_CHECKING:
    from collections.abc import Generator

    from hepyaestus import Line
    from hepyaestus.Base import BaseObject
    from hepyaestus.ProbDistribution import ProbDistribution
    from simpy import Environment
    from simpy.resources.store import StoreGet


class ProcessForTime:
    def __init__(self, env: Environment, machine: Machine) -> None:
        self.id = count().__next__()
        self.env = env
        self.machine = machine
        self.startTime = self.env.now
        self.isInterupted = False

    def run(self, processTime: float, callback: Callable) -> Generator:
        self.startTime = self.env.now
        yield self.env.timeout(delay=processTime)
        if self.isInterupted is False:
            self.env.process(callback(process=self))
        else:
            print('has been interupted')

    def interupt(self, caller: BaseObject) -> None:
        self.isInterupted = True
        self.interuption = caller
        self.interuptionTime = self.env.now


class Machine(StoreNode):
    def __init__(
        self,
        id: str,
        name: str,
        *,
        processingTime: ProbDistribution,
        capacity: int = 1,
        priority: int = 0,
        processEntity=ProcessForTime,
    ) -> None:
        super().__init__(id, name, capacity=capacity, priority=priority)
        self.processingTime: RandomNumberGenerator = RandomNumberGenerator(
            distribution=processingTime
        )
        self.process = processEntity

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.outputStore = Store(env=env, capacity=self.capacity)
        self.activeProcess: list[ProcessForTime] = []
        self.pro = self.process(env=env, machine=self)

    def run(self) -> Generator:
        while True:
            receivedEvents = yield self.env.any_of(
                [
                    self.isRequested,
                    self.canDispose,
                    self.initialWIP,
                    self.interruptionStart,
                    # self.interruptionEnd,
                ]
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
                self.startEntityProcess(entity=eventData.transmission)

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

            if self.interruptionStart in receivedEvents:
                assert self.interruptionStart.value is not None
                eventData = self.interruptionStart.value
                assert isinstance(eventData, EventData)

                self.interruptionStart = self.env.event()
                self.printTrace(interrupted=eventData)

                for process in self.activeProcess:
                    process.interupt(caller=eventData.caller)

                yield self.interruptionEnd

                assert self.interruptionEnd.value is not None
                eventData = self.interruptionEnd.value
                assert isinstance(eventData, EventData)

                self.interruptionEnd = self.env.event()
                self.printTrace(interruptEnd=eventData)
                for entity in self.getStoreQueue():
                    self.startEntityProcess(entity=entity)

            # if self.interruptionEnd in receivedEvents:

            # self.canReceiversReceive()
            # moved to process callback
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

    def _give(self) -> StoreGet:
        entity = self.getOutputEntity()
        assert entity is not None
        self.stats.givenEntity(entity=entity)
        return self.outputStore.get()

    def getOutputEntity(self) -> Entity | None:
        if self.outputNotEmpty():
            entity = self.outputStore.items[0]
            # Make sure this is a copy not reference
            assert isinstance(entity, Entity)
            return entity

        else:
            return None

    def canGive(self) -> bool:
        return self.outputNotEmpty() and not self.canDispose.triggered

    def canReceive(self) -> bool:
        usage = len(self.store.items) + len(self.outputStore.items)
        return usage < self.store.capacity and not self.anyEventsTriggered()

    def outputNotEmpty(self) -> bool:
        return len(self.outputStore.items) > 0

    def processEntity(self, process) -> Generator:
        entity = yield self.store.get()
        self.outputStore.put(entity)
        self.activeProcess.remove(process)
        # self.stats.finishedProcessing()
        self.canReceiversReceive()

    def startEntityProcess(self, entity: Entity) -> None:
        process = self.process(env=self.env, machine=self)
        self.env.process(
            process.run(
                processTime=self.calculateProcessingTime(),
                callback=self.processEntity,
            )
        )
        self.activeProcess.append(process)
