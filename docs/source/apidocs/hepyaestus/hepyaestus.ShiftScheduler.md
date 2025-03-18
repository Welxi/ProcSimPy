# {py:mod}`hepyaestus.ShiftScheduler`

```{py:module} hepyaestus.ShiftScheduler
```

```{autodoc2-docstring} hepyaestus.ShiftScheduler
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`StoreShiftScheduler <hepyaestus.ShiftScheduler.StoreShiftScheduler>`
  -
* - {py:obj}`Shift <hepyaestus.ShiftScheduler.Shift>`
  -
* - {py:obj}`ShiftPattern <hepyaestus.ShiftScheduler.ShiftPattern>`
  -
* - {py:obj}`ShiftSchedule <hepyaestus.ShiftScheduler.ShiftSchedule>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ShiftBuilder <hepyaestus.ShiftScheduler.ShiftBuilder>`
  - ```{autodoc2-docstring} hepyaestus.ShiftScheduler.ShiftBuilder
    :summary:
    ```
* - {py:obj}`vaildateSchedule <hepyaestus.ShiftScheduler.vaildateSchedule>`
  - ```{autodoc2-docstring} hepyaestus.ShiftScheduler.vaildateSchedule
    :summary:
    ```
````

### API

`````{py:class} StoreShiftScheduler(id: str, name: str, victim: hepyaestus.StoreNode.StoreNode)
:canonical: hepyaestus.ShiftScheduler.StoreShiftScheduler

Bases: {py:obj}`hepyaestus.Interruption.Interruption`

````{py:method} initialize(env: simpy.Environment, line: hepyaestus.Line.Line) -> None
:canonical: hepyaestus.ShiftScheduler.StoreShiftScheduler.initialize

```{autodoc2-docstring} hepyaestus.ShiftScheduler.StoreShiftScheduler.initialize
```

````

````{py:method} run() -> collections.abc.Generator
:canonical: hepyaestus.ShiftScheduler.StoreShiftScheduler.run

```{autodoc2-docstring} hepyaestus.ShiftScheduler.StoreShiftScheduler.run
```

````

`````

````{py:function} ShiftBuilder(pattern: typing.Optional[tuple[float, float]], schedule: typing.Optional[list[tuple[float, float]]]) -> ShiftPattern | ShiftSchedule
:canonical: hepyaestus.ShiftScheduler.ShiftBuilder

```{autodoc2-docstring} hepyaestus.ShiftScheduler.ShiftBuilder
```
````

`````{py:class} Shift()
:canonical: hepyaestus.ShiftScheduler.Shift

Bases: {py:obj}`abc.ABC`

````{py:method} isOnShift(time: float) -> bool
:canonical: hepyaestus.ShiftScheduler.Shift.isOnShift
:abstractmethod:

```{autodoc2-docstring} hepyaestus.ShiftScheduler.Shift.isOnShift
```

````

````{py:method} next(time: float) -> tuple[float, float]
:canonical: hepyaestus.ShiftScheduler.Shift.next
:abstractmethod:

```{autodoc2-docstring} hepyaestus.ShiftScheduler.Shift.next
```

````

`````

`````{py:class} ShiftPattern(onFor: float, offFor: float)
:canonical: hepyaestus.ShiftScheduler.ShiftPattern

Bases: {py:obj}`hepyaestus.ShiftScheduler.Shift`

````{py:method} isOnShift(time: float) -> bool
:canonical: hepyaestus.ShiftScheduler.ShiftPattern.isOnShift

```{autodoc2-docstring} hepyaestus.ShiftScheduler.ShiftPattern.isOnShift
```

````

````{py:method} next(time: float) -> tuple[float, float]
:canonical: hepyaestus.ShiftScheduler.ShiftPattern.next

```{autodoc2-docstring} hepyaestus.ShiftScheduler.ShiftPattern.next
```

````

`````

`````{py:class} ShiftSchedule(schedule: list[tuple[float, float]])
:canonical: hepyaestus.ShiftScheduler.ShiftSchedule

Bases: {py:obj}`hepyaestus.ShiftScheduler.Shift`

````{py:method} isOnShift(time: float) -> bool
:canonical: hepyaestus.ShiftScheduler.ShiftSchedule.isOnShift

```{autodoc2-docstring} hepyaestus.ShiftScheduler.ShiftSchedule.isOnShift
```

````

````{py:method} next(time: float) -> tuple[float, float]
:canonical: hepyaestus.ShiftScheduler.ShiftSchedule.next

```{autodoc2-docstring} hepyaestus.ShiftScheduler.ShiftSchedule.next
```

````

`````

````{py:function} vaildateSchedule(schedule: list[tuple[float, float]]) -> list[tuple[float, float]]
:canonical: hepyaestus.ShiftScheduler.vaildateSchedule

```{autodoc2-docstring} hepyaestus.ShiftScheduler.vaildateSchedule
```
````
