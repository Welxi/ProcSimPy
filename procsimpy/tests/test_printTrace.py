import pytest

from procsimpy.Base import Base
from procsimpy.Entity import Entity
from procsimpy.EventData import (
    CreateEvent,
    EnterEvent,
    GiveEvent,
    InitEvent,
    ReceiveEvent,
)
from procsimpy.Node import Node
from procsimpy.printTrace import printTrace


@pytest.fixture
def transmission() -> Base:
    return Entity('TE', 'TestEntity')


@pytest.fixture
def base() -> Base:
    return Node('Base', 'SimBase')


@pytest.fixture
def caller() -> Base:
    return Base('Caller', 'SimCaller')


@pytest.fixture
def time() -> float:
    return 1.5


@pytest.fixture
def timecode(time) -> str:
    return f'@T:{time:>4.2f} ->'


def test_CreateEvent(time, caller, timecode, capsys):
    event = CreateEvent(time=time, caller=caller)
    printTrace(event)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} Entity Created => {caller.name}\n'


def test_InitEvent(time, caller, timecode, capsys):
    event = InitEvent(time=time, caller=caller)
    printTrace(event)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} Object Initialized => {caller.name}\n'


def test_EnterEvent(time, caller, transmission, timecode, capsys):
    event = EnterEvent(time=time, caller=transmission, station=caller)
    printTrace(event)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {transmission.name} entered {caller.name}\n'


def test_ReceiveEvent(time, caller, transmission, timecode, capsys):
    event = ReceiveEvent(time=time, caller=caller, entity=transmission)
    printTrace(event)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {caller.name} received {transmission.name}\n'


def test_GiveEvent(time, caller, timecode, capsys):
    event = GiveEvent(time=time, caller=caller)
    printTrace(event)
    captured = capsys.readouterr()
    assert captured.out == f'{timecode} {caller.name} gave Entity\n'
