# Exit
This node represents the conclusion of the process, entities that have arrive here are considered to be finished goods or have had service provided

Exit modifies Node with the goal of always having availability. 
the capacity of the internal SimPy Store is set to Infinity.

Note: SimPy Stores default to Inf capacity but in this library Nodes default to a capacity of One.

Since Exits are not required to process Entities the put method is modified so as not to trigger a process

compare {Exit.put()} vs {Node.put()}