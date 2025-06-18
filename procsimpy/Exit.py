from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.EventData import ReceiveEvent
from procsimpy.Node import Node
from simpy.core import Infinity

if TYPE_CHECKING:
    from procsimpy.Entity import Entity
    from simpy.resources.store import StoreGet, StorePut


class Exit(Node):
    """
    A conceptual Node representing the completion of a process,
    they are assumed to always be available and have infinite capacity
    """

    def __init__(
        self,
        id: str,
        name: str,
    ) -> None:
        super().__init__(id, name, capacity=Infinity)

    def getToken(self) -> StoreGet:
        """
        Wrapper for Node.getToken() that puts an AvailabilityToken into availability,
          before request, this is because Exits are always available as they are
            conceptual buckets for the completion of the process

        :return: _description_
        :rtype: StoreGet
        """
        # Exits are always avaible so add Token before request
        # TODO Check if this will overfill and if that even matters
        #? could just return a token
        # not worry about availabilityStore
        self.availabilityStore.put(self.createToken())
        return super().getToken()

    def put(self, item: Entity) -> StorePut:
        """
        Overload of Node.put required to stop callback of ProcessEntity
        """
        self.printTrace(ReceiveEvent(time=self.env.now, caller=self, entity=item))

        item.updateStation(station=self)
        self.stats.receivedEntity(entity=item)

        return self.store.put(item)
