def testServerWithShift1() -> None:
    from examples.MachineWithShift1 import main

    results = main(test=True, maxSimTime=20)
    assert results is not None
    assert results['parts'] == 3
    assert 49.99 < results['working_percent'] < 50.01


def testServerWithShift2() -> None:
    from examples.MachineWithShift2 import main

    results = main(test=True, maxSimTime=20)
    assert results is not None
    assert results['parts'] == 3
    assert 49.99 < results['working_percent'] < 50.01


# @pytest.mark.skip('Not Implemented')
def testServerWithShift3() -> None:
    from examples.MachineWithShift3 import main

    results = main(test=True, maxSimTime=20)
    assert results is not None
    # assert results['parts'] == 4
    # assert 59.99 < results['working_percent'] < 60.01


# @pytest.mark.skip('Not Implemented')
def testServerWithShift4() -> None:
    from examples.MachineWithShift4 import main

    results = main(test=True, maxSimTime=20)
    assert results is not None
    # assert results['parts'] == 2
    # assert 29.99 < results['working_percent'] < 30.01
