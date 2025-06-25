###### Source
Goal: Abstract creation of entities

This Node models the Beginning of the Process, the purchase or receiving of raw material or given parts, or the acquisition of a new client 

This is a child of Node and has all the internal components defined {here}

Source has one more process and one more method

createEntity method creates an Entity provided by the item parameter of the constructor (defaults to the Entity class defined by this library)

creates {Entities} at a rate of the set by the arrivalTime Distribution

Is the Standard Entry Point of entities into the model, The Other being defining {Work In Progress} in Experiment Setup

The Default operation of this node works by appending a process responsible for timing of creating Entities and a method that creates entities 

this IntervalEntityGenerator Process simply calls this createEntity function adds it to the SimPy Store then waits a certain amount of time defined by the Arrival Time until the process repeats 

