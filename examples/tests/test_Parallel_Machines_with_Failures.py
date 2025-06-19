def test_parallel_machines_1_with_Failures() -> None:
    from examples.ParallelMachinesWF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 23.09 < results['working_percent_M1'] < 23.10
    assert 26.90 < results['working_percent_M2'] < 26.91


def test_parallel_machines_2_with_Failures() -> None:
    from examples.ParallelMachinesSelectM1WF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_percent_M1'] < 46.19
    assert 3.81 < results['working_percent_M2'] < 3.82


def test_parallel_machines_3_with_Failures() -> None:
    from examples.ParallelMachinesPriorityWF import main

    results = main(test=True, maxSimTime=1440)
    assert results is not None
    assert results['parts'] == 2880
    assert 46.18 < results['working_percent_M1'] < 46.19
    assert 3.81 < results['working_percent_M2'] < 3.82
