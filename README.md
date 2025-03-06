# Process SimPy (ProcSimPy)
> Warning this project is currently undergoing development and validation please use under you own discretion

Discrete Event Simulation (DES) Python Library for the Manufacturing and Supply line Domains, built on top of [SimPy](https://github.com/simpx/simpy). The scope of the project is to provide simulation modellers with a collection of open source DES objects that can be connected like "black boxes" in order to form a model.

This collection is desired to be expandable by giving means to developers for:
- customizing existing objects
- adding completely new objects to the list

It is encouraged to build on the abstractions provided in the OOP methodology. Class reference documentation can be found in the [documentation](https://hepyaestus.readthedocs.io/en/latest/) where you can also find tutorials and examples.

SimPy uses Process to model elements in the simulation. These Process are defined in Python by [generator](http://docs.python.org/3/glossary.html#term-generator) functions. This Library aims to provide abstractions and tools to aid in the simulation of problems in the Manufacturing and Supply line Domains.

This project relies on many of the GitHub features for collaboration, if can questions cannot be answered by the documentation please feel free to start a discussion or if you encounter a bug please create an issue 
## How to use
A simple single server example

- Source: models the receiving of Entities to the System, in this case every time unit
- Queue: Buffer before the Machine, in more complex systems provides routing decisions
- Machine: Takes an Entity and performs an operation on it for a given time, in this case 2 time units
- Exit: The "Output" of the system

>Note on Time
>
>The Library relies on [SimPy time scheduling](https://simpy.readthedocs.io/en/latest/topical_guides/time_and_scheduling.html). It is agnostic to the time scale of the model, what one time unit means in your system is up to you (1 second/minute/hour/etc.)
>
>It is important to note that you keep the same base when inputting values 

```python 
from hepyaestus.Exit import Exit
from hepyaestus.Experiment import Experiment
from hepyaestus.Line import Line
from hepyaestus.Machine import Machine
from hepyaestus.ProbDistribution import FixedDistribution
from hepyaestus.Queue import Queue
from hepyaestus.Source import Source

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

experiment.run(maxSimTime=10)

workingRatio = machine.totalWorkingTime / maxSimTime

print(f'Sim End Time: {experiment.env.now}')
print(f'the system produced {exit.numOfExits} parts')
print(f'the total working ratio of the {machine.name} is {workingRatio:.2%}')
```
## Installation
Currently in Alpha, you must clone and install dependencies (in project.toml) from package manager of choice 
#### Getting the Repository

1. Clone the Project:
	- get command from green Code button above repository
	- or `git clone https://github.com/Welxi/HePYaestus.git`

2. Move to Folder Created

3. create a [virtual environment](https://docs.python.org/3/library/venv.html) and set your console to use it. This will depend on Operating System and Python installation

4. point package manager to the pyproject.toml
    - `uv sync`
    - `pip install pyproject.toml --extra dev` 

You should be able to run `pytest` to run tests and explore the project. If you run into any probelms please open an Issue on the GitHub


## Acknowledgements
This Project is a fork of ManPy. ManPy is product of a research project funded from the European Union Seventh Framework Programme (FP7-2012-NMP-ICT-FoF) under grant agreement n° 314364. The project name is DREAM and stands for "Simulation based application Decision support in Real-time for Efficient Agile Manufacturing". More information about the scope of DREAM can be found in http://dream-simulation.eu/.


