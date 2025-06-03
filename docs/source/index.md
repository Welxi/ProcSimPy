# Process SimPy
This project is built on top of the [SimPy](https://simpy.readthedocs.io/en/latest/) Library and aims to provide common abstractions used in Simulation Experiments focusing on modelling a Process, with a Particular focus on the Manufacturing domain

In many cases when setting up ProcSimPy objects accessing prebuilt functionality is done in the constructor method. the preferred method is to use the enums provided, this allows for greater static analysis done by your editor and ensuring the requested functionality is supported. If there is missing functionality please open an Issue on the GitHub Page
## A simple single server example
All the primary nodes are used in this example, they are:
- Source: models the receiving of Entities to the System, in this case every time unit
- Queue: Buffer before the Machine, in more complex systems provides routing decisions
- Machine: Takes an Entity and performs an operation on it for a given time, in this case 2 time units
- Exit: The "Output" of the system

>Note on Time
>The Library relies on [SimPy time scheduling](https://simpy.readthedocs.io/en/latest/topical_guides/time_and_scheduling.html). It is agnostic to the time scale of the model, what one time unit means in your system is up to you (1 second/minute/hour/etc.)
>
>It is important to note that you keep the same base when inputting values 

```python
from hepyaestus import Exit, Experiment, FixedDistribution, Line, Machine, Queue, Source

# Define the timings of Intrest
arrivalTime = FixedDistribution(mean=1)
processingTime = FixedDistribution(mean=2)

# Create the Nodes of Intrest
source = Source('S', 'Source', interArrivalTime=arrivalTime)
queue = Queue('Q1', 'Queue', capacity=1)
machine = Machine('M1', 'Machine', processingTime=processingTime)
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
line = Line(objectList=[source, queue, machine, exit])
experiment = Experiment(line=line)

results = experiment.run(maxSimTime=maxSimTime, test=test)

# we are only interested in the first iteration so we can shadow the first results stub
results = results.stubs[0]  

print(f'Sim End Time: {results["simTime"]}')
print(f'the system produced {results["partsCreated"]} parts')
print(f'Working Percent of {machine.name} is {machine.stats.workingRatio:.2%}')
```
# Next Steps
The individual descriptions can be found in the Reference section but it is advised to read [](../source/Setting%20up%20Your%20Experiment.md) first


