def test_single_server():
    from singleServer import main

    results = main(test=True)
    assert results is not None
    assert results['parts'] == 2880
    # assert 49.99 < results['working_ratio'] < 50.01
