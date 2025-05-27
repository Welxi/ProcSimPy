# {py:mod}`hepyaestus.Statistics`

```{py:module} hepyaestus.Statistics
```

```{autodoc2-docstring} hepyaestus.Statistics
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Statistics <hepyaestus.Statistics.Statistics>`
  - ```{autodoc2-docstring} hepyaestus.Statistics.Statistics
    :summary:
    ```
````

### API

`````{py:class} Statistics(env: simpy.Environment, line: hepyaestus.Line)
:canonical: hepyaestus.Statistics.Statistics

```{autodoc2-docstring} hepyaestus.Statistics.Statistics
```

```{rubric} Initialization
```

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.__init__
```

````{py:method} createRatios(simTime: float) -> None
:canonical: hepyaestus.Statistics.Statistics.createRatios

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.createRatios
```

````

````{py:method} startingProcessing() -> None
:canonical: hepyaestus.Statistics.Statistics.startingProcessing

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.startingProcessing
```

````

````{py:method} finishedProcessing() -> None
:canonical: hepyaestus.Statistics.Statistics.finishedProcessing

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.finishedProcessing
```

````

````{py:method} receivedEntity(entity: hepyaestus.Entity.Entity) -> None
:canonical: hepyaestus.Statistics.Statistics.receivedEntity

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.receivedEntity
```

````

````{py:method} givenEntity(entity: hepyaestus.Entity.Entity) -> None
:canonical: hepyaestus.Statistics.Statistics.givenEntity

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.givenEntity
```

````

````{py:method} wentOnShift() -> None
:canonical: hepyaestus.Statistics.Statistics.wentOnShift

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.wentOnShift
```

````

````{py:method} wentOffShift() -> None
:canonical: hepyaestus.Statistics.Statistics.wentOffShift

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.wentOffShift
```

````

````{py:method} toDict() -> dict[str, int | float]
:canonical: hepyaestus.Statistics.Statistics.toDict

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.toDict
```

````

````{py:method} lastEvent() -> float
:canonical: hepyaestus.Statistics.Statistics.lastEvent

```{autodoc2-docstring} hepyaestus.Statistics.Statistics.lastEvent
```

````

`````
