# {py:mod}`hepyaestus.RandomNumberGenerator`

```{py:module} hepyaestus.RandomNumberGenerator
```

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SeedType <hepyaestus.RandomNumberGenerator.SeedType>`
  -
* - {py:obj}`RandomNumberGenerator <hepyaestus.RandomNumberGenerator.RandomNumberGenerator>`
  - ```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.RandomNumberGenerator
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`setSeed <hepyaestus.RandomNumberGenerator.setSeed>`
  - ```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.setSeed
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SEED <hepyaestus.RandomNumberGenerator.SEED>`
  - ```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.SEED
    :summary:
    ```
* - {py:obj}`generators <hepyaestus.RandomNumberGenerator.generators>`
  - ```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.generators
    :summary:
    ```
````

### API

`````{py:class} SeedType(*args, **kwds)
:canonical: hepyaestus.RandomNumberGenerator.SeedType

Bases: {py:obj}`enum.Enum`

````{py:attribute} INT
:canonical: hepyaestus.RandomNumberGenerator.SeedType.INT
:value: >
   'Int'

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.SeedType.INT
```

````

````{py:attribute} OS
:canonical: hepyaestus.RandomNumberGenerator.SeedType.OS
:value: >
   'OS'

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.SeedType.OS
```

````

`````

````{py:data} SEED
:canonical: hepyaestus.RandomNumberGenerator.SEED
:type: int | None
:value: >
   42

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.SEED
```

````

````{py:data} generators
:canonical: hepyaestus.RandomNumberGenerator.generators
:type: list[hepyaestus.RandomNumberGenerator.RandomNumberGenerator]
:value: >
   []

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.generators
```

````

````{py:function} setSeed(seed: int = 42, seedType: hepyaestus.RandomNumberGenerator.SeedType = SeedType.INT) -> None
:canonical: hepyaestus.RandomNumberGenerator.setSeed

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.setSeed
```
````

`````{py:class} RandomNumberGenerator(distribution: hepyaestus.ProbDistribution.ProbDistribution)
:canonical: hepyaestus.RandomNumberGenerator.RandomNumberGenerator

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.RandomNumberGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.RandomNumberGenerator.__init__
```

````{py:method} generateNumber() -> float
:canonical: hepyaestus.RandomNumberGenerator.RandomNumberGenerator.generateNumber

```{autodoc2-docstring} hepyaestus.RandomNumberGenerator.RandomNumberGenerator.generateNumber
```

````

`````
