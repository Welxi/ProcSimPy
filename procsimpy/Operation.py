from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy import Failure
from simpy import Interrupt

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Node import Node


class Operation:
    def __init__(self, node: Node) -> None:
        self.node = node
        self.env = node.env
        self.line = node.line
        self.operating: bool = False

    def run(self) -> Generator:
        # Trying to model if a node is operating/ onShift and only then processing
        # might need to use events to model this
        # ? Turn into class that runs this procees and updates state that can be requested
        # if requests are made would need events made/triggerd
        while True:
            try:
                nextShiftStart, nextShiftEnd = self.node.shift.next(self.env.now)

                if self.node.shift.isOnShift(self.node.env.now):
                    self.operating = True
                    self.node.fillAvailability()
                    yield self.env.timeout(nextShiftEnd - self.env.now)
                    self.operating = False
                    self.node.clearAvailability()
                    # Disallow Process Entity
                    for process in self.node.processes:
                        process.interrupt('Shift Change')
                else:
                    self.operating = False
                    self.node.clearAvailability()
                    yield self.env.timeout(nextShiftStart - self.env.now)
                    self.operating = True
                    self.node.fillAvailability()
                    # self.reactivate()
                    # enable processEntity calls
            except Interrupt as interrupt:
                self.operating = False
                self.node.clearAvailability()
                cause = interrupt.cause
                assert isinstance(cause, Failure)

                with self.line.repairRequest(cause=cause) as repair:
                    yield repair
                    yield self.env.timeout(cause.TTR.generateNumber())
                    self.operating = True
                    self.node.fillAvailability()

    def isOperating(self) -> bool:
        return self.operating
