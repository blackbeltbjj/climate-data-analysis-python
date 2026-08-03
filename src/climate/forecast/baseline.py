"""
Baseline forecasting models.
"""

from __future__ import annotations

import pandas as pd


def persistence_forecast(
    series: pd.Series,
    *,
    steps: int = 12,
) -> pd.Series:
    """
    Forecast future values using the last observed value.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    if steps <= 0:
        raise ValueError("Steps must be positive.")

    clean = series.dropna()

    if len(clean) == 0:
        raise ValueError("Series cannot be empty.")

    last_value = clean.iloc[-1]

    future_index = pd.RangeIndex(
        start=0,
        stop=steps,
    )

    return pd.Series(
        last_value,
        index=future_index,
    )


def mean_forecast(
    series: pd.Series,
    *,
    steps: int = 12,
) -> pd.Series:
    """
    Forecast future values using the historical mean.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    if steps <= 0:
        raise ValueError("Steps must be positive.")

    clean = series.dropna()

    if len(clean) == 0:
        raise ValueError("Series cannot be empty.")

    mean_value = clean.mean()

    future_index = pd.RangeIndex(
        start=0,
        stop=steps,
    )

    return pd.Series(
        mean_value,
        index=future_index,
    )