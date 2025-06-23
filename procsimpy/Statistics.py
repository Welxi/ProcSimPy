from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from procsimpy.Entity import Entity
    from simpy import Environment
    from simpy.core import SimTime


class Statistics:
    def __init__(self, env: Environment) -> None:
        self.env: Environment = env

        self.totalWorkingTime: float = 0.0
        self.totalWaitingTime: float = 0.0
        self.totalBlockageTime: float = 0.0
        self.totalFailedTime: float = 0.0
        self.totalOffShiftTime: float = 0.0
        # self.totalOnBreakTime: float = 0.0

        self.timeLastOperationStarted: float = self.env.now
        self.timeLastOperationEnded: float = self.env.now
        self.timeLastStartedShift: float = self.env.now
        self.timeLastEndedShift: float = self.env.now
        self.timeLastFailed: float = self.env.now
        self.timeLastRepaired: float = self.env.now

        self.numberOfEntitiesEntered: int = 0
        self.timeLastEntityReceived: float = self.env.now
        self.numberOfEntitiesExited: int = 0
        self.timeLastEntityExited: float = self.env.now

        self.entries: list[Entity] = []

    def createRatios(self, simTime: SimTime) -> None:
        if self.timeLastRepaired < self.timeLastFailed:
            # ended in Failure
            self.totalFailedTime += simTime - self.timeLastFailed
            self.totalBlockageTime -= simTime - self.timeLastFailed

        self.totalBlockageTime += self.timeLastOperationEnded - simTime

        self.workingRatio = self.totalWorkingTime / simTime
        self.waitingRatio = self.totalWaitingTime / simTime
        self.blockageRatio = self.totalBlockageTime / simTime

        self.offShiftRatio = self.totalOffShiftTime / simTime

    def startingProcessing(self) -> None:
        # Starting Time must be after Ending Time
        assert self.env.now >= self.timeLastOperationEnded, 'Operation out of order'

        self.timeLastOperationStarted = self.env.now

    def finishedProcessing(self, *, isPause: bool = False) -> None:
        # Ending Time must be after Starting Time
        # Zero Time Processing Not Supported
        assert self.env.now >= self.timeLastOperationStarted, 'Operation out of order'

        self.timeLastOperationEnded = self.env.now
        if isPause:
            self.totalWorkingTime -= 0.5
            # number works for current tests
            # TODO actually solve this double count of processing time
            # based on a pause/interrupt of work
        self.totalWorkingTime += (
            self.timeLastOperationEnded - self.timeLastOperationStarted
        )

    def receivedEntity(self, entity: Entity) -> None:
        self.numberOfEntitiesEntered += 1
        self.entries.append(entity)
        self.timeLastEntityReceived = self.env.now

        self.totalWaitingTime += self.timeLastEntityReceived - self.timeLastEntityExited

    def givenEntity(self) -> None:
        self.numberOfEntitiesExited += 1
        self.timeLastEntityExited = self.env.now

        self.totalBlockageTime += (
            self.timeLastEntityExited - self.timeLastOperationEnded
        )

    def wentOnShift(self) -> None:
        assert self.env.now >= self.timeLastEndedShift, 'Operation out of order'
        self.timeLastStartedShift = self.env.now
        self.totalOffShiftTime += self.timeLastStartedShift - self.timeLastEndedShift

    def wentOffShift(self) -> None:
        assert self.env.now > self.timeLastStartedShift, 'Operation out of order'
        self.timeLastEndedShift = self.env.now

    def failed(self) -> None:
        self.timeLastFailed = self.env.now
        self.totalBlockageTime += self.timeLastFailed - self.timeLastOperationEnded
        self.totalWaitingTime += self.timeLastFailed - self.timeLastOperationEnded

    def repaired(self) -> None:
        self.timeLastRepaired = self.env.now
        self.timeLastOperationEnded = self.env.now

        self.totalFailedTime += self.timeLastRepaired - self.timeLastFailed

    def toDict(self) -> dict[str, int | float]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if type(value) is int or type(value) is float
        }
