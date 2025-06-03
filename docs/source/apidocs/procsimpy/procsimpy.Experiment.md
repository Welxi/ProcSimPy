# {py:mod}`procsimpy.Experiment`

```{py:module} procsimpy.Experiment
```

```{autodoc2-docstring} procsimpy.Experiment
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Experiment <procsimpy.Experiment.Experiment>`
  - ```{autodoc2-docstring} procsimpy.Experiment.Experiment
    :summary:
    ```
````

### API

`````{py:class} Experiment(line: procsimpy.Line.Line, seed: int = 42, seedType: procsimpy.RandomNumberGenerator.SeedType = SeedType.INT)
:canonical: procsimpy.Experiment.Experiment

```{autodoc2-docstring} procsimpy.Experiment.Experiment
```

```{rubric} Initialization
```

```{autodoc2-docstring} procsimpy.Experiment.Experiment.__init__
```

````{py:method} run(maxSimTime: float = 100, numberOfReplications: int = 1, *, test: bool = False) -> procsimpy.Results.Results
:canonical: procsimpy.Experiment.Experiment.run

```{autodoc2-docstring} procsimpy.Experiment.Experiment.run
```

````

````{py:method} _runIteration() -> None
:canonical: procsimpy.Experiment.Experiment._runIteration

```{autodoc2-docstring} procsimpy.Experiment.Experiment._runIteration
```

````

`````
