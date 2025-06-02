from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from procsimpy.Node import Node

if TYPE_CHECKING:
    from procsimpy.ShiftScheduler import Shift


class Queue(Node):
    def __init__(
        self,
        id: str,
        name: str,
        *,
        capacity: int = 1,
        priority: Optional[int] = None,
        shift: Optional[Shift] = None,
    ) -> None:
        super().__init__(
            id,
            name,
            capacity=capacity,
            priority=priority,
            shift=shift,
        )
