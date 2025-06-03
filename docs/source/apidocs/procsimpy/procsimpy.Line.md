# {py:mod}`procsimpy.Line`

```{py:module} procsimpy.Line
```

```{autodoc2-docstring} procsimpy.Line
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Line <procsimpy.Line.Line>`
  - ```{autodoc2-docstring} procsimpy.Line.Line
    :summary:
    ```
````

### API

`````{py:class} Line(nodeList: list[procsimpy.Node.Node], *, WIPList: typing.Optional[list[procsimpy.Entity.Entity]] = None, failures: typing.Optional[list[procsimpy.Failure.Failure]] = None, repair: typing.Optional[list[procsimpy.RepairTechnician.RepairTechnician]] = None, routingPriority: typing.Optional[typing.Callable[[list[procsimpy.AvailabilityToken.AvailabilityToken]], procsimpy.AvailabilityToken.AvailabilityToken]] = None)
:canonical: procsimpy.Line.Line

```{autodoc2-docstring} procsimpy.Line.Line
```

```{rubric} Initialization
```

```{autodoc2-docstring} procsimpy.Line.Line.__init__
```

````{py:method} initialize(env: simpy.Environment) -> None
:canonical: procsimpy.Line.Line.initialize

```{autodoc2-docstring} procsimpy.Line.Line.initialize
```

````

````{py:method} setWorkInProgress() -> None
:canonical: procsimpy.Line.Line.setWorkInProgress

```{autodoc2-docstring} procsimpy.Line.Line.setWorkInProgress
```

````

````{py:method} turnTraceingOff() -> None
:canonical: procsimpy.Line.Line.turnTraceingOff

```{autodoc2-docstring} procsimpy.Line.Line.turnTraceingOff
```

````

````{py:method} canTrace(base: procsimpy.Base.Base) -> bool
:canonical: procsimpy.Line.Line.canTrace

```{autodoc2-docstring} procsimpy.Line.Line.canTrace
```

````

````{py:method} filterTrace(node: procsimpy.Node.Node) -> None
:canonical: procsimpy.Line.Line.filterTrace

```{autodoc2-docstring} procsimpy.Line.Line.filterTrace
```

````

````{py:method} partsCreated() -> int
:canonical: procsimpy.Line.Line.partsCreated

```{autodoc2-docstring} procsimpy.Line.Line.partsCreated
```

````

````{py:method} repairRequest(cause) -> simpy.resources.resource.Request
:canonical: procsimpy.Line.Line.repairRequest

```{autodoc2-docstring} procsimpy.Line.Line.repairRequest
```

````

`````
