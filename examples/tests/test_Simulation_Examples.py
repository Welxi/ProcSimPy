import pytest


def test_single_server() -> None:
    from examples.SingleServer import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_percent'] < 50.01


def test_parallel_machines_1() -> None:
    from examples.ParallelMachinesWF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 24.99 < results['working_percent_M1'] < 25.01
    assert 24.99 < results['working_percent_M2'] < 25.01


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_1_with_Failures() -> None:
    from examples.ParallelMachinesWF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 23.09 < results['working_percent_M1'] < 23.10
    assert 26.90 < results['working_percent_M2'] < 26.91


def test_parallel_machines_2() -> None:
    from examples.ParallelMachinesSelectM1 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_percent_M1'] < 50.01
    assert -00.01 < results['working_percent_M2'] < 00.01


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_2_with_Failures() -> None:
    from examples.ParallelMachinesSelectM1WF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_percent_M1'] < 46.19
    assert 3.81 < results['working_percent_M2'] < 3.82


def test_parallel_machines_3() -> None:
    from examples.ParallelMachinesPriorityWF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_percent_M1'] < 50.01
    assert -00.01 < results['working_percent_M2'] < 00.01


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_3_with_Failures() -> None:
    from examples.ParallelMachinesPriorityWF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_percent_M1'] < 46.19
    assert 3.81 < results['working_percent_M2'] < 3.82


def test_setting_WIP_1() -> None:
    from examples.SettingWIP1Part import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 1
    assert results['simulationTime'] == 0.25
    assert results['working_percent'] == 100


def test_setting_WIP_2() -> None:
    from examples.SettingWIP2Parts import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert results['simulationTime'] == 0.50
    assert results['working_percent'] == 100


def test_setting_WIP_3() -> None:
    from examples.SettingWIPRemainingPT import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert results['simulationTime'] == 0.35
    assert results['working_percent'] == 100


def testServerWithShift1() -> None:
    from examples.MachineWithShift1 import main

    results = main(test=True, maxSimTime=20)
    assert results is not None
    assert results['parts'] == 3
    assert 49.99 < results['working_percent'] < 50.01


def testServerWithShift2() -> None:
    from examples.MachineWithShift2 import main

    results = main(test=True, maxSimTime=100)
    assert results is not None
    assert results['parts'] == 16
    assert 49.99 < results['working_percent'] < 50.01


@pytest.mark.skip('Not Implemented')
def testServerWithShift3() -> None:
    from examples.MachineWithShift3 import main

    results = main(test=True, maxSimTime=20)
    assert results is not None
    assert results['parts'] == 4
    assert 59.99 < results['working_percent'] < 60.01


@pytest.mark.skip('Not Implemented')
def testServerWithShift4() -> None:
    from MachineWithShift4 import main

    results = main(test=True, maxSimTime=20)
    assert results is not None
    assert results['parts'] == 2
    assert 29.99 < results['working_percent'] < 30.01


@pytest.mark.skip('No Test Data For')
def test_Series_Fixed() -> None:
    from examples.MachinesInSeriesFixedWF import main

    results = main(test=True, maxSimTime=1440)


@pytest.mark.skip('Not Implemented')
def test_Series_Fixed_with_Failures() -> None:
    from examples.MachinesInSeriesFixedWF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 732
    assert 78.17 < results['blockage_ratio'] < 78.18
    assert 26.73 < results['working_percent'] < 27.74


@pytest.mark.skip('No Test Data For')
def test_Series_Stochastic() -> None:
    from examples.MachinesInSeriesFixedWF import main

    results = main(test=True, maxSimTime=1440)


@pytest.mark.skip('No Test Data For')
def test_Series_Stochastic_with_Failures() -> None:
    from examples.MachinesInSeriesFixedWF import main

    results = main(test=True, maxSimTime=1440)
