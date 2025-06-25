```{toctree}
:hidden:
Home <self>
Reference/Nodes/Node.md
Reference/Nodes/Exit.md
Reference/Nodes/Queue.md
Reference/Nodes/Server.md
Reference/Nodes/Source.md
Reference/Entity.md
Reference/Experiment.md
Reference/Line.md
Reference/Probability.md
guides/new_to_simulation.md
guides/setting_up_your_experiment.md
apidocs/index.rst
about/acknowledgements.md
about/defense_of_design.md
about/how_to_contribute.md
about/maintenance/pull_requests.md
about/maintenance/readthedocs.md
about/maintenance/structurizr.md
```
# Process SimPy
This project is built on top of the [SimPy](https://simpy.readthedocs.io/en/latest/) Library and aims to provide common abstractions used in Simulation Experiments focusing on modelling a Process, with a Particular focus on the Manufacturing domain
## A simple single server example
All the primary nodes are used in this example, they are:
- Source: models the receiving of Entities to the System, in this case every time unit
- Queue: Buffer before the Machine
- Machine: Takes an Entity and performs an operation on it for a given time, in this case 2 time units
- Exit: The "Output" of the system

```python
from procsimpy import (
    Exit,
    Experiment,
    FixedDistribution,
    Line,
    Queue,
    Server,
    Source,
)

# Define the timings of Intrest
arrivalTime = FixedDistribution(mean=1)
processingTime = FixedDistribution(mean=2)

# Create the Nodes of Intrest
source = Source('S', 'Source', arrivalTime=arrivalTime)
queue = Queue('Q1', 'Queue')
machine = Server('M1', 'Machine', processingTime=processingTime)
exit = Exit('E', 'Exit')

# Link the Nodes to each other (input/output)
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

# Create the Orchestration Objects
line = Line(nodeList=[source, queue, machine, exit])
experiment = Experiment(line=line)

results = experiment.run(maxSimTime=10)

# we are only interested in the first iteration so we can shadow the first results stub
results = results.stubs[0]  

print(f'Sim End Time: {results["simTime"]}')
print(f'the system produced {results["partsCreated"]} parts')
print(f'Working Percent of {machine.name} is {machine.stats.workingRatio:.2%}')
```
# Next Steps
The individual descriptions can be found in the Reference section but it is advised to read {experiment} first
