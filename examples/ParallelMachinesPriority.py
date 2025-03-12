from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.append(os.path.join(Path(sys.path[0]).parent))

from hepyaestus import Exit, Experiment, FixedDistribution, Line, Machine, Queue, Source

print('Selective Queue Chooses Priority')

arrivalTime = FixedDistribution(mean=0.5)
processingTimeM1 = FixedDistribution(mean=0.25)
processingTimeM2 = FixedDistribution(mean=0.25)


class SelectiveQueue(Queue):
    # TODO Selective Queue
    # #override so that it chooses receiver according to priority
    # def selectReceiver(self,possibleReceivers=[]):
    #     # sort the receivers according to their priority
    #     possibleReceivers.sort(key=lambda x: x.priority, reverse=True)
    #     if possibleReceivers[0].canAccept():
    #         return possibleReceivers[0]
    #     elif possibleReceivers[1].canAccept():
    #         return possibleReceivers[1]
    #     return None
    pass


source = Source('S', 'Source', interArrivalTime=arrivalTime)
selectiveQ = SelectiveQueue('Q', 'Queue', capacity=1)
first_machine = Machine('M1', 'Machine 1', processingTime=processingTimeM1)
second_machine = Machine('M2', 'Machine 2', processingTime=processingTimeM2)
exit = Exit('E', 'Exit')
# TODO F = Failure
# (
#     victim=M1,
#     distribution={'TTF': {'Fixed': {'mean': 60.0}}, 'TTR': {'Fixed': {'mean': 5.0}}},
# )

# TODO Move to constructor
first_machine.priority = 10
second_machine.priority = 0

source.defineRouting(successorList=[selectiveQ])
selectiveQ.defineRouting(
    predecessorList=[source], successorList=[first_machine, second_machine]
)
first_machine.defineRouting(predecessorList=[selectiveQ], successorList=[exit])
second_machine.defineRouting(predecessorList=[selectiveQ], successorList=[exit])
exit.defineRouting(predecessorList=[first_machine, second_machine])


def main(test: bool = False, maxSimTime: float = 10) -> dict[str, int | float] | None:
    line = Line(objectList=[source, selectiveQ, first_machine, second_machine, exit])

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
