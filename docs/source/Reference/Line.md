## Line
Note: Am not happy with current name, suggestions are welcome - short for Manufacturing line  

The Line Represents the series of Process Steps as a whole, is the repository of common resources like Repair Technicians to resolve failures. It is also the middleware between experiments and nodes so it tell the nodes if they can output a trace or not

this is in control of the world state and is modules learn about the world in which they exist (other than their direct neighbours which may be defined by user or context or router decisions)

when and object needs a resource and does not have a linked router or similar it requests one from the line

this is one way to set experiment default or standard operating procedures.

Line is responsible for the setup of nodes at the beginning of each experiment 