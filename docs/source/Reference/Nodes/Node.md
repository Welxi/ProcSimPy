# Node
The basic structure for a permanent part of your model. It represent a step in the process, connected to both predecessors and successors 
This class is a large part of the library. It is a focal point

To understand the role of a node in the library please refer to {make overview guide}. It is the basis for the inheritor nodes used in the examples provided {Source}, {Queue}, {Server}, and {Exit}

If an unique components are necessary for your experiment it is recommended to inherit this class and overload  methods as necessary If you are creating your own components for a model and the others provided do not suit the requirements this class should be inherited. It's main role to provide standard ways for Nodes to communicate and Handover entities of the model from/to other Node

Each Store Node creates a {Statistics} subcomponent the can be told when certain events occur to create the output data for the experiment. It only store times of most resent events of a given type and a sum of totals 

the behaviour of this class is defined by the interaction of many subcomponents, many of which can be altered via dependency injection

Each Node has two internal SimPy stores, one use very much as intended by the SimPy library and one that is the inverse, being filled with availability token when the normal store has capacity. the role of the Availability tokens is explained further in the handover process section.

Each Node has three "processes" generator functions that are added to the SimPy environment via the {Enviroment.process} and model the behaviour over time.

My recommendation to anyone extending the library is the keep the processes as simply as is reasonable and have state/behaviour side-effects modelled in class functions. This is largely due to processes being interrupted by Failures and Shift change as the work required to restart a process in the required state increasing their complexity 

the three process described in further detail later in this document are:
- Operation
- ProcessEntity
- Handover
### Operation process
Is concerned with the ability of the node to perform its function. it handles modelling shift behaviour and response to failures.

it is responsible for the only event current library, onOperation. 
a process will ask the Operation process if the node is operating and if it is not will then request the event. the event will be triggered when the Node returns to operation.
(see {Handover} for the use case)
### ProcessEntity
Some nodes require time to perform their role/work.  ProcessEntity is called by each resolved put request to the nodes store. 

depending on the capacity of the node many of these can spawn and are stored in the workQueue list. 

When the Operation Process triggers a failure these spawned processes are interrupted (with progress saved based on interrupt type) and the Operation respawns these process based after recovery
### Handover
Nodes are designed to work in a network of other nodes, the checking of availability of successor nodes and routing between multiple available targets are modelled with this process

it is not interrupted by the Operation Process as to not recreated requests, but it checks for the onOperation Event at points where a non-operational node would not be able to handover:
- before requesting availability
- before removing entity from store

Pre-empting is not currently supported 





