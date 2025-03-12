# Setting up Your Experiment
To create a model you will need two aspects of this project, 
- the Orchestration Objects
- the Nodes to describe the model desired

Knowledge of both of these aspects will be require to create a valid model and experiment. A set of examples have been provided [[here]] 
## Orchestration Objects
#### Experiment
Controlling running iterations of the experiment and handles collecting and handling of results output and post processing

Other than initialising nodes most users goals should be possible by interacting with this module 

refer to the Experiment Reference page for more details #to/link 
#### Line
(want a better name for this)
The Line here refers to a manufacturing line. it is the container for the process and is the vehicle by which find and interact with node not their direct neighbour

Using multiple lines in you experiment is not currently supported but is part of the project future work

refer to the Line Reference page for more details #to/link
## Nodes
Nodes model the individual steps or stages of your model, each has an internal [SimPy Store](https://simpy.readthedocs.io/en/latest/api_reference/simpy.resources.html#module-simpy.resources.store) that holds an [[Entity]]. 

Nodes trigger [[Events]] of their neighbours to preform handover when they have capacity available or entities to give 

- Source: models the receiving of Entities to the System, in this case every time unit
- Queue: Buffer before the Machine, in more complex systems provides routing decisions
- Machine: Takes an Entity and performs an operation on it for a given time, in this case 2 time units
- Exit: The "Output" of the system