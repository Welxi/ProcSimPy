from __future__ import annotations

from enum import Enum
from random import Random

# import numpy as np
from procsimpy.ProbDistribution import DistributionType, ProbDistribution


class SeedType(Enum):
    INT = 'Int'
    OS = 'OS'


SEED: int | None = 42
generators: list[RandomNumberGenerator] = []


def setSeed(seed: int = 42, seedType: SeedType = SeedType.INT) -> None:
    match seedType:
        case SeedType.INT:
            SEED = seed
        case SeedType.OS:
            SEED = None

    for generator in generators:
        generator.Rnd.seed(SEED)


class RandomNumberGenerator:
    def __init__(self, distribution: ProbDistribution) -> None:
        if not isinstance(distribution, ProbDistribution):
            raise TypeError(
                'Distribution for Random Number Generator must inherit ProbDistribution'
            )
        self.Rnd = Random(SEED)
        # self.NpRnd = np.random.RandomState(SEED)
        self.distribution = distribution
        generators.append(self)

    def generateNumber(self) -> float:
        if (
            self.distribution.distributionType is DistributionType.CAUCHY
            or self.distribution.distributionType is DistributionType.GEOMETRIC
        ):
            # return self.distribution.distributionFunction(self.NpRnd)
            raise NotImplementedError
        return self.distribution.distributionFunction(self.Rnd)
