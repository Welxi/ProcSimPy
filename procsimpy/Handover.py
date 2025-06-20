from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.AvailabilityToken import AvailabilityToken
from procsimpy.Entity import Entity

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Node import Node


def Handover(node: Node) -> Generator:
    while True:
        if not node.operation.isOperating():
            onOperating = node.operation.onOperating()
            yield onOperating
        # Check if entities are ready
        if not node.haveProcessedEntities():
            # print('Waiting')
            yield node.pendingHandover
            node.pendingHandover = node.env.event()

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

        assert targets is not None
        assert all(isinstance(t, AvailabilityToken) for t in targets)

        token: AvailabilityToken = node.routeEntity(targets)
        assert token is not None
        assert isinstance(token, AvailabilityToken)

        for target in targets:
            if target is not token:
                # replenish token if unused
                assert isinstance(target, AvailabilityToken)
                target.node.availabilityStore.put(target)

        entity = yield node.get()
        assert entity is not None
        assert isinstance(entity, Entity)
        entity.transit()

        with token.node.put(entity) as handoff:
            # ? could do some time checking to make sure there is no waiting at this point
            yield handoff
