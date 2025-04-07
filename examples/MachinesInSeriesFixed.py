from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.append(os.path.join(Path(sys.path[0]).parent))

from hepyaestus import (
    Exit,
    Experiment,
    Failure,
    FixedDistribution,
    Line,
    Machine,
    Queue,
    RepairTechnician,
    Source,
)

print('Machines in Series')

arrivalTime = FixedDistribution(mean=0.5)
processingTimeM1 = FixedDistribution(mean=0.25)
processingTimeM2 = FixedDistribution(mean=1.5)

timeToFailure = FixedDistribution(mean=2.0)
timeToRepair = FixedDistribution(mean=1.0)

source = Source('S', 'Source', interArrivalTime=arrivalTime)
first_machine = Machine('M1', 'Machine 1', processingTime=processingTimeM1)
queue = Queue('Q', 'Queue', capacity=1)
second_machine = Machine('M2', 'Machine 2', processingTime=processingTimeM2)
exit = Exit('E', 'Exit')


repair = RepairTechnician('R', 'Repair')
failure = Failure(
    'F',
    'Failure',
    victim=first_machine,
    TTF=timeToFailure,
    TTR=timeToRepair,
    repair=repair,
)
# F2 = Failure(
#     victim=M2,
#     distribution={'TTF': {'Fixed': {'mean': 40.0}}, 'TTR': {'Fixed': {'mean': 10.0}}},
#     repairman=R,
# )


source.defineRouting(successorList=[first_machine])
first_machine.defineRouting(predecessorList=[source], successorList=[queue])
queue.defineRouting(predecessorList=[first_machine], successorList=[second_machine])
second_machine.defineRouting(predecessorList=[queue], successorList=[exit])
exit.defineRouting(predecessorList=[second_machine])


def main(test: bool = False, maxSimTime: float = 5) -> dict[str, int | float] | None:
    objectList = [source, queue, first_machine, second_machine, exit, failure, repair]
    line = Line(objectList=objectList)

    # line.filterTrace(failure)

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
