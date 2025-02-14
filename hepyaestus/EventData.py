from __future__ import annotations

from dataclasses import dataclass, field
from itertools import count
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hepyaestus.baseClasses import BaseObject
    from hepyaestus.Entity import Entity


@dataclass(frozen=True, slots=True, kw_only=True)
class EventData:
    time: float
    caller: BaseObject
    transmission: Entity | None = None
    id: int = field(default_factory=count().__next__, init=False)
