from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hepyaestus import Line
    from hepyaestus.Entity import Entity
    from simpy import Environment

# In an Ideal future this module would subscribe to event notifications or
# process event stubs to generate statistics


class Statistics:
    def __init__(self, env: Environment, line: Line) -> None:
        self.env: Environment = env
        # TODO Can I trace

        self.totalWorkingTime: float = self.env.now
        self.timeLastOperationStarted: float = self.env.now
        self.timeLastOperationEnded: float = self.env.now
        self.totalWaitingTime: float = self.env.now
        self.totalBlockageTime: float = self.env.now

        self.totalOffShiftTime: float = self.env.now
        # self.totalOnBreakTime: float = self.env.now
        self.timeLastStartedShift: float = self.env.now
        self.timeLastEndedShift: float = self.env.now

        self.numberOfEntitiesEntered: int = 0
        self.timeLastEntityReceived: float = self.env.now
        self.numberOfEntitiesExited: int = 0
        self.timeLastEntityExited: float = self.env.now

        self.entries: list[Entity] = []
        self.exits: list[Entity] = []

    def createRatios(self, simTime: float) -> None:
        self.workingRatio = self.totalWorkingTime / simTime
        self.waitingRatio = self.totalWaitingTime / simTime
        self.blockageRatio = self.totalBlockageTime / simTime

        self.offShiftRatio = self.totalOffShiftTime / simTime

    def startingProcessing(self) -> None:
        # Starting Time must be after Ending Time
        assert self.env.now >= self.timeLastOperationEnded, 'Operation out of order'

        self.timeLastOperationStarted = self.env.now

    def finishedProcessing(self) -> None:
        # Ending Time must be after Starting Time
        # Zero Time Processing Not Supported
        assert self.env.now > self.timeLastOperationStarted, 'Operation out of order'

        self.timeLastOperationEnded = self.env.now
        self.totalWorkingTime += (
            self.timeLastOperationEnded - self.timeLastOperationStarted
        )

    def receivedEntity(self, entity: Entity) -> None:
        self.numberOfEntitiesEntered += 1
        self.entries.append(entity)
        self.timeLastEntityReceived = self.env.now

        # TODO check if machine was actually idle
        # ie what if it can process more than one at a time
        # do we still consider it time spent waiting as there was opportunity cost
        self.totalWaitingTime += (
            self.timeLastEntityReceived - self.timeLastOperationEnded
        )

    def givenEntity(self, entity: Entity) -> None:
        self.numberOfEntitiesExited += 1
        self.exits.append(entity)
        self.timeLastEntityExited = self.env.now

        self.totalBlockageTime += (
            self.timeLastOperationEnded - self.timeLastEntityExited
        )

    def wentOnShift(self) -> None:
        assert self.env.now >= self.timeLastEndedShift, 'Operation out of order'
        self.timeLastStartedShift = self.env.now
        self.totalOffShiftTime += self.timeLastStartedShift - self.timeLastEndedShift

    def wentOffShift(self) -> None:
        assert self.env.now > self.timeLastStartedShift, 'Operation out of order'
        self.timeLastEndedShift = self.env.now

    def toDict(self) -> dict[str, int | float]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if type(value) is int or type(value) is float
        }
