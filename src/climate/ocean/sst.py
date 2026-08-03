"""
Sea surface temperature (SST) utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class SSTReport:
    """
    Container for SST time-series metadata.
    """

    name: str
    observations: int
    start: pd.Timestamp
    end: pd.Timestamp


def sst_report(
    series: pd.Series,
    *,
    name: str = "SST",
) -> SSTReport:
    """
    Generate a basic SST report.
    """

    if not isinstance(series, pd.Series):
        raise TypeError(
            "Input must be a pandas Series."
        )

    clean = series.dropna()

    if clean.empty:
        raise ValueError(
            "SST series cannot be empty."
        )

    if not isinstance(
        clean.index,
        pd.DatetimeIndex,
    ):
        raise TypeError(
            "SST series index must be a DatetimeIndex."
        )

    return SSTReport(
        name=name,
        observations=len(clean),
        start=clean.index.min(),
        end=clean.index.max(),
    )


def monthly_sst_climatology(
    series: pd.Series,
) -> pd.Series:
    """
    Calculate monthly SST climatology.

    Returns the mean SST value for each
    calendar month.
    """

    if not isinstance(series, pd.Series):
        raise TypeError(
            "Input must be a pandas Series."
        )

    if not isinstance(
        series.index,
        pd.DatetimeIndex,
    ):
        raise TypeError(
            "SST series index must be a DatetimeIndex."
        )

    if series.empty:
        raise ValueError(
            "SST series cannot be empty."
        )

    return series.groupby(
        series.index.month
    ).mean()


def monthly_sst_anomalies(
    series: pd.Series,
) -> pd.Series:
    """
    Calculate monthly SST anomalies.
    """

    climatology = monthly_sst_climatology(
        series
    )

    return (
        series
        - series.index.month.map(
            climatology
        ).to_numpy()
    )