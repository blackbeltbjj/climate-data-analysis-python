"""
Warm Pool climate diagnostics.
"""

from __future__ import annotations

import pandas as pd


def monthly_anomaly(
    series: pd.Series,
) -> pd.Series:
    """
    Remove the monthly climatological cycle.

    Calculates anomalies relative to the
    mean value for each calendar month.
    """

    if not isinstance(
        series,
        pd.Series,
    ):
        raise TypeError(
            "Input must be a pandas Series."
        )

    if not isinstance(
        series.index,
        pd.DatetimeIndex,
    ):
        raise TypeError(
            "Series index must be a DatetimeIndex."
        )

    if series.empty:
        raise ValueError(
            "Series cannot be empty."
        )

    climatology = series.groupby(
        series.index.month
    ).transform(
        "mean"
    )

    return series - climatology


def warm_pool_longitude_anomaly(
    tracking: pd.DataFrame,
) -> pd.Series:
    """
    Calculate Warm Pool longitude anomalies.
    """

    if "longitude" not in tracking.columns:
        raise ValueError(
            "Missing longitude column."
        )

    return monthly_anomaly(
        tracking["longitude"]
    )


def warm_pool_latitude_anomaly(
    tracking: pd.DataFrame,
) -> pd.Series:
    """
    Calculate Warm Pool latitude anomalies.
    """

    if "latitude" not in tracking.columns:
        raise ValueError(
            "Missing latitude column."
        )

    return monthly_anomaly(
        tracking["latitude"]
    )


def warm_pool_area_anomaly(
    tracking: pd.DataFrame,
) -> pd.Series:
    """
    Calculate Warm Pool area anomalies.
    """

    if "area_fraction" not in tracking.columns:
        raise ValueError(
            "Missing area_fraction column."
        )

    return monthly_anomaly(
        tracking["area_fraction"]
    )