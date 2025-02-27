from hepyaestus.Base import BaseObject
from hepyaestus.Line import Line
from simpy import Environment, Resource


class ResourceObject(BaseObject):
    def __init__(self, id: str, name: str, capacity: int = 1) -> None:
        super().__init__(id, name)
        assert capacity >= 0, 'capacity must be possitive'
        self.capacity: int = capacity

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.res = Resource(env, capacity=self.capacity)
