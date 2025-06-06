from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

# TODO make for Operator


def ShiftBuilder(
    pattern: Optional[tuple[float, float]] = None,
    schedule: Optional[list[tuple[float, float]]] = None,
) -> ShiftPattern | ShiftSchedule:
    assert pattern is not None or schedule is not None, (
        'Pattern or Schedule must be set'
    )
    assert pattern is None or schedule is None, 'Only Pattern or Schedule may be set'

    if pattern is not None:
        return ShiftPattern(onFor=pattern[0], offFor=pattern[1])
    if schedule is not None:
        return ShiftSchedule(schedule=schedule)

    raise ValueError('Pattern or Schedult must be set')


class Shift(ABC):
    @abstractmethod
    def isOnShift(self, time: float) -> bool:
        pass

    @abstractmethod
    def next(self, time: float) -> tuple[float, float]:
        pass


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
        repeats = time // self.repeat
        nextStart = self.repeat * repeats
        nextEnd = self.repeat * repeats + self.onFor

        return (nextStart, nextEnd)


class ShiftSchedule(Shift):
    def __init__(
        self,
        schedule: list[tuple[float, float]],
    ) -> None:
        super().__init__()

        self.schedule: list[tuple[float, float]] = vaildateSchedule(schedule)
        # ? What to do when schedule doesn't cover the whole MaxSimTime

    def isOnShift(self, time: float) -> bool:
        return any(start < time < end for start, end in self.schedule)

    def next(self, time: float) -> tuple[float, float]:
        # TODO make so each call dose not need to loop through begining
        for idx, (_, end) in enumerate(self.schedule):
            if time > end:
                if self.schedule[idx] != self.schedule[-1]:
                    return self.schedule[idx + 1]
                else:
                    raise AssertionError('Schedule does not cover maxSimTime')

        # mainly here to make linter happy
        raise AssertionError('Schedule does not cover maxSimTime')


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
