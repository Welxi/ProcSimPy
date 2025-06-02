from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.append(os.path.join(Path(sys.path[0]).parent))

from procsimpy import (
    Exit,
    Experiment,
    FixedDistribution,
    Line,
    Server,
    ShiftBuilder,
    Source,
)

print('Machine With Basic Shift Schedule')

arrivalTime = FixedDistribution(mean=0.5)
processingTime = FixedDistribution(mean=3)

shift = ShiftBuilder(schedule=[(0, 5), (10, 15)])
source = Source('S', 'Source', arrivalTime=arrivalTime)
machine = Server('M1', 'Machine', processingTime=processingTime, shift=shift)
exit = Exit('E', 'Exit')

source.defineRouting(successorList=[machine])
machine.defineRouting(
    predecessorList=[source],
    successorList=[exit],
)
exit.defineRouting(predecessorList=[machine])


def main(test=False, maxSimTime: float = 20) -> dict[str, int | float] | None:
    line = Line(nodeList=[source, machine, exit])

    experiment = Experiment(line=line)
    results = experiment.run(maxSimTime=maxSimTime, test=test)

    results = results.stubs[0]  # one iteration

    if test:
        return {
            'parts': exit.stats.numberOfEntitiesEntered,
            'working_percent': machine.stats.workingRatio * 100,
            'off_shift_ratio': machine.stats.offShiftRatio * 100,
        }

    print(f'Sim End Time: {results["simTime"]}')
    print(f'the system produced {results["partsCreated"]} parts')
    print(
        f'the total working ratio of the {machine.name} is {machine.stats.workingRatio:.2%}'
    )
    print(
        f'the total off-shift ratio of the {machine.name} is {machine.stats.offShiftRatio:.2%}'
    )

    return None


if __name__ == '__main__':
    main()
