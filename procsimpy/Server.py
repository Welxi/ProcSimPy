from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.Node import Node

if TYPE_CHECKING:
    from procsimpy.ProbDistribution import ProbDistribution


class Server(Node):
    def __init__(
        self,
        id: str,
        name: str,
        *,
        capacity: int = 1,
        priority: int = 0,
        processingTime: ProbDistribution,
    ) -> None:
        super().__init__(
            id,
            name,
            capacity=capacity,
            priority=priority,
            processingTime=processingTime,
        )
