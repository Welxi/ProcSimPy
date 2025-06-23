from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.Entity import Entity
from procsimpy.EventData import (
    InterruptEndEvent,
    InterruptEvent,
    ShiftEndEvent,
    ShiftStartEvent,
)
from procsimpy.Failure import Failure
from procsimpy.ShiftChange import ShiftChange
from simpy import Environment, Event, Interrupt, Process

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Line import Line
    from procsimpy.Node import Node


class Operation:
    def __init__(self, node: Node) -> None:
        self.node = node
        self.operating: bool = False
        self.waitingEvents: list[Event] = []

    def initialize(self, env: Environment, line: Line) -> None:
        self.env = env
        self.line = line
        self.process = self.env.process(self.run())

    def run(self) -> Generator:
        while True:
            try:
                if self.node.shift is None:
                    self.start()
                    yield self.process
                else:
                    nextShiftStart, nextShiftEnd = self.node.shift.next(self.env.now)

                    if nextShiftEnd < self.env.now:
                        if not self.operating:
                            self.stop(ShiftChange(cause='Shift End'))
                        yield self.process

                    # print(f'{self.env.now} : {nextShiftStart=}, {nextShiftEnd=}')

                    if self.node.shift.isOnShift(self.node.env.now):
                        self.start()
                        self.node.stats.wentOnShift()
                        self.node.printTrace(
                            ShiftStartEvent(time=self.env.now, caller=self.node)
                        )
                        yield self.env.timeout(nextShiftEnd - self.node.env.now)
                        self.stop(ShiftChange(cause='Shift End'))
                        self.node.printTrace(
                            ShiftEndEvent(time=self.env.now, caller=self.node)
                        )
                        self.node.stats.wentOffShift()
                    else:
                        if not self.operating:
                            self.stop(ShiftChange(cause='Shift End'))
                            self.node.stats.wentOffShift()

                        if nextShiftStart < self.env.now:
                            if not self.operating:
                                self.stop(ShiftChange(cause='Shift End'))
                            yield self.process

                        yield self.env.timeout(nextShiftStart - self.node.env.now)
                        self.start()
                        self.node.stats.wentOnShift()

            except Interrupt as interrupt:
                cause = interrupt.cause
                assert isinstance(cause, Failure)
                self.node.printTrace(
                    InterruptEvent(time=self.env.now, caller=self.node, cause=cause)
                )
                self.node.stats.failed()

                self.stop(cause=cause)

                with self.line.repairRequest(cause=cause) as repairRequest:
                    yield repairRequest
                    yield self.env.timeout(cause.TTR.generateNumber())
                    self.node.printTrace(
                        InterruptEndEvent(
                            time=self.env.now, caller=self.node, cause=cause
                        )
                    )
                    self.node.stats.repaired()
                    self.onRepair.succeed()
                    self.start()

    def isOperating(self) -> bool:
        return self.operating

    def start(self) -> None:
        self.operating = True
        self.node.fillAvailability()
        for event in self.waitingEvents:
            self.waitingEvents.remove(event)
            event.succeed()

        for item in self.node.store.items:
            assert isinstance(item, Entity)
            if item.toBeProcessed():
                self.node.process(item=item)

    def stop(self, cause: Failure | ShiftChange) -> None:
        self.operating = False
        self.node.clearAvailability()
        for process in self.node.workQueue:
            assert isinstance(process, Process)
            process.interrupt(cause)

    def onOperating(self) -> Event:
        event = self.env.event()
        self.waitingEvents.append(event)
        return event

    def failure(self, fail: Failure) -> Event:
        self.process.interrupt(cause=fail)
        self.onRepair = self.env.event()
        return self.onRepair
