from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from procsimpy.Entity import Entity
from procsimpy.EventData import ReceiveEvent
from procsimpy.Node import Node
from simpy.core import Infinity
from simpy.resources.store import StorePut

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Line import Line
    from simpy import Environment
    from simpy.resources.store import StoreGet


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

    # def initialize(
    #     self,
    #     env: Environment,
    #     line: Line,
    #     *,
    #     processes: list[Callable[[Node], Generator]],
    # ) -> None:
    #     """
    #     sets/resets Exit for new simulation

    #     :param env: SimPy Enviroment
    #     :type env: Environment
    #     :param line: Line Orchestration Module
    #     :type line: LineNode
    #     :param processes: only here to maintain standard no passthrough allowed
    #     :type processes: list[Callable[[Node], Generator]]
    #     """
    #     # TODO filter to remove process entity instead of not allowing passthrough
    #     super().initialize(env, line, processes=[])

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
