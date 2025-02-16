from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.EventData import EventData

if TYPE_CHECKING:
    from hepyaestus.baseClasses import BaseObject


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
    )


def printTrace(base: BaseObject, **kw) -> None:
    assert len(kw) == 1, 'Only pne phrase per printTrace supported'

    for key, eventData in kw.items():
        if key not in supportedKeywords():
            raise ValueError(f'Unsupported phrase {key} for {base.id}')
        assert isinstance(eventData, EventData)
        if eventData.trace:
            consoleTrace(baseObject=base, eventData=eventData, key=key)


def consoleTrace(baseObject: BaseObject, eventData: EventData, key) -> None:
    ctx = eventData.caller.id
    base = baseObject.id
    timecode = f'ID:{base:>3} @T:{eventData.time:>4} ->'
    phrases = {
        'init': f'{timecode} Object Initialized => {base}',
        'create': f'{timecode} Entity Created => {base}',
        'startWork': f'{timecode} {base} started work',
        'finishWork': f'{timecode} {base} finished work',
        'interrupted': f'{timecode} {base} interrupted by {ctx}',
        'interruptEnd': f'{timecode} {ctx} interruption ended on {base}',
        'enter': f'{timecode} {ctx} entered {base}',
        'received': f'{timecode} {base} received {ctx}',
        'gave': f'{timecode} {base} gave {ctx}',
        'isRequested': f'{timecode} {base} received an isRequested event for {ctx}',
        'canDispose': f'{timecode} {base} received a canDispose event for {ctx}',
    }
    print(phrases[key])


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
