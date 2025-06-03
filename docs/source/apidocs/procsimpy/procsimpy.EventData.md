# {py:mod}`procsimpy.EventData`

```{py:module} procsimpy.EventData
```

```{autodoc2-docstring} procsimpy.EventData
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EventData <procsimpy.EventData.EventData>`
  - ```{autodoc2-docstring} procsimpy.EventData.EventData
    :summary:
    ```
* - {py:obj}`CreateEvent <procsimpy.EventData.CreateEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.CreateEvent
    :summary:
    ```
* - {py:obj}`InitEvent <procsimpy.EventData.InitEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.InitEvent
    :summary:
    ```
* - {py:obj}`EnterEvent <procsimpy.EventData.EnterEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.EnterEvent
    :summary:
    ```
* - {py:obj}`ReceiveEvent <procsimpy.EventData.ReceiveEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.ReceiveEvent
    :summary:
    ```
* - {py:obj}`GiveEvent <procsimpy.EventData.GiveEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.GiveEvent
    :summary:
    ```
* - {py:obj}`isRequestedEvent <procsimpy.EventData.isRequestedEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.isRequestedEvent
    :summary:
    ```
* - {py:obj}`canDisposeEvent <procsimpy.EventData.canDisposeEvent>`
  -
* - {py:obj}`StartWorkEvent <procsimpy.EventData.StartWorkEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.StartWorkEvent
    :summary:
    ```
* - {py:obj}`FinishWorkEvent <procsimpy.EventData.FinishWorkEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.FinishWorkEvent
    :summary:
    ```
* - {py:obj}`InterruptEvent <procsimpy.EventData.InterruptEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.InterruptEvent
    :summary:
    ```
* - {py:obj}`InterruptEndEvent <procsimpy.EventData.InterruptEndEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.InterruptEndEvent
    :summary:
    ```
* - {py:obj}`WIPEvent <procsimpy.EventData.WIPEvent>`
  - ```{autodoc2-docstring} procsimpy.EventData.WIPEvent
    :summary:
    ```
````

### API

`````{py:class} EventData
:canonical: procsimpy.EventData.EventData

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} procsimpy.EventData.EventData
```

````{py:attribute} time
:canonical: procsimpy.EventData.EventData.time
:type: simpy.core.SimTime
:value: >
   None

```{autodoc2-docstring} procsimpy.EventData.EventData.time
```

````

````{py:attribute} caller
:canonical: procsimpy.EventData.EventData.caller
:type: procsimpy.Base.Base
:value: >
   None

```{autodoc2-docstring} procsimpy.EventData.EventData.caller
```

````

````{py:attribute} id
:canonical: procsimpy.EventData.EventData.id
:type: int
:value: >
   'field(...)'

```{autodoc2-docstring} procsimpy.EventData.EventData.id
```

````

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.EventData.phrase
:abstractmethod:

```{autodoc2-docstring} procsimpy.EventData.EventData.phrase
```

````

`````

`````{py:class} CreateEvent
:canonical: procsimpy.EventData.CreateEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.CreateEvent
```

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.CreateEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.CreateEvent.phrase
```

````

`````

`````{py:class} InitEvent
:canonical: procsimpy.EventData.InitEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.InitEvent
```

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.InitEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.InitEvent.phrase
```

````

`````

`````{py:class} EnterEvent
:canonical: procsimpy.EventData.EnterEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.EnterEvent
```

````{py:attribute} station
:canonical: procsimpy.EventData.EnterEvent.station
:type: procsimpy.Node.Node
:value: >
   None

```{autodoc2-docstring} procsimpy.EventData.EnterEvent.station
```

````

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.EnterEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.EnterEvent.phrase
```

````

`````

`````{py:class} ReceiveEvent
:canonical: procsimpy.EventData.ReceiveEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.ReceiveEvent
```

````{py:attribute} entity
:canonical: procsimpy.EventData.ReceiveEvent.entity
:type: procsimpy.Entity.Entity
:value: >
   None

```{autodoc2-docstring} procsimpy.EventData.ReceiveEvent.entity
```

````

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.ReceiveEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.ReceiveEvent.phrase
```

````

`````

`````{py:class} GiveEvent
:canonical: procsimpy.EventData.GiveEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.GiveEvent
```

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.GiveEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.GiveEvent.phrase
```

````

`````

`````{py:class} isRequestedEvent
:canonical: procsimpy.EventData.isRequestedEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.isRequestedEvent
```

````{py:attribute} requestingNode
:canonical: procsimpy.EventData.isRequestedEvent.requestingNode
:type: procsimpy.Node.Node
:value: >
   None

```{autodoc2-docstring} procsimpy.EventData.isRequestedEvent.requestingNode
```

````

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.isRequestedEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.isRequestedEvent.phrase
```

````

`````

`````{py:class} canDisposeEvent
:canonical: procsimpy.EventData.canDisposeEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.canDisposeEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.canDisposeEvent.phrase
```

````

`````

`````{py:class} StartWorkEvent
:canonical: procsimpy.EventData.StartWorkEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.StartWorkEvent
```

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.StartWorkEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.StartWorkEvent.phrase
```

````

`````

`````{py:class} FinishWorkEvent
:canonical: procsimpy.EventData.FinishWorkEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.FinishWorkEvent
```

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.FinishWorkEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.FinishWorkEvent.phrase
```

````

`````

`````{py:class} InterruptEvent
:canonical: procsimpy.EventData.InterruptEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.InterruptEvent
```

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.InterruptEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.InterruptEvent.phrase
```

````

`````

`````{py:class} InterruptEndEvent
:canonical: procsimpy.EventData.InterruptEndEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.InterruptEndEvent
```

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.InterruptEndEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.InterruptEndEvent.phrase
```

````

`````

`````{py:class} WIPEvent
:canonical: procsimpy.EventData.WIPEvent

Bases: {py:obj}`procsimpy.EventData.EventData`

```{autodoc2-docstring} procsimpy.EventData.WIPEvent
```

````{py:method} phrase() -> str
:canonical: procsimpy.EventData.WIPEvent.phrase

```{autodoc2-docstring} procsimpy.EventData.WIPEvent.phrase
```

````

`````
