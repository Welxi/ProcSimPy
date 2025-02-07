from random import Random

# import numpy as np
from hepyaestus.ProbDistribution import DistributionType, ProbDistribution

SEED = 42


class RandomNumberGenerator:
    # TODO: insert Seed via init argument
    def __init__(self, distribution: ProbDistribution, seed: int = SEED) -> None:
        if not isinstance(distribution, ProbDistribution):
            raise TypeError(
                'Distribution for Random Number Generator must be a dictionary'
            )
        self.Rnd = Random(SEED)
        # self.NpRnd = np.random.RandomState(SEED)
        self.distribution = distribution

    def generateNumber(self) -> float:
        if self.distribution.distributionType is DistributionType.CAUCHY:
            # return self.distribution.distributionFunction(self.NpRnd)
            raise NotImplementedError
        return self.distribution.distributionFunction(self.Rnd)
