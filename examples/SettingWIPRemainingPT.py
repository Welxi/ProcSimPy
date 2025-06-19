from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.append(os.path.join(Path(sys.path[0]).parent))

from procsimpy import (
    Entity,
    Exit,
    Experiment,
    FixedDistribution,
    Line,
    Server,
)

print('Setting Work in Progress: One Part run till no more events')

processingTime = FixedDistribution(mean=0.25)

machine = Server('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')
part1 = Entity('P1', 'Part', startingNode=machine)
part2 = Entity('P2', 'Part2', startingNode=machine, remainingProcessingTime=0.1)

machine.defineRouting(
    successorList=[exit],
)
exit.defineRouting(predecessorList=[machine])


def main(
    test: bool = False, maxSimTime: float = float('inf')
) -> dict[str, int | float] | None:
    line = Line(nodeList=[machine, exit], WIPList=[part1, part2])

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
