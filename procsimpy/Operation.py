from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy import Failure
from simpy import Interrupt

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Node import Node


def Operation(node: Node) -> Generator:
    # Trying to model if a node is operating/ onShift and only then processing
    # might need to use events to model this
    # ? Turn into class that runs this procees and updates state that can be requested
    # if requests are made would need events made/triggerd
    while True:
        try:
            nextShiftStart, nextShiftEnd = node.shift.next(node.env.now)

            if node.shift.isOnShift(node.env.now):
                # Allow Process Entity
                yield node.env.timeout(nextShiftEnd - node.env.now)
                # Disallow Process Entity
                for process in node.processes:
                    process.interrupt('Shift Change')
            else:
                yield node.env.timeout(nextShiftStart - node.env.now)
                # self.reactivate()
                # enable processEntity calls
        except Interrupt as interrupt:
            cause = interrupt.cause
            assert isinstance(cause, Failure)

            with node.line.repairRequest(cause=cause) as repair:
                yield repair
                yield node.env.timeout(cause.TTR.generateNumber())
