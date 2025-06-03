# {py:mod}`procsimpy.Statistics`

```{py:module} procsimpy.Statistics
```

```{autodoc2-docstring} procsimpy.Statistics
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Statistics <procsimpy.Statistics.Statistics>`
  - ```{autodoc2-docstring} procsimpy.Statistics.Statistics
    :summary:
    ```
````

### API

`````{py:class} Statistics(env: simpy.Environment)
:canonical: procsimpy.Statistics.Statistics

```{autodoc2-docstring} procsimpy.Statistics.Statistics
```

```{rubric} Initialization
```

```{autodoc2-docstring} procsimpy.Statistics.Statistics.__init__
```

````{py:method} createRatios(simTime: simpy.core.SimTime) -> None
:canonical: procsimpy.Statistics.Statistics.createRatios

```{autodoc2-docstring} procsimpy.Statistics.Statistics.createRatios
```

````

````{py:method} startingProcessing() -> None
:canonical: procsimpy.Statistics.Statistics.startingProcessing

```{autodoc2-docstring} procsimpy.Statistics.Statistics.startingProcessing
```

````

````{py:method} finishedProcessing() -> None
:canonical: procsimpy.Statistics.Statistics.finishedProcessing

```{autodoc2-docstring} procsimpy.Statistics.Statistics.finishedProcessing
```

````

````{py:method} receivedEntity(entity: procsimpy.Entity.Entity) -> None
:canonical: procsimpy.Statistics.Statistics.receivedEntity

```{autodoc2-docstring} procsimpy.Statistics.Statistics.receivedEntity
```

````

````{py:method} givenEntity() -> None
:canonical: procsimpy.Statistics.Statistics.givenEntity

```{autodoc2-docstring} procsimpy.Statistics.Statistics.givenEntity
```

````

````{py:method} wentOnShift() -> None
:canonical: procsimpy.Statistics.Statistics.wentOnShift

```{autodoc2-docstring} procsimpy.Statistics.Statistics.wentOnShift
```

````

````{py:method} wentOffShift() -> None
:canonical: procsimpy.Statistics.Statistics.wentOffShift

```{autodoc2-docstring} procsimpy.Statistics.Statistics.wentOffShift
```

````

````{py:method} toDict() -> dict[str, int | float]
:canonical: procsimpy.Statistics.Statistics.toDict

```{autodoc2-docstring} procsimpy.Statistics.Statistics.toDict
```

````

`````
