from __future__ import annotations

from typing import TYPE_CHECKING

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


def consoleTrace(base: BaseObject, eventTime: float, key, context) -> None:
    timecode = f'ID:{base.id:>3} @T:{eventTime:>4} ->'
    phrases = {
        'init': f'{timecode} Object Initialized => {base.id}',
        'create': f'{timecode} Entity Created => {base.id}',
        'startWork': f'{timecode} {base.id} started work',
        'finishWork': f'{timecode} {base.id} finished work',
        'interrupted': f'{timecode} {base.id} interrupted by {context.id}',
        'interruptEnd': f'{timecode} {context.id} interruption ended on {base.id}',
        'enter': f'{timecode} {context.id} entered {base.id}',
        'received': f'{timecode} {base.id} received {context.id}',
        'gave': f'{timecode} {base.id} gave {context.id}',
        'isRequested': f'{timecode} {base.id} received an isRequested event for {context.id}',
        'canDispose': f'{timecode} {base.id} received a canDispose event for {context.id}',
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


def printTrace(base: BaseObject, eventTime: float, **kw) -> None:
    assert len(kw) == 1, 'Only pne phrase per printTrace supported'

    for key, context in kw.items():
        if key not in supportedKeywords():
            raise ValueError(f'Unsupported phrase {key} for {base.id}')
        consoleTrace(base=base, eventTime=eventTime, key=key, context=context)
