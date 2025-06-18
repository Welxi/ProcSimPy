from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from procsimpy.Failure import Failure
from procsimpy.ShiftChange import ShiftChange
from simpy import Interrupt

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Node import Node
    from simpy.core import SimTime


def ProcessEntity(node: Node) -> Generator:
    timeStarted: Optional[SimTime] = None
    processingTime = node.processingTime()
    try:
        # Processing needs to be before get Request
        # otherwise Entity is out of store while processing

        if processingTime is not None:
            timeStarted = node.env.now
            node.stats.startingProcessing()
            yield node.env.timeout(processingTime)
            node.stats.finishedProcessing()

        if not node.pendingHandover.triggered:
            node.pendingHandover.succeed()

        node.finishProcessing()

    except Interrupt as interrupt:
        cause = interrupt.cause
        assert isinstance(cause, (Failure, ShiftChange))

        if processingTime is not None and timeStarted is not None:
            timeSpent = node.env.now - timeStarted
            print(f'{timeSpent=}, {processingTime=}')
            timeRemaining = processingTime - timeSpent
            entity = node.getActiveEntity()
            entity.pause(timeRemaining)
