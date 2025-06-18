from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from itertools import count
from typing import TYPE_CHECKING

from procsimpy.Failure import Failure

if TYPE_CHECKING:
    from procsimpy.Base import Base
    from procsimpy.Entity import Entity
    from procsimpy.Node import Node
    from simpy.core import SimTime

"""The Events used here are for the purpose of logging
and tracing results of the experiment
"""


# could create a can Trace call for this to see if
#  experiment wants a given type of event logged
@dataclass(frozen=True, kw_only=True)
class EventData(ABC):
    """
    Base Data used for specific events
    """

    time: SimTime
    caller: Base
    # transmission: Optional[Entity] = None
    # trace: bool = True
    # attempt: int = 0
    id: int = field(default_factory=count().__next__, init=False)

    @abstractmethod
    def phrase(self) -> str:
        pass


@dataclass(frozen=True, kw_only=True)
class CreateEvent(EventData):
    """
    An Entity has been created
    """

    def phrase(self) -> str:
        return f'Entity Created => {self.caller.name}'


@dataclass(frozen=True, kw_only=True)
class InitEvent(EventData):
    """
    A Node has been Initialized
    """

    def phrase(self) -> str:
        return f'Object Initialized => {self.caller.name}'


@dataclass(frozen=True, kw_only=True)
class EnterEvent(EventData):
    """
    An Entity has Entered a Node
    """

    station: Node

    def phrase(self) -> str:
        return f'{self.caller.name} entered {self.station.name}'


@dataclass(frozen=True, kw_only=True)
class ReceiveEvent(EventData):
    """
    A Node has Received an Entity
    """

    entity: Entity

    def phrase(self) -> str:
        # could add where it was received from
        return f'{self.caller.name} received {self.entity.name}'


@dataclass(frozen=True, kw_only=True)
class GiveEvent(EventData):
    """
    A Node has Given an Entity
    """

    def phrase(self) -> str:
        # could add where it was given too
        return f'{self.caller.name} gave Entity'


@dataclass(frozen=True, kw_only=True)
class StartWorkEvent(EventData):
    """
    A Node has begun its processing of an Entity
    """

    def phrase(self) -> str:
        return f'{self.caller.name} Started Work on {self.caller.name}'


@dataclass(frozen=True, kw_only=True)
class FinishWorkEvent(EventData):
    """
    A Node has finished its processing of an Entity
    """

    def phrase(self) -> str:
        return f'{self.caller.name} Finished Work on {self.caller.name}'


@dataclass(frozen=True, kw_only=True)
class InterruptEvent(EventData):
    """
    A Nodes Work has been Interrupted
    """

    cause: Failure

    def phrase(self) -> str:
        return f'{self.caller.name} interrupted by {self.cause.name}'


# This just might never be used without event architecture
@dataclass(frozen=True, kw_only=True)
class InterruptEndEvent(EventData):
    """
    A Nodes Interruption has been resolved
    """

    def phrase(self) -> str:
        return f'{self.caller.name} interruption ended on {self.caller.name}'


# This might not be nessary for work to begin but would be useful for logging
@dataclass(frozen=True, kw_only=True)
class WIPEvent(EventData):
    """
    The experiment starts with a node with work to begin
    """

    def phrase(self) -> str:
        return f'{self.caller.name} has Work in Progress'


# Possible Future Events
# preempt
# preempted
# destroy
# ResourceAvailable
# OperatorAvailable
