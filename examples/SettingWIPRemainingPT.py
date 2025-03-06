from __future__ import annotations

from hepyaestus import (
    Entity,
    Exit,
    Experiment,
    FixedDistribution,
    Line,
    Machine,
    Queue,
)

print('Setting Work in Progress: One Part run till no more events')

processingTime = FixedDistribution(mean=0.25)
remainingTime = FixedDistribution(mean=0.1)

queue = Queue('Q1', 'Queue', capacity=1)
machine = Machine('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')
part1 = Entity('P1', 'Part', startingStation=machine)
part2 = Entity(
    'P2', 'Part2', startingStation=machine, remainingProcessingTime=remainingTime
)

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
    line = Line(objectList=[queue, machine, exit, part1, part2])

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
