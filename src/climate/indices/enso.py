"""
ENSO index utilities.

Provides basic structures and methods for working with
Niño region climate indices.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class ENSOIndexReport:
    """
    Container for ENSO index time series metadata.
    """

    name: str
    observations: int
    start: pd.Timestamp
    end: pd.Timestamp


def enso_report(
    series: pd.Series,
    *,
    name: str = "ENSO Index",
) -> ENSOIndexReport:
    """
    Generate a basic ENSO index report.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    clean = series.dropna()

    if clean.empty:
        raise ValueError(
            "ENSO index series cannot be empty."
        )

    return ENSOIndexReport(
        name=name,
        observations=len(clean),
        start=clean.index.min(),
        end=clean.index.max(),
    )


def monthly_anomalies(
    series: pd.Series,
) -> pd.Series:
    """
    Calculate monthly climatological anomalies.

    The anomaly is calculated by subtracting the
    climatological mean for each calendar month.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    if not isinstance(series.index, pd.DatetimeIndex):
        raise TypeError(
            "Series index must be a DatetimeIndex."
        )

    if series.empty:
        raise ValueError(
            "ENSO index series cannot be empty."
        )

    climatology = series.groupby(
        series.index.month
    ).transform(
        "mean"
    )

    return series - climatology