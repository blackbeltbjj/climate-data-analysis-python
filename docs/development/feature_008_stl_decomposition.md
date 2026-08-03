# Feature 008 — STL Decomposition

## Status

Completed

---

## Version

0.1.0-dev

---

## Module

src/climate/statistics/decomposition.py

---

## Purpose

Provide a reusable interface for Seasonal-Trend decomposition using LOESS (STL).

---

## Public API

```python
from climate.statistics import stl_decompose
```

---

## Classes

- STLReport

---

## Functions

- stl_decompose()

---

## Input

- pandas.Series
- DatetimeIndex
- Regular time series

---

## Output

- Trend component
- Seasonal component
- Residual component

Returned as an `STLReport`.

---

## Files Created

```
src/climate/statistics/decomposition.py
tests/test_statistics_decomposition.py
```

---

## Files Modified

```
src/climate/statistics/__init__.py
PROJECT_STATUS.md
```

---

## Tests

Feature tests:

3 passing

Project tests:

35 passing

---

## Dependencies

- pandas
- statsmodels

---

## Design Notes

- Built on `statsmodels.tsa.seasonal.STL`
- Returns a dataclass instead of the raw Statsmodels object
- Preserves the original DatetimeIndex
- Consistent API with the rest of the `climate.statistics` package

---

## Next Feature

Feature 009

Stationarity Analysis

Planned public API

```python
from climate.statistics import (
    adf_test,
    kpss_test,
)
```

---

End of Feature 008