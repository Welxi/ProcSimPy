from abc import ABC, abstractmethod
from collections.abc import Generator

from hepyaestus.Base import BaseObject
from hepyaestus.EventData import EventData
from hepyaestus.Line import Line
from hepyaestus.Store import StoreNode
from simpy import Environment, Event


class Interruption(BaseObject, ABC):
    def __init__(self, id: str, name: str, victim: StoreNode) -> None:
        super().__init__(id, name)
        self.victim: StoreNode = victim

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)

        assert isinstance(self.victim.interruptionStart, Event), (
            'interruptionStart must be event'
        )
        assert isinstance(self.victim.interruptionEnd, Event), (
            'interruptionEnd must be event'
        )

    @abstractmethod
    def run(self) -> Generator:
        raise NotImplementedError("Subclass must define 'run' method")

    def interrupt(self) -> None:
        self.victim.interruptionStart.succeed(EventData(caller=self, time=self.env.now))

    def reactivate(self) -> None:
        self.victim.interruptionEnd.succeed(EventData(caller=self, time=self.env.now))
