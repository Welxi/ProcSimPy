# {py:mod}`hepyaestus.Resource`

```{py:module} hepyaestus.Resource
```

```{autodoc2-docstring} hepyaestus.Resource
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ResourceObject <hepyaestus.Resource.ResourceObject>`
  - ```{autodoc2-docstring} hepyaestus.Resource.ResourceObject
    :summary:
    ```
````

### API

`````{py:class} ResourceObject(id: str, name: str, capacity: int = 1)
:canonical: hepyaestus.Resource.ResourceObject

Bases: {py:obj}`hepyaestus.Base.BaseObject`

```{autodoc2-docstring} hepyaestus.Resource.ResourceObject
```

```{rubric} Initialization
```

```{autodoc2-docstring} hepyaestus.Resource.ResourceObject.__init__
```

````{py:method} initialize(env: simpy.Environment, line: hepyaestus.Line.Line) -> None
:canonical: hepyaestus.Resource.ResourceObject.initialize

```{autodoc2-docstring} hepyaestus.Resource.ResourceObject.initialize
```

````

````{py:method} checkAvailable() -> bool
:canonical: hepyaestus.Resource.ResourceObject.checkAvailable

```{autodoc2-docstring} hepyaestus.Resource.ResourceObject.checkAvailable
```

````

````{py:method} request() -> simpy.resources.resource.Request
:canonical: hepyaestus.Resource.ResourceObject.request

```{autodoc2-docstring} hepyaestus.Resource.ResourceObject.request
```

````

````{py:method} release()
:canonical: hepyaestus.Resource.ResourceObject.release

```{autodoc2-docstring} hepyaestus.Resource.ResourceObject.release
```

````

````{py:property} assignedTo
:canonical: hepyaestus.Resource.ResourceObject.assignedTo

```{autodoc2-docstring} hepyaestus.Resource.ResourceObject.assignedTo
```

````

`````
