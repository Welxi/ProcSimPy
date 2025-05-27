# {py:mod}`hepyaestus.tests.test_printTrace`

```{py:module} hepyaestus.tests.test_printTrace
```

```{autodoc2-docstring} hepyaestus.tests.test_printTrace
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`transmission <hepyaestus.tests.test_printTrace.transmission>`
  - ```{autodoc2-docstring} hepyaestus.tests.test_printTrace.transmission
    :summary:
    ```
* - {py:obj}`base <hepyaestus.tests.test_printTrace.base>`
  - ```{autodoc2-docstring} hepyaestus.tests.test_printTrace.base
    :summary:
    ```
* - {py:obj}`caller <hepyaestus.tests.test_printTrace.caller>`
  - ```{autodoc2-docstring} hepyaestus.tests.test_printTrace.caller
    :summary:
    ```
* - {py:obj}`eventData <hepyaestus.tests.test_printTrace.eventData>`
  - ```{autodoc2-docstring} hepyaestus.tests.test_printTrace.eventData
    :summary:
    ```
* - {py:obj}`timecode <hepyaestus.tests.test_printTrace.timecode>`
  - ```{autodoc2-docstring} hepyaestus.tests.test_printTrace.timecode
    :summary:
    ```
* - {py:obj}`test_printTrace_invalidArg <hepyaestus.tests.test_printTrace.test_printTrace_invalidArg>`
  - ```{autodoc2-docstring} hepyaestus.tests.test_printTrace.test_printTrace_invalidArg
    :summary:
    ```
* - {py:obj}`test_printTrace_TooManArgs <hepyaestus.tests.test_printTrace.test_printTrace_TooManArgs>`
  - ```{autodoc2-docstring} hepyaestus.tests.test_printTrace.test_printTrace_TooManArgs
    :summary:
    ```
* - {py:obj}`test_printTrace_keywords <hepyaestus.tests.test_printTrace.test_printTrace_keywords>`
  - ```{autodoc2-docstring} hepyaestus.tests.test_printTrace.test_printTrace_keywords
    :summary:
    ```
````

### API

````{py:function} transmission() -> hepyaestus.Base.BaseObject
:canonical: hepyaestus.tests.test_printTrace.transmission

```{autodoc2-docstring} hepyaestus.tests.test_printTrace.transmission
```
````

````{py:function} base() -> hepyaestus.Base.BaseObject
:canonical: hepyaestus.tests.test_printTrace.base

```{autodoc2-docstring} hepyaestus.tests.test_printTrace.base
```
````

````{py:function} caller() -> hepyaestus.Base.BaseObject
:canonical: hepyaestus.tests.test_printTrace.caller

```{autodoc2-docstring} hepyaestus.tests.test_printTrace.caller
```
````

````{py:function} eventData(caller, transmission) -> hepyaestus.EventData.EventData
:canonical: hepyaestus.tests.test_printTrace.eventData

```{autodoc2-docstring} hepyaestus.tests.test_printTrace.eventData
```
````

````{py:function} timecode(eventData) -> str
:canonical: hepyaestus.tests.test_printTrace.timecode

```{autodoc2-docstring} hepyaestus.tests.test_printTrace.timecode
```
````

````{py:function} test_printTrace_invalidArg(base, eventData) -> None
:canonical: hepyaestus.tests.test_printTrace.test_printTrace_invalidArg

```{autodoc2-docstring} hepyaestus.tests.test_printTrace.test_printTrace_invalidArg
```
````

````{py:function} test_printTrace_TooManArgs(base, eventData) -> None
:canonical: hepyaestus.tests.test_printTrace.test_printTrace_TooManArgs

```{autodoc2-docstring} hepyaestus.tests.test_printTrace.test_printTrace_TooManArgs
```
````

````{py:function} test_printTrace_keywords(base, eventData, timecode, caller, transmission, capsys) -> None
:canonical: hepyaestus.tests.test_printTrace.test_printTrace_keywords

```{autodoc2-docstring} hepyaestus.tests.test_printTrace.test_printTrace_keywords
```
````
