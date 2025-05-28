from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Optional

from procsimpy.Entity import Entity
from procsimpy.Node import Node
from procsimpy.ProcessEntity import ProcessEntity
from procsimpy.RandomNumberGenerator import RandomNumberGenerator
from simpy.core import Infinity

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Line import Line
    from procsimpy.ProbDistribution import ProbDistribution
    from simpy import Environment


class Source(Node):
    def __init__(
        self,
        id: str,
        name: str,
        *,
        arrivalTime: ProbDistribution,
        item: type[Entity] = Entity,
    ) -> None:
        super().__init__(
            id,
            name,
            capacity=Infinity,
        )
        self.arrivalTime: RandomNumberGenerator = RandomNumberGenerator(arrivalTime)

        self.partNumber: int = 0
        self.item = item

    def initialize(
        self,
        env: Environment,
        line: Line,
        *,
        processEntity: Callable[[Node], Generator] = ProcessEntity,
        processes: Optional[list[Callable[[Node], Generator]]] = None,
    ) -> None:
        if processes is None:
            processes = []
        processes.append(IntervalEntityGenerator)
        super().initialize(env, line, processEntity=processEntity, processes=processes)

    def createEntity(self) -> Entity:
        self.partNumber += 1
        entityId = f'{self.item.type[0]}{self.partNumber}'
        entityName = f'{self.item.type}{self.partNumber}'
        item = self.item(id=entityId, name=entityName)
        item.initialize(self.env, self.line, currentNode=self)
        return item


def IntervalEntityGenerator(node: Node) -> Generator:
    assert isinstance(node, Source)
    # This is need so that the function parameters match other processes

    while True:
        # could be changed to begin with wait
        #  but assumption about experiment that we begin at the most intresting time
        entity: Entity = node.createEntity()
        with node.put(entity) as handoff:
            yield handoff

        yield node.env.timeout(delay=node.arrivalTime.generateNumber())
