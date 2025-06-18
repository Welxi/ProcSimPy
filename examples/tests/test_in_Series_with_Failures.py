import pytest


@pytest.mark.skip('Not Implemented')
def test_Series_Fixed_with_Failures() -> None:
    from examples.MachinesInSeriesFixedWF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 732
    assert 78.17 < results['blockage_ratio'] < 78.18
    # assert 26.73 < results['working_percent'] < 27.74
    # TODO Stats for Repair Tech


@pytest.mark.skip('No Test Data For')
def test_Series_Stochastic_with_Failures() -> None:
    from examples.MachinesInSeriesStochasticWF import main

    results = main(test=True, maxSimTime=1440)

    assert results is not None
