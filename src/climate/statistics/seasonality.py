"""
Seasonality analysis utilities.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict

import pandas as pd


@dataclass(frozen=True)
class SeasonalityReport:
    """Monthly climatology and anomalies."""

    climatology: pd.Series
    anomalies: pd.Series

    def to_dict(self) -> dict:
        return {
            "climatology": self.climatology,
            "anomalies": self.anomalies,
        }


def monthly_climatology(series: pd.Series) -> pd.Series:
    """
    Compute monthly climatology.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    if not isinstance(series.index, pd.DatetimeIndex):
        raise TypeError("Series must have a DatetimeIndex.")

    return series.groupby(series.index.month).mean()


def monthly_anomalies(series: pd.Series) -> pd.Series:
    """
    Compute monthly anomalies.
    """

    climatology = monthly_climatology(series)

    anomalies = series.copy()

    for month in range(1, 13):
        mask = anomalies.index.month == month
        anomalies.loc[mask] = (
            anomalies.loc[mask] - climatology.loc[month]
        )

    return anomalies


def seasonality_report(series: pd.Series) -> SeasonalityReport:
    """
    Return monthly climatology and anomalies.
    """

    return SeasonalityReport(
        climatology=monthly_climatology(series),
        anomalies=monthly_anomalies(series),
    )