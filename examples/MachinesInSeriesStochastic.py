from __future__ import annotations

import os
import sys
from pathlib import Path

from procsimpy.ProbDistribution import FixedDistribution

sys.path.append(os.path.join(Path(sys.path[0]).parent))

from procsimpy import (
    Exit,
    ExpDistribution,
    Experiment,
    GaussianDistribution,
    Line,
    Queue,
    Server,
    Source,
)

print('Machines in Series')

arrivalTime = ExpDistribution(mean=0.5)
processingTimeM1 = GaussianDistribution(mean=0.25, stdev=0.1, min=0.1, max=1)
processingTimeM2 = GaussianDistribution(mean=1.5, stdev=0.3, min=0.1, max=5)

timeToFailure1 = FixedDistribution(mean=60.0)
timeToRepair1 = FixedDistribution(mean=5.0)

timeToFailure2 = FixedDistribution(mean=40.0)
timeToRepair2 = FixedDistribution(mean=10.0)

source = Source('S', 'Source', arrivalTime=arrivalTime)
queue = Queue('Q', 'Queue')
first_machine = Server('M1', 'Machine 1', processingTime=processingTimeM1)
second_machine = Server('M2', 'Machine 2', processingTime=processingTimeM2)
exit = Exit('E', 'Exit')

source.defineRouting(successorList=[queue])
queue.defineRouting(
    predecessorList=[source], successorList=[first_machine, second_machine]
)
first_machine.defineRouting(predecessorList=[queue], successorList=[exit])
second_machine.defineRouting(predecessorList=[queue], successorList=[exit])
exit.defineRouting(predecessorList=[first_machine, second_machine])


def main(test: bool = False, maxSimTime: float = 10) -> dict[str, int | float] | None:
    line = Line(nodeList=[source, queue, first_machine, second_machine, exit])

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
