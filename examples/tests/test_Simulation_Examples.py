import pytest

# TODO Turn into package and do these tests from build


def test_single_server() -> None:
    from SingleServer import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_ratio'] < 50.01


def test_parallel_machines_1() -> None:
    from ParallelMachines import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 23.09 < results['working_ratio_M1'] < 23.10
    assert 26.90 < results['working_ratio_M2'] < 26.91
    # TODO these stats were for longest machine waiting scheduling rules


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_2() -> None:
    from ParallelMachinesSelectM1 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_ratio_M1'] < 46.19
    assert 3.81 < results['working_ratio_M2'] < 3.82


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_3() -> None:
    from ParallelMachinesPriority import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_ratio_M1'] < 46.19
    assert 3.81 < results['working_ratio_M2'] < 3.82


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_4() -> None:
    from ParallelMachinesExitCount import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_ratio_M1'] < 46.19
    assert 3.81 < results['working_ratio_M2'] < 3.82
    assert results['NumM1'] == 2660
    assert results['NumM2'] == 220


def test_setting_WIP_1() -> None:
    from SettingWIP1Part import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 1
    assert results['simulationTime'] == 0.25
    assert results['working_ratio'] == 100


def test_setting_WIP_2() -> None:
    from SettingWIP2Parts import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert results['simulationTime'] == 0.50
    assert results['working_ratio'] == 100


def test_setting_WIP_3() -> None:
    from SettingWIPRemainingPT import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert results['simulationTime'] == 0.35
    assert results['working_ratio'] == 100


@pytest.mark.skip('Not Implemented')
def testServerWithShift1(self) -> None:
    from MachineWithShift1 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 3
    assert 49.99 < results['working_ratio'] < 50.01


@pytest.mark.skip('Not Implemented')
def testServerWithShift2(self) -> None:
    from MachineWithShift2 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 16
    assert 49.99 < results['working_ratio'] < 50.01


@pytest.mark.skip('Not Implemented')
def testServerWithShift3(self) -> None:
    from MachineWithShift3 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 4
    assert 59.99 < results['working_ratio'] < 60.01


@pytest.mark.skip('Not Implemented')
def testServerWithShift4(self) -> None:
    from MachineWithShift4 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert 29.99 < results['working_ratio'] < 30.01


@pytest.mark.skip('Not Implemented')
def testTwoServers(self) -> None:
    from MachinesInSeriesFixed import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 732
    assert 78.17 < results['blockage_ratio'] < 78.18
    assert 26.73 < results['working_ratio'] < 27.74
