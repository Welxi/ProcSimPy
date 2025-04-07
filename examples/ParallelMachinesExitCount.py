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
    Source,
)

print('Selective Queue Chooses Priority')

arrivalTime = FixedDistribution(mean=0.5)
processingTimeM1 = FixedDistribution(mean=0.25)
processingTimeM2 = FixedDistribution(mean=0.25)

timeToFailure = FixedDistribution(mean=6.0)
timeToRepair = FixedDistribution(mean=1.0)


# the custom queue
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


# the custom machine
class Milling(Machine):
    # ? Unsure of reason, could be achieved by reviewing stations visited
    # def getEntity(self):
    #     activeEntity=Machine.getEntity(self)        #call the parent method to get the entity
    #     part=self.getActiveObjectQueue()[0]         #retrieve the obtained part
    #     part.machineId=self.id                      #create an attribute to the obtained part and give it the value of the object's id
    #     return activeEntity
    pass  # return the entity obtained


# the custom exit
class CountingExit(Exit):
    # TODO Counting Exit
    # def getEntity(self):
    #     activeEntity=Exit.getEntity(self)                        #call the parent method to get the entity
    #     #check the attribute and update the counters accordingly
    #     if activeEntity.machineId=='M1':
    #         G.NumM1+=1
    #     elif activeEntity.machineId=='M2':
    #         G.NumM2+=1
    #     return activeEntity             #return the entity obtained
    pass


source = Source('S', 'Source', interArrivalTime=arrivalTime)
selectiveQ = SelectiveQueue('Q', 'Queue', capacity=1)
first_machine = Milling('M1', 'Machine 1', processingTime=processingTimeM1)
second_machine = Milling('M2', 'Machine 2', processingTime=processingTimeM2)
exit = CountingExit('E', 'Exit')
failure = Failure(
    'F',
    'Failure',
    victim=first_machine,
    TTF=timeToFailure,
    TTR=timeToRepair,
)

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
            'produced_M1': len(first_machine.stats.exits),
            'working_percent_M2': second_machine.stats.workingRatio * 100,
            'produced_M2': len(second_machine.stats.exits),
        }

    print(f'Sim End Time: {results["simTime"]}')
    print(f'the system produced {results["partsCreated"]} parts')
    print(
        f'Working Percent of {first_machine.name} is {first_machine.stats.workingRatio:.2%}'
    )
    print(f'{first_machine.name} produced {len(first_machine.stats.exits)}')
    print(
        f'Working Percent of {second_machine.name} is {second_machine.stats.workingRatio:.2%}'
    )
    print(f'{second_machine.name} produced {len(second_machine.stats.exits)}')
    return None


if __name__ == '__main__':
    main()
