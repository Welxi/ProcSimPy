from __future__ import annotations

from typing import TYPE_CHECKING

import simpy
from procsimpy.RandomNumberGenerator import SeedType, setSeed
from procsimpy.Results import Results

if TYPE_CHECKING:
    from procsimpy.Line import Line


class Experiment:
    """
    Orchastration Module or runing one or more SimPy Simulations
    """

    def __init__(
        self, line: Line, seed: int = 42, seedType: SeedType = SeedType.INT
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
        *,
        test: bool = False,
    ) -> Results:
        """
        initiate and returns results of defined experiment

        :param maxSimTime: Max allowed Time for Simulation, defaults to 100
        :type maxSimTime: float, optional
        :param numberOfReplications: how many times the experiment is ran, defaults to 1
        :type numberOfReplications: int, optional
        :param test: used for automated testing to avoid overlogging, defaults to False
        :type test: bool, optional
        :return: a collection of results of the defined experiment
        :rtype: Results
        """
        self.maxSimTime: float = maxSimTime
        self.numberOfReplications: int = numberOfReplications

        if test:
            self.line.turnTraceingOff()

        self._runIteration()

        while self.iteration < self.numberOfReplications:
            self.iteration += 1
            self.seed += 1
            self._runIteration()

        # TODO if one iteration just return the first stub
        # Could standardise this to the average and stubs are each iteration
        return self.results

    def _runIteration(self) -> None:
        """
        Internally called by run: Runs one iteration of the experiment
        """
        setSeed(seed=self.seed, seedType=self.seedType)
        self.env = simpy.Environment()
        self.line.initialize(self.env)

        self.env.run(until=self.maxSimTime)

        self.results.addIteration(simTime=self.env.now)
        # could return results and append in run
