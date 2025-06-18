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
    Queue,
    Server,
    Source,
)

print('Single Server')

arrivalTime = FixedDistribution(mean=0.5)
processingTime = FixedDistribution(mean=0.25)

source = Source('S', 'Source', arrivalTime=arrivalTime)
queue = Queue('Q1', 'Queue')
machine = Server('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')

source.defineRouting(successorList=[queue])
queue.defineRouting(predecessorList=[source], successorList=[machine])
machine.defineRouting(predecessorList=[queue], successorList=[exit])
exit.defineRouting(predecessorList=[machine])


def main(test=False, maxSimTime: float = 10) -> dict[str, int | float] | None:
    line = Line(nodeList=[source, queue, machine, exit])

    experiment = Experiment(line=line)
    results = experiment.run(maxSimTime=maxSimTime, test=test)

    results = results.stubs[0]  # one iteration

    if test:
        return {
            'parts': results['partsCreated'],
            'working_percent': machine.stats.workingRatio * 100,
        }

    print(f'Sim End Time: {results["simTime"]}')
    print(f'the system produced {results["partsCreated"]} parts')
    print(f'Working Percent of {machine.name} is {machine.stats.workingRatio:.2%}')

    return None


if __name__ == '__main__':
    main()
