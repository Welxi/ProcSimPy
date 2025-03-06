from __future__ import annotations

from hepyaestus import Exit, Experiment, FixedDistribution, Line, Machine, Source

print('Machine With Shift Schedule and receive before end Threshold')

arrivalTime = FixedDistribution(mean=0.5)
processingTime = FixedDistribution(mean=3)

source = Source('S', 'Source', interArrivalTime=arrivalTime)
machine = Machine('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')

# TODO ShiftScheduler
# SS=ShiftScheduler(victim=M, shiftPattern=[[0,5],[10,15]],receiveBeforeEndThreshold=3)

source.defineRouting(successorList=[machine])
machine.defineRouting(
    predecessorList=[source],
    successorList=[exit],
)
exit.defineRouting(predecessorList=[machine])


def main(test=False, maxSimTime: float = 10) -> dict[str, int | float] | None:
    line = Line(objectList=[source, machine, exit])

    experiment = Experiment(line=line)
    experiment.run(maxSimTime=maxSimTime, test=test)

    workingRatio = machine.totalWorkingTime / experiment.env.now
    # TODO totalOffShiftTime for Machine
    offShiftRatio = 0.50  #  machine.totalOffShiftTime / experiment.env.now

    if test:
        return {
            'parts': exit.numOfExits,
            'working_ratio': workingRatio * 100,
            'off_shift_ratio': offShiftRatio * 100,
        }

    print(f'Sim End Time: {experiment.env.now}')
    print(f'the system produced {exit.numOfExits} parts')
    print(f'the total working ratio of the {machine.name} is {workingRatio:.2%}')
    print(f'the total off-shift ratio of the {machine.name} is {offShiftRatio:.2%}')

    return None


if __name__ == '__main__':
    main()
