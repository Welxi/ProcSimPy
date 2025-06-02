from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.AvailabilityToken import AvailabilityToken
from procsimpy.Entity import Entity
from procsimpy.Failure import Failure
from simpy import Interrupt

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Node import Node


def ProcessEntity(node: Node) -> Generator:
    try:
        # Processing needs to be before get Request
        # otherwise Entity is out of store while processing
        processingTime = node.processingTime()
        if processingTime is not None:
            node.stats.startingProcessing()
            yield node.env.timeout(processingTime)
            node.stats.finishedProcessing()

        entity = yield node.get()
        assert entity is not None
        assert isinstance(entity, Entity)

        transactions = [successor.getToken() for successor in node.next]

        successors = yield node.env.any_of(transactions)
        assert successors is not None

        for transaction in transactions:
            if not transaction.triggered:
                transaction.cancel()

        targets = [
            successors[transaction]
            for transaction in transactions
            if transaction in successors
            # and not isinstance(successors[transaction], StoreGet)
            # cant remember what this was for
        ]

        token: AvailabilityToken = node.routeEntity(targets)
        assert token is not None
        assert isinstance(token, AvailabilityToken)

        for target in targets:
            if target is not token:
                # print(f'{target=}, {token=}')
                # TODO replenish token if unused
                assert isinstance(target, AvailabilityToken)
                target.node.availabilityStore.put(target)
                # print(target.node.availabilityStore.items)
                # Trying to replace

        with token.node.put(entity) as handoff:
            # ? could do some time checking to make sure there is no waiting at this point
            yield handoff

    except Interrupt as interrupt:
        cause = interrupt.cause
        assert isinstance(cause, Failure)
        with node.line.repairRequest(cause=cause) as repair:
            yield repair
            yield node.env.timeout(cause.TTR.generateNumber())
