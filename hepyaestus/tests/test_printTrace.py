import pytest

from hepyaestus.baseClasses import BaseObject
from hepyaestus.printTrace import printTrace


@pytest.fixture
def context() -> BaseObject:
    return BaseObject('TE', 'TestEntity')


@pytest.fixture
def base() -> BaseObject:
    return BaseObject('SO', 'SimObject')


@pytest.fixture
def eventTime() -> float:
    return float(1)


@pytest.fixture
def timecode(base, eventTime) -> str:
    return f'ID:{base.id:>3} @T:{eventTime:4} ->'


def test_printTrace_invalidArg(base, eventTime) -> None:
    with pytest.raises(ValueError, match=f'Unsupported phrase asdf for {base.id}'):
        printTrace(base=base, eventTime=eventTime, asdf='')


def test_printTrace_TooManArgs(base, eventTime) -> None:
    with pytest.raises(
        AssertionError, match='Only pne phrase per printTrace supported'
    ):
        printTrace(base=base, eventTime=eventTime, create='', signal='')


def test_printTrace_init(base, eventTime, timecode, capsys) -> None:
    printTrace(base=base, eventTime=eventTime, init=base)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} Object Initialized => {base.id}\n'


def test_printTrace_create(base, eventTime, timecode, capsys) -> None:
    printTrace(base=base, eventTime=eventTime, create=base)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} Entity Created => {base.id}\n'


def test_printTrace_startWork(base, eventTime, timecode, capsys) -> None:
    printTrace(base=base, eventTime=eventTime, startWork=base)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.id} started work\n'


def test_printTrace_finishWork(base, eventTime, timecode, capsys) -> None:
    printTrace(base=base, eventTime=eventTime, finishWork=base)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.id} finished work\n'


def test_printTrace_interrupted(base, eventTime, timecode, capsys, context) -> None:
    printTrace(base=base, eventTime=eventTime, interrupted=context)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.id} interrupted by {context.id}\n'


def test_printTrace_interruptionEnd(base, eventTime, timecode, capsys, context) -> None:
    printTrace(base=base, eventTime=eventTime, interruptEnd=context)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {context.id} interruption ended on {base.id}\n'


def test_printTrace_enter(base, eventTime, timecode, capsys, context) -> None:
    printTrace(base=base, eventTime=eventTime, enter=context)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {context.id} entered {base.id}\n'


def test_printTrace_received(base, eventTime, timecode, capsys, context) -> None:
    printTrace(base=base, eventTime=eventTime, received=context)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.id} received {context.id}\n'


def test_printTrace_gave(base, eventTime, timecode, capsys, context) -> None:
    printTrace(base=base, eventTime=eventTime, gave=context)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {base.id} gave {context.id}\n'


def test_printTrace_isRequested(base, eventTime, timecode, capsys, context) -> None:
    printTrace(base=base, eventTime=eventTime, isRequested=context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f'{timecode} {base.id} received an isRequested event for {context.id}\n'
    )


def test_printTrace_canDispose(base, eventTime, timecode, capsys, context) -> None:
    printTrace(base=base, eventTime=eventTime, canDispose=context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f'{timecode} {base.id} received a canDispose event for {context.id}\n'
    )


# def test_printTrace_signal(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, signal=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} signalling: TE\n'


# def test_printTrace_signalGiver(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, signalGiver=simObject.id)
#     captured = capsys.readouterr()
#     assert (
#         captured.out
#         == f'{timecode} _______________________signalling giver: {simObject.id}\n'
#     )


# def test_printTrace_signalReceiver(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, signalReceiver=simObject.id)
#     captured = capsys.readouterr()
#     assert (
#         captured.out
#         == f'{timecode} ____________________signalling receiver: {simObject.id}\n'
#     )


# def test_printTrace_attemptSignal(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, attemptSignal=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} will try to signal: {simObject.id}\n'


# def test_printTrace_attemptSignalGiver(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, attemptSignalGiver=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} will try to signal a giver: {simObject.id}\n'


# def test_printTrace_attemptSignalReceiver(
#     simObject, eventTime, timecode, capsys
# ) -> None:
#     printTrace(base=simObject, eventTime=eventTime, attemptSignalReceiver=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} will try to signal a receiver: {simObject.id}\n'


# def test_printTrace_preempt(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, preempt=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} preempts: {simObject.id}.\n'


# def test_printTrace_preempted(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, preempted=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} is being preempted: {simObject.id}.\n'

# def test_printTrace_processEnd(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, processEnd=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} ended processing in: {simObject.id}\n'

# def test_printTrace_destroy(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, destroy=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} destroyed at: {simObject.id} * \n'


# def test_printTrace_waitEvent(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, waitEvent=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} will wait for event: {simObject.id}\n'

# def test_printTrace_loadOperatorAvailable(
#     simObject, eventTime, timecode, capsys
# ) -> None:
#     printTrace(base=simObject, eventTime=eventTime, loadOperatorAvailable=simObject.id)
#     captured = capsys.readouterr()
#     assert (
#         captured.out
#         == f'{timecode} received a loadOperatorAvailable event at: {simObject.id}\n'
#     )


# def test_printTrace_resourceAvailable(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, resourceAvailable=simObject.id)
#     captured = capsys.readouterr()
#     assert (
#         captured.out
#         == f'{timecode} received a resourceAvailable event: {simObject.id}\n'
#     )


# def test_printTrace_entityRemoved(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, entityRemoved=simObject.id)
#     captured = capsys.readouterr()
#     assert (
#         captured.out
#         == f'{timecode} received an entityRemoved event from: {simObject.id}\n'
#     )


# def test_printTrace_conveyerEnd(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, conveyerEnd=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} has reached conveyer End: {simObject.id}.!\n'


# def test_printTrace_conveyerFull(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, conveyerFull=simObject.id)
#     out, err = capsys.readouterr()
#     assert out == f'{timecode} is now Full, No of units: TE(*)\n'


# def test_printTrace_moveEnd(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, moveEnd=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} received a moveEnd event: {simObject.id}\n'


# def test_printTrace_eventsToCome(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, eventsToCome=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} there are MORE events for now: {simObject.id}\n'


# def test_printTrace_noEventsToCome(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, noEventsToCome=simObject.id)
#     captured = capsys.readouterr()
#     assert (
#         captured.out == f'{timecode} there are NO more events for now: {simObject.id}\n'
#     )


# def test_printTrace_lineBreak(simObject, eventTime, timecode, capsys) -> None:
#     printTrace(base=simObject, eventTime=eventTime, lineBreak=simObject.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} : {simObject.id}\n'
