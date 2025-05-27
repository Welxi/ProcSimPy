from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from procsimpy.Line import Line


class Results:
    def __init__(self, line: Line) -> None:
        self.line: Line = line
        self.stubs: list[dict] = []

    def addIteration(self, simTime: float) -> None:
        for object in self.line.nodeList:
            object.stats.createRatios(simTime=simTime)

        self.stubs.append(
            {
                'iteration': len(self.stubs),
                'simTime': simTime,
                'partsCreated': self.line.partsCreated(),
                'stats': {
                    object.id: object.stats.toDict() for object in self.line.nodeList
                },
            }
        )
