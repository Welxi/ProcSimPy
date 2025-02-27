import pytest


def test_single_server() -> None:
    from SingleServer import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_ratio'] < 50.01


def test_parallel_machines_1() -> None:
    from ParallelMachines1 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 23.09 < results['working_ratio_M1'] < 23.10
    assert 26.90 < results['working_ratio_M2'] < 26.91
    # TODO these stats were for longest machine waiting scheduling rules


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_2() -> None:
    from ParallelMachines2 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_ratio_M1'] < 46.19
    assert 3.81 < results['working_ratio_M2'] < 3.82


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_3() -> None:
    from ParallelMachines3 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_ratio_M1'] < 46.19
    assert 3.81 < results['working_ratio_M2'] < 3.82


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_4() -> None:
    from ParallelMachines4 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_ratio_M1'] < 46.19
    assert 3.81 < results['working_ratio_M2'] < 3.82
    assert results['NumM1'] == 2660
    assert results['NumM2'] == 220


def test_setting_WIP_1():
    from SettingWIP1 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 1
    assert results['simulationTime'] == 0.25
    assert results['working_ratio'] == 100


def test_setting_WIP_2():
    from SettingWIP2 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert results['simulationTime'] == 0.50
    assert results['working_ratio'] == 100


def test_setting_WIP_3():
    from SettingWIP3 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert results['simulationTime'] == 0.35
    assert results['working_ratio'] == 100
