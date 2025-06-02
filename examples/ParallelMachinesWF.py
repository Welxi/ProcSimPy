from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.append(os.path.join(Path(sys.path[0]).parent))

from procsimpy import (
    Exit,
    Experiment,
    Failure,
    FixedDistribution,
    Line,
    Queue,
    RepairTechnician,
    Server,
    Source,
)

print('Parallel Machines')

arrivalTime = FixedDistribution(mean=0.5)
processingTimeM1 = FixedDistribution(mean=0.25)
processingTimeM2 = FixedDistribution(mean=0.25)

timeToFailure1 = FixedDistribution(mean=60.0)
timeToRepair1 = FixedDistribution(mean=5.0)

timeToFailure2 = FixedDistribution(mean=40.0)
timeToRepair2 = FixedDistribution(mean=10.0)

source = Source('S', 'Source', arrivalTime=arrivalTime)
queue = Queue('Q', 'Queue')
first_machine = Server('M1', 'Machine 1', processingTime=processingTimeM1)
second_machine = Server('M2', 'Machine 2', processingTime=processingTimeM2)
exit = Exit('E', 'Exit')

repair = RepairTechnician('R', 'Repair')
failure1 = Failure(
    'F1', 'Failure1', victim=first_machine, TTF=timeToFailure1, TTR=timeToRepair1
)
failure2 = Failure(
    'F2', 'Failure2', victim=second_machine, TTF=timeToFailure2, TTR=timeToRepair2
)

source.defineRouting(successorList=[queue])
queue.defineRouting(
    predecessorList=[source], successorList=[first_machine, second_machine]
)
first_machine.defineRouting(predecessorList=[queue], successorList=[exit])
second_machine.defineRouting(predecessorList=[queue], successorList=[exit])
exit.defineRouting(predecessorList=[first_machine, second_machine])


# TODO Turn into two test one with and one without failures
def main(test: bool = False, maxSimTime: float = 2) -> dict[str, int | float] | None:
    line = Line(
        nodeList=[source, queue, first_machine, second_machine, exit],
        failures=[failure1, failure2],
        repair=[repair],
    )

    experiment = Experiment(line=line)
    results = experiment.run(maxSimTime=maxSimTime, test=test)

    results = results.stubs[0]  # one iteration

    if test:
        return {
            'parts': results['partsCreated'],
            'working_percent_M1': first_machine.stats.workingRatio * 100,
            'working_percent_M2': second_machine.stats.workingRatio * 100,
        }

    print(f'Sim End Time: {results["simTime"]}')
    print(f'the system produced {results["partsCreated"]} parts')
    print(
        f'Working Percent of {first_machine.name} is {first_machine.stats.workingRatio:.2%}'
    )
    print(
        f'Working Percent of {second_machine.name} is {second_machine.stats.workingRatio:.2%}'
    )

    return None


if __name__ == '__main__':
    main()
