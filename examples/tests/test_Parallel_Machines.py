def test_parallel_machines_1() -> None:
    from examples.ParallelMachines import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 24.99 < results['working_percent_M1'] < 25.01
    assert 24.99 < results['working_percent_M2'] < 25.01


def test_parallel_machines_2() -> None:
    from examples.ParallelMachinesSelectM1 import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_percent_M1'] < 50.01
    assert -00.01 < results['working_percent_M2'] < 00.01


def test_parallel_machines_3() -> None:
    from examples.ParallelMachinesPriority import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_percent_M1'] < 50.01
    assert -00.01 < results['working_percent_M2'] < 00.01
