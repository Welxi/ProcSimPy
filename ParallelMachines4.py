from __future__ import annotations

from hepyaestus.Exit import Exit
from hepyaestus.Experiment import Experiment
from hepyaestus.Line import Line
from hepyaestus.Machine import Machine
from hepyaestus.ProbDistribution import FixedDistribution
from hepyaestus.Queue import Queue
from hepyaestus.Source import Source

print('Selective Queue Chooses Priority')

arrivalTime = FixedDistribution(mean=0.5)
processingTimeM1 = FixedDistribution(mean=0.25)
processingTimeM2 = FixedDistribution(mean=1.5)


# the custom queue
class SelectiveQueue(Queue):
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
    # def getEntity(self):
    #     activeEntity=Machine.getEntity(self)        #call the parent method to get the entity
    #     part=self.getActiveObjectQueue()[0]         #retrieve the obtained part
    #     part.machineId=self.id                      #create an attribute to the obtained part and give it the value of the object's id
    #     return activeEntity
    pass  # return the entity obtained


# the custom exit
class CountingExit(Exit):
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
# F = Failure(
#     victim=M1,
#     distribution={'TTF': {'Fixed': {'mean': 60.0}}, 'TTR': {'Fixed': {'mean': 5.0}}},
# )

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
    experiment.run(maxSimTime=maxSimTime, test=test)

    # blockageRatio1 = first_machine.totalBlockageTime / maxSimTime
    workingRatio1 = first_machine.totalWorkingTime / maxSimTime
    # blockageRatio2 = second_machine.totalBlockageTime / maxSimTime
    workingRatio2 = second_machine.totalWorkingTime / maxSimTime

    # return results for the test
    if test:
        return {
            'parts': exit.numOfExits,
            'working_ratio_M1': workingRatio1 * 100,
            'working_ratio_M2': workingRatio2 * 100,
        }
        #   "NumM1":G.NumM1,
        #   "NumM2":G.NumM2}

    print(f'Sim End Time: {experiment.env.now}')
    print(f'the system produced {exit.numOfExits} parts')
    # print(f'the blockage ratio of the {first_machine.name} is {blockageRatio1:.2%}')
    print(f'the working ratio of the {first_machine.name} is {workingRatio1:.2%}')
    # print(f'the blockage ratio of the {second_machine.name} is {blockageRatio2:.2%}')
    print(f'the working ratio of the {second_machine.name} is {workingRatio2:.2%}')
    # print M1.objName, "produced", G.NumM1, "parts"
    # print M2.objName, "produced", G.NumM2, "parts"
    return None


if __name__ == '__main__':
    main()
