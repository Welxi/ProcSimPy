# {py:mod}`hepyaestus.ProbDistribution`

```{py:module} hepyaestus.ProbDistribution
```

```{autodoc2-docstring} hepyaestus.ProbDistribution
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DistributionType <hepyaestus.ProbDistribution.DistributionType>`
  -
* - {py:obj}`ProbDistribution <hepyaestus.ProbDistribution.ProbDistribution>`
  -
* - {py:obj}`FixedDistribution <hepyaestus.ProbDistribution.FixedDistribution>`
  -
* - {py:obj}`GaussianDistribution <hepyaestus.ProbDistribution.GaussianDistribution>`
  -
* - {py:obj}`ExpDistribution <hepyaestus.ProbDistribution.ExpDistribution>`
  -
* - {py:obj}`GammaDistribution <hepyaestus.ProbDistribution.GammaDistribution>`
  -
* - {py:obj}`LogisticDistribution <hepyaestus.ProbDistribution.LogisticDistribution>`
  -
* - {py:obj}`ErlangDistribution <hepyaestus.ProbDistribution.ErlangDistribution>`
  -
* - {py:obj}`GeometricDistribution <hepyaestus.ProbDistribution.GeometricDistribution>`
  -
* - {py:obj}`LognormalDistribution <hepyaestus.ProbDistribution.LognormalDistribution>`
  -
* - {py:obj}`WeibullDistribution <hepyaestus.ProbDistribution.WeibullDistribution>`
  -
* - {py:obj}`CauchyDistribution <hepyaestus.ProbDistribution.CauchyDistribution>`
  -
* - {py:obj}`TriangularDistribution <hepyaestus.ProbDistribution.TriangularDistribution>`
  -
````

### API

`````{py:class} DistributionType(*args, **kwds)
:canonical: hepyaestus.ProbDistribution.DistributionType

Bases: {py:obj}`enum.Enum`

````{py:attribute} FIXED
:canonical: hepyaestus.ProbDistribution.DistributionType.FIXED
:value: >
   'Fixed'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.FIXED
```

````

````{py:attribute} GAUSSIAN
:canonical: hepyaestus.ProbDistribution.DistributionType.GAUSSIAN
:value: >
   'Gaussian'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.GAUSSIAN
```

````

````{py:attribute} EXP
:canonical: hepyaestus.ProbDistribution.DistributionType.EXP
:value: >
   'Exp'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.EXP
```

````

````{py:attribute} GAMMA
:canonical: hepyaestus.ProbDistribution.DistributionType.GAMMA
:value: >
   'Gamma'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.GAMMA
```

````

````{py:attribute} LOGISTIC
:canonical: hepyaestus.ProbDistribution.DistributionType.LOGISTIC
:value: >
   'Logistic'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.LOGISTIC
```

````

````{py:attribute} ERLANG
:canonical: hepyaestus.ProbDistribution.DistributionType.ERLANG
:value: >
   'Erlang'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.ERLANG
```

````

````{py:attribute} GEOMETRIC
:canonical: hepyaestus.ProbDistribution.DistributionType.GEOMETRIC
:value: >
   'Geometric'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.GEOMETRIC
```

````

````{py:attribute} LOGNORMAL
:canonical: hepyaestus.ProbDistribution.DistributionType.LOGNORMAL
:value: >
   'Lognormal'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.LOGNORMAL
```

````

````{py:attribute} WEIBULL
:canonical: hepyaestus.ProbDistribution.DistributionType.WEIBULL
:value: >
   'Weibull'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.WEIBULL
```

````

````{py:attribute} CAUCHY
:canonical: hepyaestus.ProbDistribution.DistributionType.CAUCHY
:value: >
   'Cauchy'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.CAUCHY
```

````

````{py:attribute} TRIANGULAR
:canonical: hepyaestus.ProbDistribution.DistributionType.TRIANGULAR
:value: >
   'Triangular'

```{autodoc2-docstring} hepyaestus.ProbDistribution.DistributionType.TRIANGULAR
```

````

`````

`````{py:class} ProbDistribution(distributionType: hepyaestus.ProbDistribution.DistributionType)
:canonical: hepyaestus.ProbDistribution.ProbDistribution

Bases: {py:obj}`abc.ABC`

````{py:method} distributionFunction(RanNumGenerator) -> float
:canonical: hepyaestus.ProbDistribution.ProbDistribution.distributionFunction
:abstractmethod:

```{autodoc2-docstring} hepyaestus.ProbDistribution.ProbDistribution.distributionFunction
```

````

`````

`````{py:class} FixedDistribution(mean: float)
:canonical: hepyaestus.ProbDistribution.FixedDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: hepyaestus.ProbDistribution.FixedDistribution.distributionFunction

````

`````

`````{py:class} GaussianDistribution(mean: float, stdev: float, min: float, max: float)
:canonical: hepyaestus.ProbDistribution.GaussianDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: hepyaestus.ProbDistribution.GaussianDistribution.distributionFunction

````

`````

`````{py:class} ExpDistribution(mean: float)
:canonical: hepyaestus.ProbDistribution.ExpDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator) -> float
:canonical: hepyaestus.ProbDistribution.ExpDistribution.distributionFunction

````

`````

`````{py:class} GammaDistribution(alpha: float, beta: float, shape: float, rate: float)
:canonical: hepyaestus.ProbDistribution.GammaDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: hepyaestus.ProbDistribution.GammaDistribution.distributionFunction

````

`````

`````{py:class} LogisticDistribution(mean: float, scale: float)
:canonical: hepyaestus.ProbDistribution.LogisticDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: hepyaestus.ProbDistribution.LogisticDistribution.distributionFunction

````

`````

`````{py:class} ErlangDistribution(alpha: float, beta: float, shape: float, rate: float)
:canonical: hepyaestus.ProbDistribution.ErlangDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: hepyaestus.ProbDistribution.ErlangDistribution.distributionFunction

````

`````

`````{py:class} GeometricDistribution(probability: float)
:canonical: hepyaestus.ProbDistribution.GeometricDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator) -> float
:canonical: hepyaestus.ProbDistribution.GeometricDistribution.distributionFunction

````

`````

`````{py:class} LognormalDistribution(logmean: float, logsd: float)
:canonical: hepyaestus.ProbDistribution.LognormalDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: hepyaestus.ProbDistribution.LognormalDistribution.distributionFunction

````

`````

`````{py:class} WeibullDistribution(scale: float, shape: float)
:canonical: hepyaestus.ProbDistribution.WeibullDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: hepyaestus.ProbDistribution.WeibullDistribution.distributionFunction

````

`````

`````{py:class} CauchyDistribution(location: float, scale: float)
:canonical: hepyaestus.ProbDistribution.CauchyDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator) -> float
:canonical: hepyaestus.ProbDistribution.CauchyDistribution.distributionFunction

````

`````

`````{py:class} TriangularDistribution(min: float, mean: float, max: float)
:canonical: hepyaestus.ProbDistribution.TriangularDistribution

Bases: {py:obj}`hepyaestus.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: hepyaestus.ProbDistribution.TriangularDistribution.distributionFunction

````

`````
