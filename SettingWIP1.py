from __future__ import annotations

from hepyaestus.Entity import Entity
from hepyaestus.Exit import Exit
from hepyaestus.Experiment import Experiment
from hepyaestus.Line import Line
from hepyaestus.Machine import Machine
from hepyaestus.ProbDistribution import FixedDistribution
from hepyaestus.Queue import Queue

print('Setting Work in Progress: One Part run till no more events')

processingTime = FixedDistribution(mean=0.25)

queue = Queue('Q1', 'Queue', capacity=1)
machine = Machine('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')
part = Entity('P1', 'Part', startingStation=machine)

queue.defineRouting(
    successorList=[machine],
)
machine.defineRouting(
    predecessorList=[queue],
    successorList=[exit],
)
exit.defineRouting(predecessorList=[machine])


def main(
    test: bool = False, maxSimTime: float = float('inf')
) -> dict[str, int | float] | None:
    line = Line(objectList=[queue, machine, exit, part])

    experiment = Experiment(line=line)
    experiment.run(maxSimTime=maxSimTime, test=test)

    workingRatio = machine.totalWorkingTime / exit.timeLastEntityLeft

    if test:
        return {
            'parts': exit.numOfExits,
            'simulationTime': exit.timeLastEntityLeft,
            'working_ratio': workingRatio * 100,
        }

    print(f'Sim End Time: {experiment.env.now}')
    print(f'the system produced {exit.numOfExits} parts in {experiment.env.now} min')
    print(f'the total working ratio of the {machine.name} is {workingRatio:.2%}')
    return None


if __name__ == '__main__':
    main()
