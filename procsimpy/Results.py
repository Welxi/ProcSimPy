from __future__ import annotations

from typing import TYPE_CHECKING

from simpy.core import Infinity, SimTime

if TYPE_CHECKING:
    from procsimpy.Line import Line


class Results:
    def __init__(self, line: Line) -> None:
        self.line: Line = line
        self.stubs: list[dict] = []

    def addIteration(self, simTime: SimTime) -> None:
        if simTime == Infinity:
            # sim has ended due to no more events to process
            #  so we need to find last event
            simTime = max(
                node.stats.timeLastEntityReceived for node in self.line.nodeList
            )

        for object in self.line.nodeList:
            object.stats.createRatios(simTime=simTime)

        self.stubs.append(
            {
                'iteration': len(self.stubs),
                'simTime': simTime,
                # TODO if simTime is Inf need to do last event processed
                'partsCreated': self.line.partsCreated(),
                'stats': {
                    object.id: object.stats.toDict() for object in self.line.nodeList
                },
            }
        )
