"""
Temporal resampling utilities for climate time series.
"""

from __future__ import annotations

from typing import Literal

import pandas as pd

from climate.time.validation import validate_datetime_index

Aggregation = Literal["mean", "sum", "median", "min", "max"]


def _resample(
    data: pd.Series | pd.DataFrame,
    frequency: str,
    aggregation: Aggregation,
) -> pd.Series | pd.DataFrame:
    """
    Resample a time series using a supported aggregation method.
    """
    validate_datetime_index(data)

    if data.empty:
        return data.copy()

    resampler = data.resample(frequency)

    methods = {
        "mean": resampler.mean,
        "sum": resampler.sum,
        "median": resampler.median,
        "min": resampler.min,
        "max": resampler.max,
    }

    try:
        method = methods[aggregation]
    except KeyError as exc:
        allowed = ", ".join(methods)
        raise ValueError(
            f"Unsupported aggregation: {aggregation}. "
            f"Choose from: {allowed}."
        ) from exc

    return method()


def daily_to_monthly(
    data: pd.Series | pd.DataFrame,
    *,
    aggregation: Aggregation = "mean",
) -> pd.Series | pd.DataFrame:
    """
    Convert a daily time series to monthly values.

    Monthly timestamps are placed at the beginning of each month.
    """
    return _resample(data, "MS", aggregation)


def monthly_to_annual(
    data: pd.Series | pd.DataFrame,
    *,
    aggregation: Aggregation = "mean",
) -> pd.Series | pd.DataFrame:
    """
    Convert a monthly time series to annual values.

    Annual timestamps are placed at the beginning of each year.
    """
    return _resample(data, "YS", aggregation)


def daily_to_annual(
    data: pd.Series | pd.DataFrame,
    *,
    aggregation: Aggregation = "mean",
) -> pd.Series | pd.DataFrame:
    """
    Convert a daily time series directly to annual values.
    """
    return _resample(data, "YS", aggregation)