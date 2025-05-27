# {py:mod}`hepyaestus.Interruption`

```{py:module} hepyaestus.Interruption
```

```{autodoc2-docstring} hepyaestus.Interruption
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Interruption <hepyaestus.Interruption.Interruption>`
  -
````

### API

`````{py:class} Interruption(id: str, name: str, victim: hepyaestus.StoreNode.StoreNode)
:canonical: hepyaestus.Interruption.Interruption

Bases: {py:obj}`hepyaestus.Base.BaseObject`, {py:obj}`abc.ABC`

````{py:method} initialize(env: simpy.Environment, line: hepyaestus.Line.Line) -> None
:canonical: hepyaestus.Interruption.Interruption.initialize

```{autodoc2-docstring} hepyaestus.Interruption.Interruption.initialize
```

````

````{py:method} run() -> collections.abc.Generator
:canonical: hepyaestus.Interruption.Interruption.run
:abstractmethod:

```{autodoc2-docstring} hepyaestus.Interruption.Interruption.run
```

````

````{py:method} interrupt() -> None
:canonical: hepyaestus.Interruption.Interruption.interrupt

```{autodoc2-docstring} hepyaestus.Interruption.Interruption.interrupt
```

````

````{py:method} reactivate() -> None
:canonical: hepyaestus.Interruption.Interruption.reactivate

```{autodoc2-docstring} hepyaestus.Interruption.Interruption.reactivate
```

````

`````
