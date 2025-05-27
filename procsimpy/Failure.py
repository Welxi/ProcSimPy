from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.Base import Base
from procsimpy.RandomNumberGenerator import RandomNumberGenerator

if TYPE_CHECKING:
    from collections.abc import Generator

    from procsimpy.Line import Line
    from procsimpy.Node import Node
    from procsimpy.ProbDistribution import ProbDistribution
    from simpy import Environment

# TODO Distinct Failure Types
# delayInteruption
# restartFailure
# scrapFailure
# repeating of each
# single fail of each


class Failure(Base):
    def __init__(
        self,
        id: str,
        name: str,
        *,
        victim: Node,
        TTF: ProbDistribution,
        TTR: ProbDistribution,
    ) -> None:
        super().__init__(id, name)
        self.TTF = RandomNumberGenerator(TTF)
        self.TTR = RandomNumberGenerator(TTR)
        self.victim = victim

    def initialize(self, env: Environment, line: Line) -> None:
        super().initialize(env, line)
        self.env.process(self.run())

    def run(self) -> Generator:
        while True:
            yield self.env.timeout(self.TTF.generateNumber())

            for process in self.victim.processes:
                process.interrupt(self)
