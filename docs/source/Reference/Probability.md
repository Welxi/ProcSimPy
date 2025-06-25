#### Probability
Each variable in the model is shared the same Random Number Generator, this is to avoid the large effect of Initial seed values on the experiment, due to this the distribution of the variable is provided by functions that take the random number generator as an argument and map that onto the required distribution. 

Common Distributions are provided by the library, but more nuanced distributions should be provided by the user. 
###### Distribution Functions
Fixed
Gaussian
Exponential
Gamma
Logistic
Erlang
Lognormal
Weibull
Triangular

 Many common Probability Distributions are provided by this library but it can be extended if they do not meet your needs. A specific Step functions modelling your component of interested would be one example that could be extended, or a sampling of already collected data.