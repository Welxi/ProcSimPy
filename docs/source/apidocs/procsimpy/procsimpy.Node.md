# {py:mod}`procsimpy.Node`

```{py:module} procsimpy.Node
```

```{autodoc2-docstring} procsimpy.Node
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Node <procsimpy.Node.Node>`
  - ```{autodoc2-docstring} procsimpy.Node.Node
    :summary:
    ```
````

### API

`````{py:class} Node(id: str, name: str, *, capacity: int | float = 1, priority: typing.Optional[int] = None, processingTime: typing.Optional[procsimpy.ProbDistribution.ProbDistribution] = None, shift: typing.Optional[procsimpy.ShiftScheduler.Shift] = None)
:canonical: procsimpy.Node.Node

Bases: {py:obj}`procsimpy.Base.Base`

```{autodoc2-docstring} procsimpy.Node.Node
```

```{rubric} Initialization
```

```{autodoc2-docstring} procsimpy.Node.Node.__init__
```

````{py:method} initialize(env: simpy.Environment, line: procsimpy.Line.Line, *, processEntity: typing.Callable[[procsimpy.Node.Node], collections.abc.Generator] = ProcessEntity, processes: typing.Optional[list[typing.Callable[[procsimpy.Node.Node], collections.abc.Generator]]] = None) -> None
:canonical: procsimpy.Node.Node.initialize

```{autodoc2-docstring} procsimpy.Node.Node.initialize
```

````

````{py:method} defineRouting(predecessorList: typing.Optional[list[procsimpy.Node.Node]] = None, successorList: typing.Optional[list[procsimpy.Node.Node]] = None) -> None
:canonical: procsimpy.Node.Node.defineRouting

```{autodoc2-docstring} procsimpy.Node.Node.defineRouting
```

````

````{py:method} get() -> simpy.resources.store.StoreGet
:canonical: procsimpy.Node.Node.get

```{autodoc2-docstring} procsimpy.Node.Node.get
```

````

````{py:method} put(item: procsimpy.Entity.Entity) -> simpy.resources.store.StorePut
:canonical: procsimpy.Node.Node.put

```{autodoc2-docstring} procsimpy.Node.Node.put
```

````

````{py:method} process() -> None
:canonical: procsimpy.Node.Node.process

```{autodoc2-docstring} procsimpy.Node.Node.process
```

````

````{py:method} processingTime() -> simpy.core.SimTime | None
:canonical: procsimpy.Node.Node.processingTime

```{autodoc2-docstring} procsimpy.Node.Node.processingTime
```

````

````{py:method} _getActiveEntity() -> procsimpy.Entity.Entity
:canonical: procsimpy.Node.Node._getActiveEntity

```{autodoc2-docstring} procsimpy.Node.Node._getActiveEntity
```

````

````{py:property} availability
:canonical: procsimpy.Node.Node.availability
:type: int

```{autodoc2-docstring} procsimpy.Node.Node.availability
```

````

````{py:method} createToken() -> procsimpy.AvailabilityToken.AvailabilityToken
:canonical: procsimpy.Node.Node.createToken

```{autodoc2-docstring} procsimpy.Node.Node.createToken
```

````

````{py:method} getToken() -> simpy.resources.store.StoreGet
:canonical: procsimpy.Node.Node.getToken

```{autodoc2-docstring} procsimpy.Node.Node.getToken
```

````

````{py:method} addAvailability(eventType) -> None
:canonical: procsimpy.Node.Node.addAvailability

```{autodoc2-docstring} procsimpy.Node.Node.addAvailability
```

````

````{py:method} fillAvailability() -> None
:canonical: procsimpy.Node.Node.fillAvailability

```{autodoc2-docstring} procsimpy.Node.Node.fillAvailability
```

````

````{py:method} clearAvailability() -> None
:canonical: procsimpy.Node.Node.clearAvailability

```{autodoc2-docstring} procsimpy.Node.Node.clearAvailability
```

````

````{py:method} routeEntity(targets: list[procsimpy.AvailabilityToken.AvailabilityToken]) -> procsimpy.AvailabilityToken.AvailabilityToken
:canonical: procsimpy.Node.Node.routeEntity

```{autodoc2-docstring} procsimpy.Node.Node.routeEntity
```

````

`````
