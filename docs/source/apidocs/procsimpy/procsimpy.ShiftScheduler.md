# {py:mod}`procsimpy.ShiftScheduler`

```{py:module} procsimpy.ShiftScheduler
```

```{autodoc2-docstring} procsimpy.ShiftScheduler
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Shift <procsimpy.ShiftScheduler.Shift>`
  -
* - {py:obj}`ShiftPattern <procsimpy.ShiftScheduler.ShiftPattern>`
  -
* - {py:obj}`ShiftSchedule <procsimpy.ShiftScheduler.ShiftSchedule>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ShiftBuilder <procsimpy.ShiftScheduler.ShiftBuilder>`
  - ```{autodoc2-docstring} procsimpy.ShiftScheduler.ShiftBuilder
    :summary:
    ```
* - {py:obj}`vaildateSchedule <procsimpy.ShiftScheduler.vaildateSchedule>`
  - ```{autodoc2-docstring} procsimpy.ShiftScheduler.vaildateSchedule
    :summary:
    ```
````

### API

````{py:function} ShiftBuilder(pattern: typing.Optional[tuple[float, float]] = None, schedule: typing.Optional[list[tuple[float, float]]] = None) -> ShiftPattern | ShiftSchedule
:canonical: procsimpy.ShiftScheduler.ShiftBuilder

```{autodoc2-docstring} procsimpy.ShiftScheduler.ShiftBuilder
```
````

`````{py:class} Shift
:canonical: procsimpy.ShiftScheduler.Shift

Bases: {py:obj}`abc.ABC`

````{py:method} isOnShift(time: float) -> bool
:canonical: procsimpy.ShiftScheduler.Shift.isOnShift
:abstractmethod:

```{autodoc2-docstring} procsimpy.ShiftScheduler.Shift.isOnShift
```

````

````{py:method} next(time: float) -> tuple[float, float]
:canonical: procsimpy.ShiftScheduler.Shift.next
:abstractmethod:

```{autodoc2-docstring} procsimpy.ShiftScheduler.Shift.next
```

````

`````

`````{py:class} ShiftPattern(onFor: float, offFor: float)
:canonical: procsimpy.ShiftScheduler.ShiftPattern

Bases: {py:obj}`procsimpy.ShiftScheduler.Shift`

````{py:method} isOnShift(time: float) -> bool
:canonical: procsimpy.ShiftScheduler.ShiftPattern.isOnShift

```{autodoc2-docstring} procsimpy.ShiftScheduler.ShiftPattern.isOnShift
```

````

````{py:method} next(time: float) -> tuple[float, float]
:canonical: procsimpy.ShiftScheduler.ShiftPattern.next

```{autodoc2-docstring} procsimpy.ShiftScheduler.ShiftPattern.next
```

````

`````

`````{py:class} ShiftSchedule(schedule: list[tuple[float, float]])
:canonical: procsimpy.ShiftScheduler.ShiftSchedule

Bases: {py:obj}`procsimpy.ShiftScheduler.Shift`

````{py:method} isOnShift(time: float) -> bool
:canonical: procsimpy.ShiftScheduler.ShiftSchedule.isOnShift

```{autodoc2-docstring} procsimpy.ShiftScheduler.ShiftSchedule.isOnShift
```

````

````{py:method} next(time: float) -> tuple[float, float]
:canonical: procsimpy.ShiftScheduler.ShiftSchedule.next

```{autodoc2-docstring} procsimpy.ShiftScheduler.ShiftSchedule.next
```

````

`````

````{py:function} vaildateSchedule(schedule: list[tuple[float, float]]) -> list[tuple[float, float]]
:canonical: procsimpy.ShiftScheduler.vaildateSchedule

```{autodoc2-docstring} procsimpy.ShiftScheduler.vaildateSchedule
```
````
