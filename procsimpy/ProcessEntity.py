from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.AvailabilityToken import AvailabilityToken
from procsimpy.Failure import Failure
from simpy import Interrupt
from simpy.resources.store import StoreGet

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Node import Node


def ProcessEntity(node: Node) -> Generator:
    try:
        # Processing needs to be before get Request
        # otherwise Entity is out of store while processing
        if node.processingTime is not None:
            node.stats.startingProcessing()
            yield node.env.timeout(node.processingTime.generateNumber())
            node.stats.finishedProcessing()

        with node.get(requestNode=node) as item:
            entity = yield item

            transactions = [successor.getToken() for successor in node.next]

            successors = yield node.env.any_of(transactions)
            assert successors is not None

            targets = [
                successors[transaction]
                for transaction in transactions
                if transaction in successors
                and not isinstance(successors[transaction], StoreGet)
            ]

            token: AvailabilityToken = node.routeEntity(targets)
            assert token is not None
            assert isinstance(token, AvailabilityToken)

            assert entity is not None
            with token.node.put(entity) as handoff:
                yield handoff

    except Interrupt as interrupt:
        cause = interrupt.cause
        assert isinstance(cause, Failure)
        with node.line.repairRequest(cause=cause) as repair:
            yield repair
            yield node.env.timeout(cause.TTR.generateNumber())
