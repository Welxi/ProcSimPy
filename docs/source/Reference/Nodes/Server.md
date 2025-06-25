###### Server
Server is the place in the model where time is required to complete the "work", e.g. a Machine in a manufacturing experiment

A child of {Node} it is modelled in the same way it just enforces that a processingTime {{Distribution}} is set

While Servers can have many Predecessors or Successors it is recommended to model this with {Queue}s where possible. 