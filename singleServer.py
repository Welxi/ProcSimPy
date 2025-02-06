from hepyaestus.Exit import Exit
from hepyaestus.Experiment import Experiment
from hepyaestus.Line import Line
from hepyaestus.Machine import Machine
from hepyaestus.ProbDistribution import FixedDistribution
from hepyaestus.Queue import Queue
from hepyaestus.Source import Source
from simpy import Environment

RANDOM_SEED = 42
print('Single Server')


arrivalTime = FixedDistribution(mean=0.5)
processingTime = FixedDistribution(mean=0.25)

source = Source('S', 'Source', interArrivalTime=arrivalTime)
queue = Queue('Q1', 'Queue', capacity=1)
machine = Machine('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')

# TODO can define Routing by implicit order of objectList
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


def main(test=False) -> dict[str, int | float] | None:
    env = Environment()
    objectList = [source, queue, machine, exit]
    line = Line(objectList=objectList)
    line.initialize(env=env)

    maxSimTime = 1440.0
    experiment = Experiment(line=line)
    experiment.run(maxSimTime=maxSimTime, test=test)

    workingRatio = (machine.totalWorkingTime / maxSimTime)

    if test:
        return {'parts': exit.numOfExits, 'working_ratio': workingRatio}

    print(f'Sim End Time: {env.now}')
    print(f'the system produced {exit.numOfExits} parts')
    print(f'the total working ratio of the {machine.name} is {workingRatio:.2%}')

    return None


if __name__ == '__main__':
    main()
