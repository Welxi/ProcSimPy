# {py:mod}`procsimpy.Source`

```{py:module} procsimpy.Source
```

```{autodoc2-docstring} procsimpy.Source
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Source <procsimpy.Source.Source>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IntervalEntityGenerator <procsimpy.Source.IntervalEntityGenerator>`
  - ```{autodoc2-docstring} procsimpy.Source.IntervalEntityGenerator
    :summary:
    ```
````

### API

`````{py:class} Source(id: str, name: str, *, arrivalTime: procsimpy.ProbDistribution.ProbDistribution, item: type[procsimpy.Entity.Entity] = Entity)
:canonical: procsimpy.Source.Source

Bases: {py:obj}`procsimpy.Node.Node`

````{py:method} initialize(env: simpy.Environment, line: procsimpy.Line.Line, *, processEntity: typing.Callable[[procsimpy.Node.Node], collections.abc.Generator] = ProcessEntity, processes: typing.Optional[list[typing.Callable[[procsimpy.Node.Node], collections.abc.Generator]]] = None) -> None
:canonical: procsimpy.Source.Source.initialize

````

````{py:method} createEntity() -> procsimpy.Entity.Entity
:canonical: procsimpy.Source.Source.createEntity

```{autodoc2-docstring} procsimpy.Source.Source.createEntity
```

````

`````

````{py:function} IntervalEntityGenerator(node: procsimpy.Node.Node) -> collections.abc.Generator
:canonical: procsimpy.Source.IntervalEntityGenerator

```{autodoc2-docstring} procsimpy.Source.IntervalEntityGenerator
```
````
