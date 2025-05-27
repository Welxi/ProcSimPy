# {py:mod}`hepyaestus.Source`

```{py:module} hepyaestus.Source
```

```{autodoc2-docstring} hepyaestus.Source
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EntityGenerator <hepyaestus.Source.EntityGenerator>`
  - ```{autodoc2-docstring} hepyaestus.Source.EntityGenerator
    :summary:
    ```
* - {py:obj}`Source <hepyaestus.Source.Source>`
  - ```{autodoc2-docstring} hepyaestus.Source.Source
    :summary:
    ```
````

### API

`````{py:class} EntityGenerator(source: hepyaestus.Source.Source, env: simpy.Environment, line: hepyaestus.Line.Line)
:canonical: hepyaestus.Source.EntityGenerator

```{autodoc2-docstring} hepyaestus.Source.EntityGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} hepyaestus.Source.EntityGenerator.__init__
```

````{py:method} run() -> collections.abc.Generator
:canonical: hepyaestus.Source.EntityGenerator.run

```{autodoc2-docstring} hepyaestus.Source.EntityGenerator.run
```

````

`````

`````{py:class} Source(id: str, name: str, interArrivalTime: hepyaestus.ProbDistribution.ProbDistribution, entity: typing.Optional[type[hepyaestus.Entity.Entity]] = None, priority: int = 0)
:canonical: hepyaestus.Source.Source

Bases: {py:obj}`hepyaestus.StoreNode.StoreNode`

```{autodoc2-docstring} hepyaestus.Source.Source
```

```{rubric} Initialization
```

```{autodoc2-docstring} hepyaestus.Source.Source.__init__
```

````{py:method} initialize(env: simpy.Environment, line: hepyaestus.Line.Line) -> None
:canonical: hepyaestus.Source.Source.initialize

```{autodoc2-docstring} hepyaestus.Source.Source.initialize
```

````

````{py:method} run() -> collections.abc.Generator
:canonical: hepyaestus.Source.Source.run

```{autodoc2-docstring} hepyaestus.Source.Source.run
```

````

````{py:method} createEntity()
:canonical: hepyaestus.Source.Source.createEntity

```{autodoc2-docstring} hepyaestus.Source.Source.createEntity
```

````

````{py:method} calculateInterArrivalTime() -> float
:canonical: hepyaestus.Source.Source.calculateInterArrivalTime

```{autodoc2-docstring} hepyaestus.Source.Source.calculateInterArrivalTime
```

````

`````
