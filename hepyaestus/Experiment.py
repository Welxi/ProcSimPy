from __future__ import annotations

from typing import TYPE_CHECKING

import simpy
from hepyaestus.RandomNumberGenerator import SeedType, setSeed
from hepyaestus.Results import Results

if TYPE_CHECKING:
    from hepyaestus.Line import Line
# ? End simulation early, why would it be needed


class Experiment:
    def __init__(
        self, *, line: Line, seed: int = 42, seedType: SeedType = SeedType.INT
    ) -> None:
        self.iteration: int = 1
        self.line: Line = line
        self.seed: int = seed
        self.seedType: SeedType = seedType
        self.results: Results = Results(line=self.line)

    def run(
        self,
        maxSimTime: float = 100,
        numberOfReplications: int = 1,
        test: bool = False,
    ) -> Results:
        self.maxSimTime: float = maxSimTime
        self.numberOfReplications: int = numberOfReplications

        if test:
            self.line.turnTraceingOff()

        self.runIteration()

        while self.iteration < self.numberOfReplications:
            self.iteration += 1
            self.seed += 1
            self.runIteration()

        return self.results

    def runIteration(self) -> None:
        print(f'Iteration {self.iteration}: Seed = {self.seed}')
        setSeed(seed=self.seed, seedType=self.seedType)
        self.env = simpy.Environment()
        self.line.initialize(self.env)

        self.env.run(until=self.maxSimTime)

        self.results.addIteration(simTime=self.env.now)

    # TODO log sim time as experiment results
