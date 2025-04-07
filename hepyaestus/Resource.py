from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.Base import BaseObject
from simpy import Environment, Resource

if TYPE_CHECKING:
    from hepyaestus.Line import Line
    from simpy.resources.resource import Request


class ResourceObject(BaseObject):
    def __init__(self, id: str, name: str, *, capacity: int = 1) -> None:
        super().__init__(id, name)
        assert capacity >= 0, 'capacity must be possitive'
        self.capacity: int = capacity

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.res = Resource(env, capacity=self.capacity)

    def request(self) -> Request:
        return self.res.request()

    def isAvailable(self) -> bool:
        return len(self.res.users) < self.capacity
