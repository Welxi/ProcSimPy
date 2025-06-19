import pytest


def test_single_server() -> None:
    from examples.SingleServer import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_percent'] < 50.01


# @pytest.mark.skip('No Test Data For')
def test_Series_Fixed() -> None:
    from examples.MachinesInSeriesFixed import main

    results = main(test=True, maxSimTime=1440)

    #! Data for this test not confirmed by separate Simulation Tools
    assert results is not None
    assert results['parts'] == 959
    assert 16.73 < results['working_percent_M1'] < 27.51
    assert 99.89 < results['working_percent_M2'] < 99.91


# Is a long test should performance test with and without rng
@pytest.mark.skip('No Test Data For')
def test_Series_Stochastic() -> None:
    from examples.MachinesInSeriesStochastic import main

    results = main(test=True, maxSimTime=1440)

    assert results is not None
