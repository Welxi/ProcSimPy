import pytest


def test_single_server() -> None:
    from SingleServer import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 0.4999 < results['working_ratio'] < 0.5001


def test_parallel_machines_1() -> None:
    from ParallelMachines1 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 0.2309 < results['working_ratio_M1'] < 0.231
    assert 0.269 < results['working_ratio_M2'] < 0.2691


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_2() -> None:
    from ParallelMachines2 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 0.4618 < results['working_ratio_M1'] < 0.4619
    assert 0.0381 < results['working_ratio_M2'] < 0.0382


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_3() -> None:
    from ParallelMachines3 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 0.4618 < results['working_ratio_M1'] < 0.4619
    assert 0.0381 < results['working_ratio_M2'] < 0.0382


@pytest.mark.skip('Not Implemented')
def test_parallel_machines_4() -> None:
    from ParallelMachines4 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 0.4618 < results['working_ratio_M1'] < 0.4619
    assert 0.0381 < results['working_ratio_M2'] < 0.0382
    assert results['NumM1'] == 2660
    assert results['NumM2'] == 220


@pytest.mark.skip('Not Implemented')
def test_setting_WIP_1():
    from SettingWIP1 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 1
    assert results['simulationTime'] == 0.25
    assert results['working_ratio_M1'] == 100


@pytest.mark.skip('Not Implemented')
def test_setting_WIP_2():
    from SettingWIP2 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert results['simulationTime'] == 0.50
    assert results['working_ratio_M1'] == 100


@pytest.mark.skip('Not Implemented')
def test_setting_WIP_3():
    from SettingWIP3 import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2
    assert results['simulationTime'] == 0.35
    assert results['working_ratio_M1'] == 100
