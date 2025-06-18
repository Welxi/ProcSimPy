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
