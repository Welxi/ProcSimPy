# {py:mod}`procsimpy.RepairTechnician`

```{py:module} procsimpy.RepairTechnician
```

```{autodoc2-docstring} procsimpy.RepairTechnician
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`RepairTechnician <procsimpy.RepairTechnician.RepairTechnician>`
  - ```{autodoc2-docstring} procsimpy.RepairTechnician.RepairTechnician
    :summary:
    ```
````

### API

`````{py:class} RepairTechnician(id: str, name: str, *, capacity: int = 1)
:canonical: procsimpy.RepairTechnician.RepairTechnician

Bases: {py:obj}`procsimpy.Resource.ResourceObject`

```{autodoc2-docstring} procsimpy.RepairTechnician.RepairTechnician
```

```{rubric} Initialization
```

```{autodoc2-docstring} procsimpy.RepairTechnician.RepairTechnician.__init__
```

````{py:method} filterFailures(failures: list[procsimpy.Failure.Failure]) -> None
:canonical: procsimpy.RepairTechnician.RepairTechnician.filterFailures

```{autodoc2-docstring} procsimpy.RepairTechnician.RepairTechnician.filterFailures
```

````

````{py:method} request(cause) -> simpy.resources.resource.Request
:canonical: procsimpy.RepairTechnician.RepairTechnician.request

```{autodoc2-docstring} procsimpy.RepairTechnician.RepairTechnician.request
```

````

`````
