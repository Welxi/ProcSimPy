# {py:mod}`hepyaestus.StoreNode`

```{py:module} hepyaestus.StoreNode
```

```{autodoc2-docstring} hepyaestus.StoreNode
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`StoreNode <hepyaestus.StoreNode.StoreNode>`
  -
````

### API

`````{py:class} StoreNode(id: str, name: str, capacity: float = Infinity, shift: typing.Optional[hepyaestus.ShiftScheduler.Shift] = None, priority: int = 0)
:canonical: hepyaestus.StoreNode.StoreNode

Bases: {py:obj}`hepyaestus.Base.BaseObject`, {py:obj}`abc.ABC`

````{py:method} initialize(env: simpy.Environment, line: hepyaestus.Line.Line) -> None
:canonical: hepyaestus.StoreNode.StoreNode.initialize

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.initialize
```

````

````{py:method} defineRouting(predecessorList: typing.Optional[list] = None, successorList: typing.Optional[list] = None) -> None
:canonical: hepyaestus.StoreNode.StoreNode.defineRouting

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.defineRouting
```

````

````{py:method} _give() -> simpy.resources.store.StoreGet
:canonical: hepyaestus.StoreNode.StoreNode._give

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode._give
```

````

````{py:method} _receive(entity: hepyaestus.Entity.Entity) -> None
:canonical: hepyaestus.StoreNode.StoreNode._receive

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode._receive
```

````

````{py:method} canReceive() -> bool
:canonical: hepyaestus.StoreNode.StoreNode.canReceive

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.canReceive
```

````

````{py:method} canGive() -> bool
:canonical: hepyaestus.StoreNode.StoreNode.canGive

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.canGive
```

````

````{py:method} notEmpty() -> bool
:canonical: hepyaestus.StoreNode.StoreNode.notEmpty

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.notEmpty
```

````

````{py:method} _getActiveEntity() -> hepyaestus.Entity.Entity | None
:canonical: hepyaestus.StoreNode.StoreNode._getActiveEntity

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode._getActiveEntity
```

````

````{py:method} run() -> collections.abc.Generator
:canonical: hepyaestus.StoreNode.StoreNode.run
:abstractmethod:

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.run
```

````

````{py:method} anyEventsTriggered() -> bool
:canonical: hepyaestus.StoreNode.StoreNode.anyEventsTriggered

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.anyEventsTriggered
```

````

````{py:method} canGiversGive() -> None
:canonical: hepyaestus.StoreNode.StoreNode.canGiversGive

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.canGiversGive
```

````

````{py:method} canReceiversReceive() -> None
:canonical: hepyaestus.StoreNode.StoreNode.canReceiversReceive

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.canReceiversReceive
```

````

````{py:method} sortReceivers() -> None
:canonical: hepyaestus.StoreNode.StoreNode.sortReceivers

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.sortReceivers
```

````

````{py:method} giveReceiverEntity(event: hepyaestus.EventData.EventData) -> None
:canonical: hepyaestus.StoreNode.StoreNode.giveReceiverEntity

```{autodoc2-docstring} hepyaestus.StoreNode.StoreNode.giveReceiverEntity
```

````

`````
