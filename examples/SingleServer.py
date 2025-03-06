from __future__ import annotations

from hepyaestus import Exit, Experiment, FixedDistribution, Line, Machine, Queue, Source

print('Single Server')

arrivalTime = FixedDistribution(mean=0.5)
processingTime = FixedDistribution(mean=0.25)

source = Source('S', 'Source', interArrivalTime=arrivalTime)
queue = Queue('Q1', 'Queue', capacity=1)
machine = Machine('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')

source.defineRouting(successorList=[queue])
queue.defineRouting(
    predecessorList=[source],
    successorList=[machine],
)
machine.defineRouting(
    predecessorList=[queue],
    successorList=[exit],
)
exit.defineRouting(predecessorList=[machine])


def main(test=False, maxSimTime: float = 10) -> dict[str, int | float] | None:
    line = Line(objectList=[source, queue, machine, exit])

    experiment = Experiment(line=line)
    experiment.run(maxSimTime=maxSimTime, test=test)

    workingRatio = machine.totalWorkingTime / experiment.env.now

    if test:
        return {'parts': exit.numOfExits, 'working_ratio': workingRatio * 100}

    print(f'Sim End Time: {experiment.env.now}')
    print(f'the system produced {exit.numOfExits} parts')
    print(f'the total working ratio of the {machine.name} is {workingRatio:.2%}')

    return None


if __name__ == '__main__':
    main()
