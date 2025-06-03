# {py:mod}`procsimpy.Failure`

```{py:module} procsimpy.Failure
```

```{autodoc2-docstring} procsimpy.Failure
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Failure <procsimpy.Failure.Failure>`
  -
````

### API

`````{py:class} Failure(id: str, name: str, *, victim: procsimpy.Node.Node, TTF: procsimpy.ProbDistribution.ProbDistribution, TTR: procsimpy.ProbDistribution.ProbDistribution)
:canonical: procsimpy.Failure.Failure

Bases: {py:obj}`procsimpy.Base.Base`

````{py:method} initialize(env: simpy.Environment, line: procsimpy.Line.Line) -> None
:canonical: procsimpy.Failure.Failure.initialize

````

````{py:method} run() -> collections.abc.Generator
:canonical: procsimpy.Failure.Failure.run

```{autodoc2-docstring} procsimpy.Failure.Failure.run
```

````

`````
