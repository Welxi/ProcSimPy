from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from hepyaestus.baseClasses import BaseObject, CoreObject

if TYPE_CHECKING:
    from hepyaestus.Line import Line
    from simpy import Environment


class Entity(BaseObject):
    type = 'Entity'

    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)

    def initialize(
        self, env: Environment, line: Line, currentStation: Optional[CoreObject] = None
    ) -> None:
        super().initialize(env, line)
        self.creationTime = self.env.now
        self.startTime = self.env.now
        self.currentStation = currentStation if currentStation else None
