from __future__ import annotations

from hepyaestus.Exit import Exit
from hepyaestus.Experiment import Experiment
from hepyaestus.Line import Line
from hepyaestus.Machine import Machine
from hepyaestus.ProbDistribution import FixedDistribution
from hepyaestus.Queue import Queue
from hepyaestus.Source import Source

print('Parallel Machines')

arrivalTime = FixedDistribution(mean=0.5)
processingTimeM1 = FixedDistribution(mean=0.25)
processingTimeM2 = FixedDistribution(mean=1.5)

source = Source('S', 'Source', interArrivalTime=arrivalTime)
queue = Queue('Q', 'Queue', capacity=1)
first_machine = Machine('M1', 'Machine 1', processingTime=processingTimeM1)
second_machine = Machine('M2', 'Machine 2', processingTime=processingTimeM2)
exit = Exit('E', 'Exit')

source.defineRouting(successorList=[queue])
queue.defineRouting(
    predecessorList=[source], successorList=[first_machine, second_machine]
)
first_machine.defineRouting(predecessorList=[queue], successorList=[exit])
second_machine.defineRouting(predecessorList=[queue], successorList=[exit])
exit.defineRouting(predecessorList=[first_machine, second_machine])


def main(test: bool = False, maxSimTime: float = 10) -> dict[str, int | float] | None:
    objectList = [source, queue, first_machine, second_machine, exit]
    line = Line(objectList=objectList)

    experiment = Experiment(line=line)
    experiment.run(maxSimTime=maxSimTime, test=test)

    # blockageRatio1 = first_machine.totalBlockageTime / maxSimTime
    workingRatio1 = first_machine.totalWorkingTime / maxSimTime
    # blockageRatio2 = second_machine.totalBlockageTime / maxSimTime
    workingRatio2 = second_machine.totalWorkingTime / maxSimTime

    if test:
        return {
            'parts': exit.numOfExits,
            'working_ratio_M1': workingRatio1 * 100,
            'working_ratio_M2': workingRatio2 * 100,
        }

    print(f'Sim End Time: {experiment.env.now}')
    print(f'the system produced {exit.numOfExits} parts')
    # print(f'the blockage ratio of the {first_machine.name} is {blockageRatio1:.2%}')
    print(f'the working ratio of the {first_machine.name} is {workingRatio1:.2%}')
    # print(f'the blockage ratio of the {second_machine.name} is {blockageRatio2:.2%}')
    print(f'the working ratio of the {second_machine.name} is {workingRatio2:.2%}')

    return None


if __name__ == '__main__':
    main()
