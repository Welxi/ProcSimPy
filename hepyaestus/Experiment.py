from __future__ import annotations

from typing import TYPE_CHECKING

import simpy
from hepyaestus.RandomNumberGenerator import SeedType, setSeed

if TYPE_CHECKING:
    from hepyaestus.Line import Line


class Experiment:
    def __init__(
        self, line: Line, seed: int = 42, seedType: SeedType = SeedType.INT
    ) -> None:
        self.interation: int = 1
        self.line: Line = line
        self.seed: int = seed
        self.seedType = seedType

    def run(
        self,
        maxSimTime: float = 100,
        numberOfReplications: int = 1,
        test: bool = False,
    ) -> None:
        self.maxSimTime: float = maxSimTime
        self.numberOfReplications: int = numberOfReplications

        if test:
            self.line.turnTraceingOff()

        self.runIteration()

        while self.interation < self.numberOfReplications:
            self.interation += 1
            self.seed += 1
            self.runIteration()

    def runIteration(self) -> None:
        print(f'Interation {self.interation}: Seed = {self.seed}')
        setSeed(seed=self.seed, seedType=self.seedType)
        self.env = simpy.Environment()
        self.line.initialize(self.env)

        self.env.run(until=self.maxSimTime)
