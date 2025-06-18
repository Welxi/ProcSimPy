from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from procsimpy.EventData import EventData
    from procsimpy.Line import Line
    from simpy import Environment


class Base:
    """
    Used to ensure each piece of the simulation has access to the SimPy environment
    and the line orchestration module. Create Identifiers used for Logging
    and Printing Traces
    """

    def __init__(self, id: str, name: str) -> None:
        # TODO ensure unique IDs
        # ids could also be auto generated here rather than passed in
        #  or be made optional
        self.id: str = id
        self.name: str = name
        self.canPrint: bool = True
        self.events: list[EventData] = []

    def initialize(self, env: Environment, line: Line) -> None:
        """
        Sets/resets component for new simulation

        :param env: SimPy Simulation Environment
        :type env: Environment
        :param line: Line Orchestration Module
        :type line: LineNode
        """
        #? could append line to env so I dont have to pass both each time
        #  or package together
        self.env: Environment = env
        self.line: Line = line
        self.canPrint = self.line.canTrace(self)

    def printTrace(self, event: EventData) -> None:
        """
        Common formating for logging/tracing based on arguments provided
        """
        if not self.canPrint:
            return
        from procsimpy.printTrace import printTrace

        self.events.append(event)
        printTrace(event)
