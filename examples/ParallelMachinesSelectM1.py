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

print('Selective Queue Chooses M1 over M2')

arrivalTime = FixedDistribution(mean=0.5)
processingTimeM1 = FixedDistribution(mean=0.25)
processingTimeM2 = FixedDistribution(mean=0.25)

timeToFailure = FixedDistribution(mean=6.0)
timeToRepair = FixedDistribution(mean=1.0)


class SelectiveQueue(Queue):
    # TODO Selective Queue
    # override so that it first chooses M1 and then M2
    # def selectReceiver(self, possibleReceivers=[]):
    #     if first_machine.canAccept():
    #         return first_machine
    #     elif second_machine.canAccept():
    #         return second_machine
    #     return None
    pass


source = Source('S', 'Source', arrivalTime=arrivalTime)
selectiveQ = SelectiveQueue('Q', 'Queue', capacity=1)
first_machine = Server('M1', 'Machine 1', processingTime=processingTimeM1)
second_machine = Server('M2', 'Machine 2', processingTime=processingTimeM2)
exit = Exit('E', 'Exit')

repair = RepairTechnician('R', 'Repair')
failure = Failure(
    'F',
    'Failure',
    victim=first_machine,
    TTF=timeToFailure,
    TTR=timeToRepair,
)

source.defineRouting(successorList=[selectiveQ])
selectiveQ.defineRouting(
    predecessorList=[source], successorList=[first_machine, second_machine]
)
first_machine.defineRouting(predecessorList=[selectiveQ], successorList=[exit])
second_machine.defineRouting(predecessorList=[selectiveQ], successorList=[exit])
exit.defineRouting(predecessorList=[first_machine, second_machine])


def main(test: bool = False, maxSimTime: float = 10) -> dict[str, int | float] | None:
    line = Line(nodeList=[source, selectiveQ, first_machine, second_machine, exit])

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
