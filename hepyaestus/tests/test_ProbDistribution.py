from random import Random

import pytest

from hepyaestus.ProbDistribution import (
    ExpDistribution,
    FixedDistribution,
    NormalDistribution,
)


@pytest.fixture
def rng() -> Random:
    SEED = 42
    return Random(SEED)


def test_Fixed(rng) -> None:
    dist = FixedDistribution(mean=1)
    number = dist.distributionFunction(rng)
    assert number == 1


def test_Normal(rng) -> None:
    dist = NormalDistribution(mean=1, stdev=0.1, min=0.5, max=1.5)
    number = dist.distributionFunction(rng)
    assert 0.5 < number < 1.5


def test_Normal_min_greater_than_max() -> None:
    with pytest.raises(ValueError, match='max must be greater than min'):
        NormalDistribution(mean=1, stdev=0.1, min=1.5, max=0.5)


def test_Exp(rng):
    dist = ExpDistribution(mean=1)
    number = dist.distributionFunction(rng)

    # Got to be a better test
    assert isinstance(number, float)
    assert number < float('inf')


def test_Exp_invalid_mean() -> None:
    with pytest.raises(ValueError, match='Mean cannot be less than or equal to 0'):
        ExpDistribution(mean=0)


# TODO Test GammaDistribution, LogisticDistribution, ErlangDistribution
# TODO Test GeometricDistribution, LognormalDistribution, WeibullDistribution
# TODO Test CauchyDistribution, TriangularDistribution
