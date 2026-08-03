"""
Basic climate time-series analysis example.

Demonstrates:
- Creating a time series
- Descriptive statistics
- Trend analysis
"""

import numpy as np
import pandas as pd

from climate.statistics import (
    describe,
    linear_trend,
)


def main():
    dates = pd.date_range(
        "2000-01-01",
        periods=120,
        freq="MS",
    )

    values = (
        np.linspace(0, 5, 120)
        + np.sin(2 * np.pi * np.arange(120) / 12)
    )

    series = pd.Series(
        values,
        index=dates,
        name="sample_climate_series",
    )

    print("Descriptive statistics")
    print("----------------------")

    report = describe(series)

    print(report)

    print()
    print("Trend analysis")
    print("--------------")

    trend = linear_trend(series)

    print(trend)


if __name__ == "__main__":
    main()