# Feature 009 — Stationarity Analysis

## Status

Completed

---

## Version

0.1.0-dev

---

## Module

src/climate/statistics/stationarity.py

---

## Purpose

Provide reusable interfaces for statistical stationarity tests commonly used in climate and oceanographic time-series analysis.

---

## Public API

```python
from climate.statistics import (
    adf_test,
    kpss_test,
)
```

---

## Classes

- StationarityReport

---

## Functions

- adf_test()
- kpss_test()

---

## Input

- pandas.Series
- DatetimeIndex
- Regular time series

---

## Output

- Test statistic
- p-value
- Stationarity flag
- Test name

Returned as a `StationarityReport`.

---

## Files Created

```
src/climate/statistics/stationarity.py
tests/test_statistics_stationarity.py
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

4 passing

Project tests:

39 passing

---

## Dependencies

- pandas
- statsmodels

---

## Design Notes

- Supports Augmented Dickey–Fuller (ADF) test.
- Supports KPSS stationarity test.
- Returns a common dataclass for both tests.
- API consistent with other modules in `climate.statistics`.

---

## Next Feature

Feature 010

Autocorrelation Analysis

Planned public API

```python
from climate.statistics import (
    acf,
    pacf,
    autocorrelation_report,
)
```

---

End of Feature 009