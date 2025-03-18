# {py:mod}`hepyaestus.Entity`

```{py:module} hepyaestus.Entity
```

```{autodoc2-docstring} hepyaestus.Entity
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Entity <hepyaestus.Entity.Entity>`
  - ```{autodoc2-docstring} hepyaestus.Entity.Entity
    :summary:
    ```
````

### API

`````{py:class} Entity(id: str, name: str, startingStation: typing.Optional[hepyaestus.StoreNode.StoreNode] = None, remainingProcessingTime: typing.Optional[hepyaestus.ProbDistribution.ProbDistribution] = None)
:canonical: hepyaestus.Entity.Entity

Bases: {py:obj}`hepyaestus.Base.BaseObject`

```{autodoc2-docstring} hepyaestus.Entity.Entity
```

```{rubric} Initialization
```

```{autodoc2-docstring} hepyaestus.Entity.Entity.__init__
```

````{py:attribute} type
:canonical: hepyaestus.Entity.Entity.type
:value: >
   'Entity'

```{autodoc2-docstring} hepyaestus.Entity.Entity.type
```

````

````{py:method} initialize(env: simpy.Environment, line: hepyaestus.Line.Line, currentStation: typing.Optional[hepyaestus.StoreNode.StoreNode] = None) -> None
:canonical: hepyaestus.Entity.Entity.initialize

```{autodoc2-docstring} hepyaestus.Entity.Entity.initialize
```

````

````{py:method} updateStation(station: hepyaestus.StoreNode.StoreNode) -> None
:canonical: hepyaestus.Entity.Entity.updateStation

```{autodoc2-docstring} hepyaestus.Entity.Entity.updateStation
```

````

`````
