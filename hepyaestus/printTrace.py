from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hepyaestus.baseClasses import BaseObject


def getSupportedPrintKwrds() -> tuple:
    return (
        'create',
        'signal',
        'signalGiver',
        'signalReceiver',
        'attemptSignal',
        'attemptSignalGiver',
        'attemptSignalReceiver',
        'preempt',
        'preempted',
        'startWork',
        'finishWork',
        'processEnd',
        'interrupted',
        'enter',
        'destroy',
        'waitEvent',
        'received',
        'isRequested',
        'canDispose',
        'interruptionEnd',
        'loadOperatorAvailable',
        'resourceAvailable',
        'entityRemoved',
        'conveyerEnd',
        'conveyerFull',
        'moveEnd',
        'eventsToCome',
        'noEventsToCome',
        'lineBreak',
    )


def getPhrase() -> dict:
    return {
        'create': {'phrase': 'created an entity'},
        'destroy': {'phrase': 'destroyed at', 'suffix': ' * '},
        'signal': {'phrase': 'signalling'},
        'signalGiver': {'phrase': 'signalling giver', 'prefix': '_'},
        'signalReceiver': {'phrase': 'signalling receiver', 'prefix': '_'},
        'attemptSignal': {'phrase': 'will try to signal'},
        'attemptSignalGiver': {'phrase': 'will try to signal a giver'},
        'attemptSignalReceiver': {'phrase': 'will try to signal a receiver'},
        'preempt': {'phrase': 'preempts', 'suffix': '.'},
        'preempted': {'phrase': 'is being preempted', 'suffix': '.'},
        'startWork': {'phrase': 'started working in'},
        'finishWork': {'phrase': 'finished working in'},
        'processEnd': {'phrase': 'ended processing in'},
        'interrupted': {'phrase': 'interrupted at', 'suffix': '.'},
        'enter': {'phrase': 'got into', 'suffix': '='},
        'waitEvent': {'phrase': 'will wait for event'},
        'received': {'phrase': 'received event'},
        'isRequested': {'phrase': 'received an isRequested event from'},
        'canDispose': {'phrase': 'received an canDispose event'},
        'interruptionEnd': {'phrase': 'received an interruptionEnd event at'},
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
        'lineBreak': {'phrase': ''},
    }


def printTrace(entity: BaseObject, eventTime: float, **kw) -> None:
    assert len(kw) == 1, 'Only pne phrase per printTrace supported'
    charLimit = 60  # could get this from line defaults
    timecode = f'ID:{entity.id:>3} @T:{eventTime:>4} ->'
    charLimit -= len(timecode)
    for key, value in kw.items():
        if key not in getSupportedPrintKwrds():
            raise ValueError(f'Unsupported phrase {key} for {entity.id}')

        element = getPhrase()[key]
        phrase = element['phrase']
        prefix = element.get('prefix', None)
        suffix = element.get('suffix', None)
        if key == 'linebreak':
            print(f'{timecode} {phrase:{value}>{charLimit}}')

        info = f'{phrase}: {value}' if value != '' else phrase
        if prefix is not None:
            # print(f"{timecode}  {info:{prefix}>{charLimit}}")
            print(f'{timecode} {info:{prefix}>{charLimit}}')
        elif suffix is not None:
            if key == 'enter':
                print(f'{timecode} {info} {">":{suffix}>{charLimit - 1}}{entity.id}')
            else:
                print(f'{timecode} {info}{suffix}')
        else:
            print(f'{timecode} {info}')  # could format too
