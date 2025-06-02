import pytest

from procsimpy.Base import Base
from procsimpy.EventData import EventData
from procsimpy.printTrace import printTrace


@pytest.fixture
def transmission() -> Base:
    return Base('TE', 'TestEntity')


@pytest.fixture
def base() -> Base:
    return Base('Base', 'SimBase')


@pytest.fixture
def caller() -> Base:
    return Base('Caller', 'SimCaller')


@pytest.fixture
def eventData(caller, transmission) -> EventData:
    return EventData(caller=caller, time=1, transmission=transmission)


@pytest.fixture
def timecode(eventData) -> str:
    return f'@T:{eventData.time:>4} ->'


@pytest.mark.skip('Not Implemented')
def test_printTrace_invalidArg(base, eventData) -> None:
    with pytest.raises(ValueError, match='Unsupported phrase asdf for printTrace'):
        printTrace(base=base, asdf=eventData)


@pytest.mark.skip('Not Implemented')
def test_printTrace_TooManArgs(base, eventData) -> None:
    with pytest.raises(
        AssertionError, match='Only one phrase per printTrace supported'
    ):
        printTrace(base=base, create=eventData, signal=eventData)


@pytest.mark.skip('Not Implemented')
def test_printTrace_keywords(
    base, eventData, timecode, caller, transmission, capsys
) -> None:
    printTrace(base=base, init=eventData)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} Object Initialized => {base.name}\n'

    printTrace(base=base, create=eventData)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} Entity Created => {base.name}\n'

    printTrace(base=base, startWork=eventData)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.name} started work\n'

    printTrace(base=base, finishWork=eventData)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.name} finished work\n'

    printTrace(base=base, interrupted=eventData)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.name} interrupted by {caller.name}\n'

    printTrace(base=base, interruptEnd=eventData)
    captured = capsys.readouterr()
    assert (
        captured.out == f'{timecode} {caller.name} interruption ended on {base.name}\n'
    )

    printTrace(base=base, enter=eventData)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.name} entered {caller.name}\n'

    printTrace(base=base, received=eventData)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.name} received {transmission.id}\n'

    printTrace(base=base, gave=eventData)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.name} gave {transmission.id}\n'


# def test_printTrace_isRequested(base, eventData, timecode, capsys, context) -> None:
#     printTrace(base=base, isRequested=eventData)
#     captured = capsys.readouterr()
#     assert (
#         captured.out
#         == f'{timecode} E:<isRequested> -> {base.name} received an isRequested event for {context.name}\n'
#     )


# def test_printTrace_canDispose(base, eventData, timecode, capsys, context) -> None:
#     printTrace(base=base, canDispose=eventData)
#     captured = capsys.readouterr()
#     assert (
#         captured.out
#         == f'{timecode} E:<canDispose> -> {base.name} called from {context.name}\n'
#     )
