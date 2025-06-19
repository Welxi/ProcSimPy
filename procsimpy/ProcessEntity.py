from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.EventData import InterruptEvent
from procsimpy.Failure import Failure
from procsimpy.ShiftChange import ShiftChange
from simpy import Interrupt

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Entity import Entity


def ProcessEntity(entity: Entity) -> Generator:
    try:
        processingTime = entity.processingTime()

        entity.startProcessing()

        if processingTime is not None:
            yield entity.env.timeout(processingTime)

        entity.finishedProcessing()

    except Interrupt as interrupt:
        cause = interrupt.cause
        assert isinstance(cause, (Failure, ShiftChange))
        entity.currentNode.printTrace(
            InterruptEvent(time=entity.env.now, caller=entity.currentNode, cause=cause)
        )
        entity.pause(cause=cause)
