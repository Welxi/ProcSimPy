from procsimpy.ProbDistribution import FixedDistribution, GaussianDistribution
from procsimpy.RandomNumberGenerator import RandomNumberGenerator


def test_RandomNumberGenerator_Fixed() -> None:
    rng = RandomNumberGenerator(FixedDistribution(mean=1))
    number = rng.generateNumber()
    assert number == 1


def test_RandomNumberGenerator_Normal() -> None:
    dist = GaussianDistribution(mean=1, stdev=0.1, min=0.5, max=1.5)
    rng = RandomNumberGenerator(dist)
    number = rng.generateNumber()
    assert 0.5 < number < 1.5
