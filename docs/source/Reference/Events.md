# Events
The way this Library uses [SimPy](https://simpy.readthedocs.io/en/latest/) is through use of their event system.

Events are created for the following purposes
#### Handover
At the end of each simulation cycle each node check with its neighbours to find a connection between a ready predecessor and an available successor. When this connection is identified events trigger to perform a handover

###### Step 1 - canDispose
this node is engaging in the handover with a specific successor 
it creates calls the internal [SimPy Store](https://simpy.readthedocs.io/en/latest/api_reference/simpy.resources.html#module-simpy.resources.store) give method to retrieve an Entity. with this entity it create a new event with the entity as a transmission variable
###### Step 2 isRequested
a percussor node is handing over an Entity. 
this calls the internal [SimPy Store](https://simpy.readthedocs.io/en/latest/api_reference/simpy.resources.html#module-simpy.resources.store) put method to add the entity to the store
#### Setup
Initial Work in Progress is also implement via the event system but that should only occur once at the beginning of each experiment iteration