import math
from abc import ABC, abstractmethod
from enum import Enum


# Still not sure Enum is the best store of this
# Could Change it to just if it wants numpy or random
class DistributionType(Enum):
    FIXED = 'Fixed'
    NORMAL = 'Normal'
    EXP = 'Exp'
    GAMMA = 'Gamma'
    LOGISTIC = 'Logistic'
    ERLANG = 'Erlang'
    GEOMETRIC = 'Geometric'
    LOGNORMAL = 'Lognormal'
    WEIBULL = 'Weibull'
    CAUCHY = 'Cauchy'
    TRIANGULAR = 'Triangular'


class ProbDistribution(ABC):
    def __init__(
        self,
        distributionType: DistributionType,
    ) -> None:
        """
        Probability Distribution to be feed into a Random Number Generator
        """
        if distributionType not in DistributionType:
            raise ValueError(
                'Invalid Distribution Type provided for Probability Distribution'
            )
        self.distributionType: DistributionType = distributionType

    @abstractmethod
    def distributionFunction(self, RanNumGenerator) -> float:
        """this function will be called by the RandomNumberGenerator"""
        raise NotImplementedError('Please Implement this method')


class FixedDistribution(ProbDistribution):
    def __init__(self, mean: float) -> None:
        super().__init__(DistributionType.FIXED)
        self.mean: float = mean

    def distributionFunction(self, RanNumGenerator) -> float:
        return self.mean


class NormalDistribution(ProbDistribution):
    def __init__(self, mean: float, stdev: float, min: float, max: float) -> None:
        super().__init__(DistributionType.NORMAL)
        if max < min:
            raise ValueError('max must be greater than min')
        self.mean: float = mean
        self.stdev: float = stdev
        self.min: float = min
        self.max: float = max

    def distributionFunction(self, RanNumGenerator) -> float:
        while 1:
            number: float = RanNumGenerator.normalvariate(self.mean, self.stdev)
            if self.min < number < self.max:
                return number
        return 0.0


class ExpDistribution(ProbDistribution):
    def __init__(self, mean: float) -> None:
        super().__init__(DistributionType.EXP)
        if mean <= 0:
            raise ValueError('Mean cannot be less than or equal to 0')

        self.mean: float = mean

    def distributionFunction(self, RanNumGenerator) -> float:
        return RanNumGenerator.expovariate(1.0 / (self.mean))


class GammaDistribution(ProbDistribution):
    def __init__(self, alpha: float, beta: float, shape: float, rate: float) -> None:
        super().__init__(DistributionType.GAMMA)
        # PLAN Value Check Input
        self.alpha: float = alpha
        self.beta: float = beta
        self.shape: float = shape
        self.rate: float = rate

        if not self.alpha:
            self.alpha: float = self.shape
        if not self.beta:
            self.beta: float = 1 / float(self.rate)

    def distributionFunction(self, RanNumGenerator) -> float:
        return RanNumGenerator.gammavariate(self.alpha, self.beta)


class LogisticDistribution(ProbDistribution):
    def __init__(self, mean: float, scale: float) -> None:
        super().__init__(DistributionType.LOGISTIC)
        # PLAN Value Check Input
        self.mean: float = mean
        self.scale: float = scale

    def distributionFunction(self, RanNumGenerator) -> float:
        while 1:
            x: float = RanNumGenerator.random()
            number: float = self.mean + self.scale * math.log(x / (1 - x))
            if number > 0:
                return number
        return 0.0


class ErlangDistribution(ProbDistribution):
    def __init__(self, alpha: float, beta: float, shape: float, rate: float) -> None:
        super().__init__(DistributionType.ERLANG)
        # PLAN Value Check Input
        self.alpha: float = alpha
        self.beta: float = beta
        self.shape: float = shape
        self.rate: float = rate

        if not self.alpha:
            self.alpha: float = self.shape
        if not self.beta:
            self.beta: float = 1 / float(self.rate)

    def distributionFunction(self, RanNumGenerator) -> float:
        return RanNumGenerator.gammavariate(self.alpha, self.beta)


class GeometricDistribution(ProbDistribution):
    def __init__(self, probability: float) -> None:
        super().__init__(DistributionType.GEOMETRIC)
        # PLAN Value Check Input
        self.probability: float = probability

    def distributionFunction(self, RanNumGenerator) -> float:
        return RanNumGenerator.geometric(self.probability)


class LognormalDistribution(ProbDistribution):
    def __init__(self, logmean: float, logsd: float) -> None:
        super().__init__(DistributionType.LOGNORMAL)
        # PLAN Value Check Input
        self.logmean: float = logmean
        self.logsd: float = logsd

    def distributionFunction(self, RanNumGenerator) -> float:
        return RanNumGenerator.lognormvariate(self.logmean, self.logsd)


class WeibullDistribution(ProbDistribution):
    def __init__(self, scale: float, shape: float) -> None:
        super().__init__(DistributionType.WEIBULL)
        # PLAN Value Check Input
        self.scale: float = scale
        self.shape: float = shape

    def distributionFunction(self, RanNumGenerator) -> float:
        return RanNumGenerator.weibullvariate(self.scale, self.shape)


class CauchyDistribution(ProbDistribution):
    def __init__(self, location: float, scale: float) -> None:
        super().__init__(DistributionType.CAUCHY)
        # PLAN Value Check Input
        self.location: float = location
        self.scale: float = scale

    def distributionFunction(self, RanNumGenerator) -> float:
        while 1:
            p = 0.0
            while p == 0.0:
                p: float = RanNumGenerator.random()
            number = self.location + self.scale * math.tan(math.pi * (p - 0.5))
            if number > 0:
                return number
        return 0.0


class TriangularDistribution(ProbDistribution):
    def __init__(self, min: float, mean: float, max: float) -> None:
        super().__init__(DistributionType.TRIANGULAR)
        # PLAN Value Check Input
        self.min: float = min
        self.mean: float = mean
        self.max: float = max

    def distributionFunction(self, RanNumGenerator) -> float:
        return RanNumGenerator.triangular(left=self.min, right=self.mean, mode=self.max)
