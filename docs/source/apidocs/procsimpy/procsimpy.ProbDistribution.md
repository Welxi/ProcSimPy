# {py:mod}`procsimpy.ProbDistribution`

```{py:module} procsimpy.ProbDistribution
```

```{autodoc2-docstring} procsimpy.ProbDistribution
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DistributionType <procsimpy.ProbDistribution.DistributionType>`
  -
* - {py:obj}`ProbDistribution <procsimpy.ProbDistribution.ProbDistribution>`
  -
* - {py:obj}`FixedDistribution <procsimpy.ProbDistribution.FixedDistribution>`
  -
* - {py:obj}`GaussianDistribution <procsimpy.ProbDistribution.GaussianDistribution>`
  -
* - {py:obj}`ExpDistribution <procsimpy.ProbDistribution.ExpDistribution>`
  -
* - {py:obj}`GammaDistribution <procsimpy.ProbDistribution.GammaDistribution>`
  -
* - {py:obj}`LogisticDistribution <procsimpy.ProbDistribution.LogisticDistribution>`
  -
* - {py:obj}`ErlangDistribution <procsimpy.ProbDistribution.ErlangDistribution>`
  -
* - {py:obj}`GeometricDistribution <procsimpy.ProbDistribution.GeometricDistribution>`
  -
* - {py:obj}`LognormalDistribution <procsimpy.ProbDistribution.LognormalDistribution>`
  -
* - {py:obj}`WeibullDistribution <procsimpy.ProbDistribution.WeibullDistribution>`
  -
* - {py:obj}`CauchyDistribution <procsimpy.ProbDistribution.CauchyDistribution>`
  -
* - {py:obj}`TriangularDistribution <procsimpy.ProbDistribution.TriangularDistribution>`
  -
````

### API

`````{py:class} DistributionType(*args, **kwds)
:canonical: procsimpy.ProbDistribution.DistributionType

Bases: {py:obj}`enum.Enum`

````{py:attribute} FIXED
:canonical: procsimpy.ProbDistribution.DistributionType.FIXED
:value: >
   'Fixed'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.FIXED
```

````

````{py:attribute} NORMAL
:canonical: procsimpy.ProbDistribution.DistributionType.NORMAL
:value: >
   'Normal'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.NORMAL
```

````

````{py:attribute} EXP
:canonical: procsimpy.ProbDistribution.DistributionType.EXP
:value: >
   'Exp'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.EXP
```

````

````{py:attribute} GAMMA
:canonical: procsimpy.ProbDistribution.DistributionType.GAMMA
:value: >
   'Gamma'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.GAMMA
```

````

````{py:attribute} LOGISTIC
:canonical: procsimpy.ProbDistribution.DistributionType.LOGISTIC
:value: >
   'Logistic'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.LOGISTIC
```

````

````{py:attribute} ERLANG
:canonical: procsimpy.ProbDistribution.DistributionType.ERLANG
:value: >
   'Erlang'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.ERLANG
```

````

````{py:attribute} GEOMETRIC
:canonical: procsimpy.ProbDistribution.DistributionType.GEOMETRIC
:value: >
   'Geometric'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.GEOMETRIC
```

````

````{py:attribute} LOGNORMAL
:canonical: procsimpy.ProbDistribution.DistributionType.LOGNORMAL
:value: >
   'Lognormal'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.LOGNORMAL
```

````

````{py:attribute} WEIBULL
:canonical: procsimpy.ProbDistribution.DistributionType.WEIBULL
:value: >
   'Weibull'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.WEIBULL
```

````

````{py:attribute} CAUCHY
:canonical: procsimpy.ProbDistribution.DistributionType.CAUCHY
:value: >
   'Cauchy'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.CAUCHY
```

````

````{py:attribute} TRIANGULAR
:canonical: procsimpy.ProbDistribution.DistributionType.TRIANGULAR
:value: >
   'Triangular'

```{autodoc2-docstring} procsimpy.ProbDistribution.DistributionType.TRIANGULAR
```

````

`````

`````{py:class} ProbDistribution(distributionType: procsimpy.ProbDistribution.DistributionType)
:canonical: procsimpy.ProbDistribution.ProbDistribution

Bases: {py:obj}`abc.ABC`

````{py:method} distributionFunction(RanNumGenerator) -> float
:canonical: procsimpy.ProbDistribution.ProbDistribution.distributionFunction
:abstractmethod:

```{autodoc2-docstring} procsimpy.ProbDistribution.ProbDistribution.distributionFunction
```

````

`````

`````{py:class} FixedDistribution(mean: float)
:canonical: procsimpy.ProbDistribution.FixedDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: procsimpy.ProbDistribution.FixedDistribution.distributionFunction

````

`````

`````{py:class} GaussianDistribution(mean: float, stdev: float, min: float, max: float)
:canonical: procsimpy.ProbDistribution.GaussianDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: procsimpy.ProbDistribution.GaussianDistribution.distributionFunction

````

`````

`````{py:class} ExpDistribution(mean: float)
:canonical: procsimpy.ProbDistribution.ExpDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator) -> float
:canonical: procsimpy.ProbDistribution.ExpDistribution.distributionFunction

````

`````

`````{py:class} GammaDistribution(alpha: float, beta: float, shape: float, rate: float)
:canonical: procsimpy.ProbDistribution.GammaDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: procsimpy.ProbDistribution.GammaDistribution.distributionFunction

````

`````

`````{py:class} LogisticDistribution(mean: float, scale: float)
:canonical: procsimpy.ProbDistribution.LogisticDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: procsimpy.ProbDistribution.LogisticDistribution.distributionFunction

````

`````

`````{py:class} ErlangDistribution(alpha: float, beta: float, shape: float, rate: float)
:canonical: procsimpy.ProbDistribution.ErlangDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: procsimpy.ProbDistribution.ErlangDistribution.distributionFunction

````

`````

`````{py:class} GeometricDistribution(probability: float)
:canonical: procsimpy.ProbDistribution.GeometricDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator) -> float
:canonical: procsimpy.ProbDistribution.GeometricDistribution.distributionFunction

````

`````

`````{py:class} LognormalDistribution(logmean: float, logsd: float)
:canonical: procsimpy.ProbDistribution.LognormalDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: procsimpy.ProbDistribution.LognormalDistribution.distributionFunction

````

`````

`````{py:class} WeibullDistribution(scale: float, shape: float)
:canonical: procsimpy.ProbDistribution.WeibullDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: procsimpy.ProbDistribution.WeibullDistribution.distributionFunction

````

`````

`````{py:class} CauchyDistribution(location: float, scale: float)
:canonical: procsimpy.ProbDistribution.CauchyDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator) -> float
:canonical: procsimpy.ProbDistribution.CauchyDistribution.distributionFunction

````

`````

`````{py:class} TriangularDistribution(min: float, mean: float, max: float)
:canonical: procsimpy.ProbDistribution.TriangularDistribution

Bases: {py:obj}`procsimpy.ProbDistribution.ProbDistribution`

````{py:method} distributionFunction(RanNumGenerator: random.Random) -> float
:canonical: procsimpy.ProbDistribution.TriangularDistribution.distributionFunction

````

`````
