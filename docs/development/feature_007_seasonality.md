# Feature 007 — Seasonality Analysis

## Status

Completed

---

## Version

0.1.0-dev

---

## Module

src/climate/statistics/seasonality.py

---

## Purpose

Provide reusable functions for seasonal climatology and anomaly calculations for climate time series.

---

## Public API

```python
from climate.statistics import (
    monthly_climatology,
    monthly_anomalies,
    seasonality_report,
)
```

---

## Classes

- SeasonalityReport

---

## Functions

- monthly_climatology()
- monthly_anomalies()
- seasonality_report()

---

## Input

- pandas.Series
- DatetimeIndex
- Monthly time series

---

## Output

- Monthly climatology (12 values)
- Monthly anomaly series
- SeasonalityReport

---

## Files Created

```
src/climate/statistics/seasonality.py
tests/test_statistics_seasonality.py
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

32 passing

---

## Dependencies

- pandas
- numpy

---

## Design Notes

- Consistent API with other statistics modules.
- Uses dataclasses for structured results.
- Monthly climatology calculated by calendar month.
- Monthly anomalies computed relative to climatology.

---

## Next Feature

Feature 008

Statistics — STL Decomposition

Planned public API

```python
from climate.statistics import stl_decompose
```

---

End of Feature 007