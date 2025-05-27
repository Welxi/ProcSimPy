# {py:mod}`hepyaestus.Machine`

```{py:module} hepyaestus.Machine
```

```{autodoc2-docstring} hepyaestus.Machine
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Machine <hepyaestus.Machine.Machine>`
  - ```{autodoc2-docstring} hepyaestus.Machine.Machine
    :summary:
    ```
````

### API

`````{py:class} Machine(id: str, name: str, processingTime: hepyaestus.ProbDistribution.ProbDistribution, capacity: int = 1, priority: int = 0)
:canonical: hepyaestus.Machine.Machine

Bases: {py:obj}`hepyaestus.StoreNode.StoreNode`

```{autodoc2-docstring} hepyaestus.Machine.Machine
```

```{rubric} Initialization
```

```{autodoc2-docstring} hepyaestus.Machine.Machine.__init__
```

````{py:method} initialize(env: simpy.Environment, line: hepyaestus.Line.Line) -> None
:canonical: hepyaestus.Machine.Machine.initialize

```{autodoc2-docstring} hepyaestus.Machine.Machine.initialize
```

````

````{py:method} run() -> collections.abc.Generator
:canonical: hepyaestus.Machine.Machine.run

```{autodoc2-docstring} hepyaestus.Machine.Machine.run
```

````

````{py:method} calculateProcessingTime() -> float
:canonical: hepyaestus.Machine.Machine.calculateProcessingTime

```{autodoc2-docstring} hepyaestus.Machine.Machine.calculateProcessingTime
```

````

`````
