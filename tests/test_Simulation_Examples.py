def test_single_server():
    from singleServer import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2880
    assert 49.99 < results['working_ratio'] < 50.01


def test_parallel_server():
    from ParallelMachines import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2880
    assert 23.09 < results['working_ratio_M1'] < 23.1
    assert 26.9 < results['working_ratio_M2'] < 26.91
