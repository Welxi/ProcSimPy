from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.append(os.path.join(Path(sys.path[0]).parent))

from hepyaestus import (
    Entity,
    Exit,
    Experiment,
    FixedDistribution,
    Line,
    Machine,
    Queue,
)

print('Setting Work in Progress: One Part run till no more events')

processingTime = FixedDistribution(mean=0.25)

queue = Queue('Q1', 'Queue', capacity=1)
machine = Machine('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')
part = Entity('P1', 'Part', startingStation=machine)

queue.defineRouting(
    successorList=[machine],
)
machine.defineRouting(
    predecessorList=[queue],
    successorList=[exit],
)
exit.defineRouting(predecessorList=[machine])


def main(
    test: bool = False, maxSimTime: float = float('inf')
) -> dict[str, int | float] | None:
    line = Line(objectList=[queue, machine, exit, part])

    experiment = Experiment(line=line)
    results = experiment.run(maxSimTime=maxSimTime, test=test)

    results = results.stubs[0]  # one iteration

    if test:
        return {
            'parts': results['partsCreated'],
            'simulationTime': results['simTime'],
            'working_percent': machine.stats.workingRatio * 100,
        }

    print(f'Sim End Time: {results["simTime"]}')
    print(f'the system produced {results["partsCreated"]} parts')
    print(f'Working Percent of {machine.name} is {machine.stats.workingRatio:.2%}')
    return None


if __name__ == '__main__':
    main()
