from __future__ import annotations

from typing import TYPE_CHECKING

from hepyaestus.EventData import EventData

if TYPE_CHECKING:
    from hepyaestus.Line import Line
    from simpy import Environment


class BaseObject:
    def __init__(self, id: str, name: str) -> None:
        self.id: str = id
        self.name: str = name
        self.canPrint: bool = True

    def initialize(self, env: Environment, line: Line) -> None:
        self.env: Environment = env
        self.line: Line = line
        self.canPrint = self.line.canTrace(self)

    def printTrace(self, **kw) -> None:
        if not self.canPrint:
            return
        from hepyaestus.printTrace import printTrace

        for key, eventData in kw.items():
            if eventData is None:
                kw[key] = self.basicEventData()
        printTrace(self, **kw)

    def basicEventData(self) -> EventData:
        return EventData(caller=self, time=self.env.now, trace=self.canPrint)

    def noTraceEventData(self) -> EventData:
        return EventData(caller=self, time=self.env.now, trace=False)
