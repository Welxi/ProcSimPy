from __future__ import annotations

from typing import TYPE_CHECKING

import simpy

if TYPE_CHECKING:
    from hepyaestus.Line import Line


class Experiment:
    def __init__(
        self,
        line: Line,
        seed: int = 42,
    ) -> None:
        self.line: Line = line
        self.seed: int = seed

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

        for interation in range(self.numberOfReplications):
            # TODO create RandomNumberGenerator with Seed Here
            print(f'Interation {interation}: Seed = {self.seed}')
            self.runIteration()
            self.seed += 1

    def runIteration(self) -> None:
        self.env = simpy.Environment()
        self.line.initialize(self.env)

        self.env.run(until=self.maxSimTime)
