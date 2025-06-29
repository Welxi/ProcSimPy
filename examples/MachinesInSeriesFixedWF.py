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

print('Machines in Series')

arrivalTime = FixedDistribution(mean=0.5)
processingTimeM1 = FixedDistribution(mean=0.25)
processingTimeM2 = FixedDistribution(mean=1.5)

timeToFailure1 = FixedDistribution(mean=60.0)
timeToRepair1 = FixedDistribution(mean=5.0)

timeToFailure2 = FixedDistribution(mean=40.0)
timeToRepair2 = FixedDistribution(mean=10.0)

source = Source('S', 'Source', arrivalTime=arrivalTime)
first_machine = Server('M1', 'Machine 1', processingTime=processingTimeM1)
queue = Queue('Q', 'Queue')
second_machine = Server('M2', 'Machine 2', processingTime=processingTimeM2)
exit = Exit('E', 'Exit')

repair = RepairTechnician('R', 'Repair')
failure1 = Failure(
    'F1', 'Failure1', victim=first_machine, TTF=timeToFailure1, TTR=timeToRepair1
)
failure2 = Failure(
    'F2', 'Failure2', victim=second_machine, TTF=timeToFailure2, TTR=timeToRepair2
)


source.defineRouting(successorList=[first_machine])
first_machine.defineRouting(predecessorList=[source], successorList=[queue])
queue.defineRouting(predecessorList=[first_machine], successorList=[second_machine])
second_machine.defineRouting(predecessorList=[queue], successorList=[exit])
exit.defineRouting(predecessorList=[second_machine])


def main(test: bool = False, maxSimTime: float = 100) -> dict[str, int | float] | None:
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
            'blockage_ratio': first_machine.stats.blockageRatio * 100,
        }

    print(f'Sim End Time: {results["simTime"]}')
    print(f'the system produced {results["partsCreated"]} parts')

    print(
        f'Blocking Percent of {first_machine.name} is {first_machine.stats.blockageRatio:.2%}'
    )

    return None


if __name__ == '__main__':
    main()
