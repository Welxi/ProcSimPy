from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

# TODO make for Operator


def ShiftBuilder(
    pattern: Optional[tuple[float, float]] = None,
    schedule: Optional[list[tuple[float, float]]] = None,
) -> ShiftPattern | ShiftSchedule:
    """
    Returns a Shift based on pattern or schedule

    :param pattern: _description_, defaults to None
    :type pattern: Optional[tuple[float, float]], optional
    :param schedule: _description_, defaults to None
    :type schedule: Optional[list[tuple[float, float]]], optional
    :raises ValueError: _description_
    :return: Shift coresponding to format of input
    :rtype: ShiftPattern | ShiftSchedule
    """
    assert pattern is not None or schedule is not None, (
        'Pattern or Schedule must be set'
    )
    assert pattern is None or schedule is None, 'Only Pattern or Schedule may be set'

    if pattern is not None:
        return ShiftPattern(onFor=pattern[0], offFor=pattern[1])
    if schedule is not None:
        return ShiftSchedule(schedule=schedule)

    raise ValueError('Pattern or Schedule must be set')


class Shift(ABC):
    @abstractmethod
    def isOnShift(self, time: float) -> bool:
        pass

    @abstractmethod
    def next(self, time: float) -> tuple[float, float]:
        """
        Returns the next working times of this shift

        :param time: current time or time of intrest for next working
        :type time: float
        :return: (start, end) of next working time
        :rtype: tuple[float, float]
        """


class ShiftPattern(Shift):
    def __init__(
        self,
        onFor: float,
        offFor: float,
    ) -> None:
        super().__init__()
        self.onFor = onFor
        self.offFor = offFor
        self.repeat = onFor + offFor

    def isOnShift(self, time: float) -> bool:
        return (time % self.repeat) < self.onFor

    def next(self, time: float) -> tuple[float, float]:
        cycles, phase = divmod(time, self.repeat)
        if phase >= self.onFor:
            cycles += 1
        nextStart = self.repeat * cycles
        nextEnd = self.repeat * cycles + self.onFor

        return (nextStart, nextEnd)


class ShiftSchedule(Shift):
    def __init__(
        self,
        schedule: list[tuple[float, float]],
    ) -> None:
        super().__init__()

        self.schedule: list[tuple[float, float]] = vaildateSchedule(schedule)
        self.currentShift = self.schedule.pop(0)
        # ? What to do when schedule doesn't cover the whole MaxSimTime

    def isOnShift(self, time: float) -> bool:
        startShift, endShift = self.currentShift
        return startShift <= time < endShift
        # return any(start <= time < end for start, end in self.schedule)

    def next(self, time: float) -> tuple[float, float]:
        _, endShift = self.currentShift

        if time >= endShift and self.schedule:
            self.currentShift = self.schedule.pop(0)

        return self.currentShift


def vaildateSchedule(schedule: list[tuple[float, float]]) -> list[tuple[float, float]]:
    # Dealing with floats dont use equality comparisons
    lastEnd: float = 0
    for start, end in schedule:
        if start < lastEnd:
            raise ValueError('Schedule not Valid')
        if start > end:
            raise ValueError('Each shift must begin before the shift ends')

        lastEnd = end

    return schedule
