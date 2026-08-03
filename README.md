# Climate Data Analysis Python

A professional open-source Python library for climate and oceanographic data analysis, statistical time-series analysis, forecasting, and scientific visualization.

---

## Overview

Climate Data Analysis Python provides reusable tools for analysing climate datasets using modern scientific Python libraries.

The project is designed for:

- Climate researchers
- Oceanographers
- Environmental scientists
- University students
- Educators
- Data scientists working with environmental data

The library emphasizes:

- Modular design
- Reproducible workflows
- Well-tested code
- Scientific correctness
- Publication-quality analysis

---

## Current Features

### Time

- Datetime validation
- Missing timestamp detection
- Frequency inference
- Resampling utilities
- Time-series reporting

### Statistics

- Descriptive statistics
- Trend analysis
- Seasonality analysis
- STL decomposition
- Stationarity tests
- Autocorrelation
- Spectral analysis

---

## Installation

```bash
git clone https://github.com/blackbeltbjj/climate-data-analysis-python.git

cd climate-data-analysis-python

python -m venv .venv

.venv\Scripts\activate

pip install -e .
```

---

## Example

```python
import pandas as pd

from climate.statistics import (
    describe,
    linear_trend,
    stl_decompose,
)

series = pd.Series(...)

statistics = describe(series)

trend = linear_trend(series)

stl = stl_decompose(series)
```

---

## Project Structure

```
src/
    climate/
        statistics/
        time/
        io/
        visualization/
        preprocessing/
        geospatial/
        forecast/
        wavelets/
```

---

## Testing

Run the complete test suite:

```bash
python -m pytest -v
```

Current status:

- 47 automated tests
- All passing

---

## Roadmap

### Completed

- Time utilities
- Descriptive statistics
- Trend analysis
- Seasonality
- STL decomposition
- Stationarity
- Autocorrelation
- Spectral analysis

### In Progress

- Cross-correlation
- Forecasting
- Wavelet analysis
- Geospatial analysis
- Scientific visualization

---

## License

MIT License

---

## Author

Fabio Vieira Machado