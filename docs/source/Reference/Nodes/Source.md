###### Source
Goal: Abstract creation of entities

This Node models the Beginning of the Process, the purchase or receiving of raw material or given parts
This Node creates Entities at a rate of the set Distribution and then hands off to the successor node

Is the Standard Entry Point of entities into the model, The Other being defining {Work In Progress} in Experiment Setup

The Default operation of this node works by appending a process responsible for timing of creating Entities and a method that creates entities 

this IntervalEntityGenerator Process simply calls this createEntity function adds it to the SimPy Store then waits a certain amount of time defined by the Arrival Time until the process repeats 