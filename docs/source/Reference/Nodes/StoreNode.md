# Store Node
The basic structure for a permanent part of your model, you cannot use this in the model directly but as it provides no run method for use in the SimPy env.process() to create and handle events

If you are creating your own components for a model and the others provided do not suit the requirements this class should be inherited. It's main role to provide standard ways for Nodes to communicate and Handover entities of the model from/to other Node

Node are linked in a Linked List Pattern using the defineRouting Function

Each Store Node creates a Statistics subcomponent the can be told when certain events occur to create the output data for the experiment
##### Internal SimPy Store
Give and receive functions
These should only be called from within the the nodes run function when handling events (isRequested and canDispose). They expose the the underlying [SimPy Store](https://simpy.readthedocs.io/en/latest/api_reference/simpy.resources.html#module-simpy.resources.store) object

- sortReceivers: priority or can be overloaded
    - if we get more feedback we can provide more use cases

##### Handover
The remaining functions are entity handover related 

Many of the other functions this class provides are for checking on the state of itself or its neighbours

- canGive: can node give entity to its recievers
- canReceive: can node recieve from its givers
- notEmpty: returns bool for if Store is empty
- anyEventsTriggered: does the node have events it still needs to process (used to stops handovers till events are processed) more on events here 
