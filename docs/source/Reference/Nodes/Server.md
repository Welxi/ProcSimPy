###### Server
Goal: Models time taken to achieve step of process
a processing node that may require resources to function ie operator

Server is the place in the model where "work" is done, e.g. a Machine in a manufacturing experiment

work is modelled by providing a processingTime given by the provided {ProbDistrubution} class. Many common Probability Distributions are provided by this library but it can be extended if they do not meet your needs. A specific Step functions modelling your component of interested would be one example that could be extended, or a sampling of already collected data.

while Servers can have many Predecessors or Successors it is recommended to model this with {Queue}s where possible. 