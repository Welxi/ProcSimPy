# {py:mod}`procsimpy.RandomNumberGenerator`

```{py:module} procsimpy.RandomNumberGenerator
```

```{autodoc2-docstring} procsimpy.RandomNumberGenerator
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SeedType <procsimpy.RandomNumberGenerator.SeedType>`
  -
* - {py:obj}`RandomNumberGenerator <procsimpy.RandomNumberGenerator.RandomNumberGenerator>`
  - ```{autodoc2-docstring} procsimpy.RandomNumberGenerator.RandomNumberGenerator
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`setSeed <procsimpy.RandomNumberGenerator.setSeed>`
  - ```{autodoc2-docstring} procsimpy.RandomNumberGenerator.setSeed
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SEED <procsimpy.RandomNumberGenerator.SEED>`
  - ```{autodoc2-docstring} procsimpy.RandomNumberGenerator.SEED
    :summary:
    ```
* - {py:obj}`generators <procsimpy.RandomNumberGenerator.generators>`
  - ```{autodoc2-docstring} procsimpy.RandomNumberGenerator.generators
    :summary:
    ```
````

### API

`````{py:class} SeedType(*args, **kwds)
:canonical: procsimpy.RandomNumberGenerator.SeedType

Bases: {py:obj}`enum.Enum`

````{py:attribute} INT
:canonical: procsimpy.RandomNumberGenerator.SeedType.INT
:value: >
   'Int'

```{autodoc2-docstring} procsimpy.RandomNumberGenerator.SeedType.INT
```

````

````{py:attribute} OS
:canonical: procsimpy.RandomNumberGenerator.SeedType.OS
:value: >
   'OS'

```{autodoc2-docstring} procsimpy.RandomNumberGenerator.SeedType.OS
```

````

`````

````{py:data} SEED
:canonical: procsimpy.RandomNumberGenerator.SEED
:type: int | None
:value: >
   42

```{autodoc2-docstring} procsimpy.RandomNumberGenerator.SEED
```

````

````{py:data} generators
:canonical: procsimpy.RandomNumberGenerator.generators
:type: list[procsimpy.RandomNumberGenerator.RandomNumberGenerator]
:value: >
   []

```{autodoc2-docstring} procsimpy.RandomNumberGenerator.generators
```

````

````{py:function} setSeed(seed: int = 42, seedType: procsimpy.RandomNumberGenerator.SeedType = SeedType.INT) -> None
:canonical: procsimpy.RandomNumberGenerator.setSeed

```{autodoc2-docstring} procsimpy.RandomNumberGenerator.setSeed
```
````

`````{py:class} RandomNumberGenerator(distribution: procsimpy.ProbDistribution.ProbDistribution)
:canonical: procsimpy.RandomNumberGenerator.RandomNumberGenerator

```{autodoc2-docstring} procsimpy.RandomNumberGenerator.RandomNumberGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} procsimpy.RandomNumberGenerator.RandomNumberGenerator.__init__
```

````{py:method} generateNumber() -> simpy.core.SimTime
:canonical: procsimpy.RandomNumberGenerator.RandomNumberGenerator.generateNumber

```{autodoc2-docstring} procsimpy.RandomNumberGenerator.RandomNumberGenerator.generateNumber
```

````

`````
