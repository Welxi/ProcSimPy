# {py:mod}`procsimpy.tests.test_printTrace`

```{py:module} procsimpy.tests.test_printTrace
```

```{autodoc2-docstring} procsimpy.tests.test_printTrace
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`transmission <procsimpy.tests.test_printTrace.transmission>`
  - ```{autodoc2-docstring} procsimpy.tests.test_printTrace.transmission
    :summary:
    ```
* - {py:obj}`base <procsimpy.tests.test_printTrace.base>`
  - ```{autodoc2-docstring} procsimpy.tests.test_printTrace.base
    :summary:
    ```
* - {py:obj}`caller <procsimpy.tests.test_printTrace.caller>`
  - ```{autodoc2-docstring} procsimpy.tests.test_printTrace.caller
    :summary:
    ```
* - {py:obj}`eventData <procsimpy.tests.test_printTrace.eventData>`
  - ```{autodoc2-docstring} procsimpy.tests.test_printTrace.eventData
    :summary:
    ```
* - {py:obj}`timecode <procsimpy.tests.test_printTrace.timecode>`
  - ```{autodoc2-docstring} procsimpy.tests.test_printTrace.timecode
    :summary:
    ```
* - {py:obj}`test_printTrace_invalidArg <procsimpy.tests.test_printTrace.test_printTrace_invalidArg>`
  - ```{autodoc2-docstring} procsimpy.tests.test_printTrace.test_printTrace_invalidArg
    :summary:
    ```
* - {py:obj}`test_printTrace_TooManArgs <procsimpy.tests.test_printTrace.test_printTrace_TooManArgs>`
  - ```{autodoc2-docstring} procsimpy.tests.test_printTrace.test_printTrace_TooManArgs
    :summary:
    ```
* - {py:obj}`test_printTrace_keywords <procsimpy.tests.test_printTrace.test_printTrace_keywords>`
  - ```{autodoc2-docstring} procsimpy.tests.test_printTrace.test_printTrace_keywords
    :summary:
    ```
````

### API

````{py:function} transmission() -> procsimpy.Base.Base
:canonical: procsimpy.tests.test_printTrace.transmission

```{autodoc2-docstring} procsimpy.tests.test_printTrace.transmission
```
````

````{py:function} base() -> procsimpy.Base.Base
:canonical: procsimpy.tests.test_printTrace.base

```{autodoc2-docstring} procsimpy.tests.test_printTrace.base
```
````

````{py:function} caller() -> procsimpy.Base.Base
:canonical: procsimpy.tests.test_printTrace.caller

```{autodoc2-docstring} procsimpy.tests.test_printTrace.caller
```
````

````{py:function} eventData(caller, transmission) -> procsimpy.EventData.EventData
:canonical: procsimpy.tests.test_printTrace.eventData

```{autodoc2-docstring} procsimpy.tests.test_printTrace.eventData
```
````

````{py:function} timecode(eventData) -> str
:canonical: procsimpy.tests.test_printTrace.timecode

```{autodoc2-docstring} procsimpy.tests.test_printTrace.timecode
```
````

````{py:function} test_printTrace_invalidArg(base, eventData) -> None
:canonical: procsimpy.tests.test_printTrace.test_printTrace_invalidArg

```{autodoc2-docstring} procsimpy.tests.test_printTrace.test_printTrace_invalidArg
```
````

````{py:function} test_printTrace_TooManArgs(base, eventData) -> None
:canonical: procsimpy.tests.test_printTrace.test_printTrace_TooManArgs

```{autodoc2-docstring} procsimpy.tests.test_printTrace.test_printTrace_TooManArgs
```
````

````{py:function} test_printTrace_keywords(base, eventData, timecode, caller, transmission, capsys) -> None
:canonical: procsimpy.tests.test_printTrace.test_printTrace_keywords

```{autodoc2-docstring} procsimpy.tests.test_printTrace.test_printTrace_keywords
```
````
