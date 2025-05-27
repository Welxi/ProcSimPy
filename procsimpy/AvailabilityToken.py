from __future__ import annotations

from dataclasses import dataclass, field
from itertools import count
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from procsimpy.Node import Node


@dataclass(frozen=True, slots=True, kw_only=True)
class AvailabilityToken:
    timeCreated: float
    node: Node
    id: int = field(default_factory=count().__next__, init=False)
