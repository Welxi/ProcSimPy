# Entity
Entity is the abstraction for the part the process is acting on, a product being manufactured or the client of a service. 

Due to the many processes require for modelling the {Nodes} much of the state of the Entity is stored by itself and updated by processes of the {Node}

States an Entity can be in:
Initialized: EntityStatus.INIT
Arrived: EntityStatus.ARRIVED
Processing: EntityStatus.PROCESSING
Processed: EntityStatus.PROCESSED
Paused: EntityStatus.PAUSED
Transit: EntityStatus.TRANSIT
Scrapped: EntityStatus.SCRAPPED

Initialized is for when the Entity has just been created and has not become involved in the experiment yet. 

Arrived state is triggered when the UpdateStation method has been called. This method is called by the Node Put method.

Processing and Processed are triggered by the Process Entity Process within Node

Paused is for when an Entity has had its Processing interrupted by a Failure or Shift Change and 

Transit is triggered by the Handover process when it removes the entity for its currentNode and passed it to the next node.

Then updateStation is call on the resolution of the Put request starting the cycle over 