from __future__ import annotations

from typing import TYPE_CHECKING

from procsimpy.EventData import EventData

if TYPE_CHECKING:
    from procsimpy.Base import BaseObject


def supportedKeywords() -> tuple:
    return (
        'init',
        'create',
        'startWork',
        'finishWork',
        'interrupted',
        'interruptEnd',
        'enter',
        'received',
        'gave',
        'isRequested',
        'canDispose',
        'initialWIP',
    )


def printTrace(base: BaseObject, **kw) -> None:
    assert len(kw) == 1, 'Only one phrase per printTrace supported'

    for key, eventData in kw.items():
        if key not in supportedKeywords():
            raise ValueError(f'Unsupported phrase {key} for printTrace')
        assert isinstance(eventData, EventData)
        if eventData.trace:
            consoleTrace(baseObject=base, eventData=eventData, key=key)


def consoleTrace(baseObject: BaseObject, eventData: EventData, key) -> None:
    caller = eventData.caller.name
    base = baseObject.name
    content = eventData.transmission.id if eventData.transmission else None
    # timecode = f'ID:{base:>3} @T:{eventData.time:>4}'
    timecode = f'@T:{eventData.time:>4}'
    # could format timecode based on maxSimTime
    phrases = {
        'init': f'Object Initialized => {base}',
        'create': f'Entity Created => {base}',
        'startWork': f'{base} started work',
        'finishWork': f'{base} finished work',
        'interrupted': f'{base} interrupted by {caller}',
        'interruptEnd': f'{caller} interruption ended on {base}',
        'enter': f'{base} entered {caller}',
        'received': f'{base} received {content}',
        'gave': f'{base} gave {content}',
        'isRequested': f'E:<isRequested> -> {base} called from {caller}, for {content}',
        'canDispose': f'E:<canDispose> -> {base} called from {caller}',
        'initialWIP': f'E:<initialWIP> -> {base} has Work in Progress',
    }
    print(f'{timecode} -> {phrases[key]}')


def oldKeywords() -> tuple:
    return (
        'signal',
        'signalGiver',
        'signalReceiver',
        'attemptSignal',
        'attemptSignalGiver',
        'attemptSignalReceiver',
        'preempt',
        'preempted',
        'processEnd',
        'destroy',
        'waitEvent',
        'loadOperatorAvailable',
        'resourceAvailable',
        'entityRemoved',
        'conveyerEnd',
        'conveyerFull',
        'moveEnd',
        'eventsToCome',
        'noEventsToCome',
    )


def getPhrase() -> dict:
    return {
        'destroy': {'phrase': 'destroyed at', 'suffix': ' * '},
        'signal': {'phrase': 'signalling'},
        'signalGiver': {'phrase': 'signalling giver', 'prefix': '_'},
        'signalReceiver': {'phrase': 'signalling receiver', 'prefix': '_'},
        'attemptSignal': {'phrase': 'will try to signal'},
        'attemptSignalGiver': {'phrase': 'will try to signal a giver'},
        'attemptSignalReceiver': {'phrase': 'will try to signal a receiver'},
        'preempt': {'phrase': 'preempts', 'suffix': '.'},
        'preempted': {'phrase': 'is being preempted', 'suffix': '.'},
        'processEnd': {'phrase': 'ended processing in'},
        'waitEvent': {'phrase': 'will wait for event'},
        'loadOperatorAvailable': {
            'phrase': 'received a loadOperatorAvailable event at'
        },
        'resourceAvailable': {'phrase': 'received a resourceAvailable event'},
        'entityRemoved': {'phrase': 'received an entityRemoved event from'},
        'moveEnd': {'phrase': 'received a moveEnd event'},
        'conveyerEnd': {'phrase': 'has reached conveyer End', 'suffix': '.!'},
        'conveyerFull': {'phrase': 'is now Full, No of units', 'suffix': '(*)'},
        'eventsToCome': {'phrase': 'there are MORE events for now'},
        'noEventsToCome': {'phrase': 'there are NO more events for now'},
    }
