# {py:mod}`procsimpy.Entity`

```{py:module} procsimpy.Entity
```

```{autodoc2-docstring} procsimpy.Entity
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Entity <procsimpy.Entity.Entity>`
  -
````

### API

`````{py:class} Entity(id: str, name: str, *, startingNode: typing.Optional[procsimpy.Node.Node] = None, remainingProcessingTime: typing.Optional[procsimpy.ProbDistribution.ProbDistribution] = None)
:canonical: procsimpy.Entity.Entity

Bases: {py:obj}`procsimpy.Base.Base`

````{py:attribute} type
:canonical: procsimpy.Entity.Entity.type
:value: >
   'Entity'

```{autodoc2-docstring} procsimpy.Entity.Entity.type
```

````

````{py:method} initialize(env: simpy.Environment, line: procsimpy.Line.Line, *, currentNode: procsimpy.Node.Node) -> None
:canonical: procsimpy.Entity.Entity.initialize

```{autodoc2-docstring} procsimpy.Entity.Entity.initialize
```

````

````{py:method} updateStation(station: procsimpy.Node.Node) -> None
:canonical: procsimpy.Entity.Entity.updateStation

```{autodoc2-docstring} procsimpy.Entity.Entity.updateStation
```

````

`````
