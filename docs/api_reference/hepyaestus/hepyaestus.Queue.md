# {py:mod}`hepyaestus.Queue`

```{py:module} hepyaestus.Queue
```

```{autodoc2-docstring} hepyaestus.Queue
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Queue <hepyaestus.Queue.Queue>`
  - ```{autodoc2-docstring} hepyaestus.Queue.Queue
    :summary:
    ```
````

### API

`````{py:class} Queue(id: str, name: str, capacity: int = 1, priority: int = 0)
:canonical: hepyaestus.Queue.Queue

Bases: {py:obj}`hepyaestus.StoreNode.StoreNode`

```{autodoc2-docstring} hepyaestus.Queue.Queue
```

```{rubric} Initialization
```

```{autodoc2-docstring} hepyaestus.Queue.Queue.__init__
```

````{py:method} initialize(env: simpy.Environment, line: hepyaestus.Line.Line) -> None
:canonical: hepyaestus.Queue.Queue.initialize

```{autodoc2-docstring} hepyaestus.Queue.Queue.initialize
```

````

````{py:method} run() -> collections.abc.Generator
:canonical: hepyaestus.Queue.Queue.run

```{autodoc2-docstring} hepyaestus.Queue.Queue.run
```

````

`````
