# Queue
Queue is a child of {Node} without a processing time, if "work" is required by the node a {Server} is the recommended Node

When using this in a model it should be one or both of two reasons
- a buffer for capacity of a successor node
- a decision point for which successor should receive at any given moment  

Any Node may have Multiple Successors or Predecessors but this node is the recommended tool for when routing considerations are in play

Note: Queue have their own capacity and care should used to ensure that Bottlenecks are not shifted by placement of extra Queue nodes

Consider the case of two Servers in Series with the default capacity of One, with different Processing Times. The later Server can create a blocking effect on the former in the absence of a Queue. By adding a Queue a buffer is formed allowing the former to Operate until both the Itself and the Queue is full. Which models the system of interest will involve Experiment Design and an understanding of your requirements

