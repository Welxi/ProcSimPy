import pytest

from hepyaestus.Entity import Entity
from hepyaestus.printTrace import printTrace


@pytest.fixture
def entity() -> Entity:
    return Entity('TE', 'TestEntity')


@pytest.fixture
def eventTime() -> float:
    return float(1)


@pytest.fixture
def timecode(entity, eventTime) -> str:
    return f'ID:{entity.id:>3} @T:{eventTime:>4} ->'


def test_printTrace_invalidArg(entity, eventTime) -> None:
    with pytest.raises(ValueError, match=f'Unsupported phrase asdf for {entity.id}'):
        printTrace(entity=entity, eventTime=eventTime, asdf='')


def test_printTrace_TooManArgs(entity, eventTime) -> None:
    with pytest.raises(
        AssertionError, match='Only pne phrase per printTrace supported'
    ):
        printTrace(entity=entity, eventTime=eventTime, create='', signal='')


def test_printTrace_create(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, create=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} created an entity: {entity.id}\n'


def test_printTrace_signal(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, signal=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} signalling: TE\n'


def test_printTrace_signalGiver(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, signalGiver=entity.id)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f'{timecode} _______________________signalling giver: {entity.id}\n'
    )


def test_printTrace_signalReceiver(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, signalReceiver=entity.id)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f'{timecode} ____________________signalling receiver: {entity.id}\n'
    )


def test_printTrace_attemptSignal(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, attemptSignal=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} will try to signal: {entity.id}\n'


def test_printTrace_attemptSignalGiver(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, attemptSignalGiver=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} will try to signal a giver: {entity.id}\n'


def test_printTrace_attemptSignalReceiver(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, attemptSignalReceiver=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} will try to signal a receiver: {entity.id}\n'


def test_printTrace_preempt(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, preempt=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} preempts: {entity.id}.\n'


def test_printTrace_preempted(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, preempted=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} is being preempted: {entity.id}.\n'


def test_printTrace_startWork(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, startWork=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} started working in: {entity.id}\n'


def test_printTrace_finishWork(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, finishWork=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} finished working in: {entity.id}\n'


def test_printTrace_processEnd(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, processEnd=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} ended processing in: {entity.id}\n'


# def test_printTrace_interrupted(entity, eventTime, timecode, capsys) -> None:
#     printTrace(entity=entity, eventTime=eventTime, interrupted=entity.id)
#     captured = capsys.readouterr()
#     assert captured.out == f'{timecode} interrupted at: {entity.id} .\n'


def test_printTrace_enter(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, enter=entity.id)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f'{timecode} got into: {entity.id} =========================================>{entity.id}\n'
    )


def test_printTrace_destroy(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, destroy=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} destroyed at: {entity.id} * \n'


def test_printTrace_waitEvent(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, waitEvent=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} will wait for event: {entity.id}\n'


def test_printTrace_received(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, received=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} received event: {entity.id}\n'


def test_printTrace_isRequested(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, isRequested=entity.id)
    captured = capsys.readouterr()
    assert (
        captured.out == f'{timecode} received an isRequested event from: {entity.id}\n'
    )


def test_printTrace_canDispose(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, canDispose=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} received an canDispose event: {entity.id}\n'


def test_printTrace_interruptionEnd(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, interruptionEnd=entity.id)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f'{timecode} received an interruptionEnd event at: {entity.id}\n'
    )


def test_printTrace_loadOperatorAvailable(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, loadOperatorAvailable=entity.id)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f'{timecode} received a loadOperatorAvailable event at: {entity.id}\n'
    )


def test_printTrace_resourceAvailable(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, resourceAvailable=entity.id)
    captured = capsys.readouterr()
    assert (
        captured.out == f'{timecode} received a resourceAvailable event: {entity.id}\n'
    )


def test_printTrace_entityRemoved(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, entityRemoved=entity.id)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f'{timecode} received an entityRemoved event from: {entity.id}\n'
    )


def test_printTrace_conveyerEnd(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, conveyerEnd=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} has reached conveyer End: {entity.id}.!\n'


def test_printTrace_conveyerFull(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, conveyerFull=entity.id)
    out, err = capsys.readouterr()
    assert out == f'{timecode} is now Full, No of units: TE(*)\n'


def test_printTrace_moveEnd(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, moveEnd=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} received a moveEnd event: {entity.id}\n'


def test_printTrace_eventsToCome(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, eventsToCome=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} there are MORE events for now: {entity.id}\n'


def test_printTrace_noEventsToCome(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, noEventsToCome=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} there are NO more events for now: {entity.id}\n'


def test_printTrace_lineBreak(entity, eventTime, timecode, capsys) -> None:
    printTrace(entity=entity, eventTime=eventTime, lineBreak=entity.id)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} : {entity.id}\n'
