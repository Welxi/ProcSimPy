from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.append(os.path.join(Path(sys.path[0]).parent))

from hepyaestus import (
    Exit,
    ExpDistribution,
    Experiment,
    GaussianDistribution,
    Line,
    Machine,
    Queue,
    Source,
)

print('Machines in Series')

arrivalTime = ExpDistribution(mean=0.5)
processingTimeM1 = GaussianDistribution(mean=0.25, stdev=0.1, min=0.1, max=1)
processingTimeM2 = GaussianDistribution(mean=1.5, stdev=0.3, min=0.1, max=5)

# TODO Repairman
source = Source('S', 'Source', interArrivalTime=arrivalTime)
queue = Queue('Q', 'Queue', capacity=1)
first_machine = Machine('M1', 'Machine 1', processingTime=processingTimeM1)
second_machine = Machine('M2', 'Machine 2', processingTime=processingTimeM2)
exit = Exit('E', 'Exit')

# TODO Failures
# F1 = Failure(
#     victim=M1,
#     distribution={'TTF': {'Fixed': {'mean': 60.0}}, 'TTR': {'Fixed': {'mean': 5.0}}},
#     repairman=R,
# )
# F2 = Failure(
#     victim=M2,
#     distribution={'TTF': {'Fixed': {'mean': 40.0}}, 'TTR': {'Fixed': {'mean': 10.0}}},
#     repairman=R,
# )

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
    experiment.run(maxSimTime=maxSimTime, test=test, numberOfReplications=10)
    # TODO Set seed (in dream seed=1)

    # In Dream they do not have a test for this
    # They rely on the KE Tool for stat functions to generate
    # - 95% Confidence interval
    # - lower bound
    # - mean
    # - upper bound

    return None


if __name__ == '__main__':
    main()
