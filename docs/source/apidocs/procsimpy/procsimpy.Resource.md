# {py:mod}`procsimpy.Resource`

```{py:module} procsimpy.Resource
```

```{autodoc2-docstring} procsimpy.Resource
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ResourceObject <procsimpy.Resource.ResourceObject>`
  -
````

### API

`````{py:class} ResourceObject(id: str, name: str, *, capacity: int = 1)
:canonical: procsimpy.Resource.ResourceObject

Bases: {py:obj}`procsimpy.Base.Base`

````{py:method} initialize(env: simpy.Environment, line: procsimpy.Line.Line) -> None
:canonical: procsimpy.Resource.ResourceObject.initialize

````

````{py:method} request() -> simpy.resources.resource.Request
:canonical: procsimpy.Resource.ResourceObject.request

```{autodoc2-docstring} procsimpy.Resource.ResourceObject.request
```

````

````{py:method} isAvailable() -> bool
:canonical: procsimpy.Resource.ResourceObject.isAvailable

```{autodoc2-docstring} procsimpy.Resource.ResourceObject.isAvailable
```

````

`````
