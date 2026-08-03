"""
Descriptive statistics for climate time series.

This module provides descriptive statistical summaries for
pandas Series and DataFrames used in climate applications.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import pandas as pd


@dataclass(frozen=True)
class StatisticsReport:
    """
    Descriptive statistics summary.
    """

    observations: int
    missing: int

    mean: float
    median: float
    minimum: float
    maximum: float

    variance: float
    standard_deviation: float

    skewness: float
    kurtosis: float

    def to_dict(self) -> dict[str, object]:
        """
        Convert the report into a dictionary.
        """
        return asdict(self)


def describe(series: pd.Series) -> StatisticsReport:
    """
    Compute descriptive statistics for a pandas Series.

    Parameters
    ----------
    series
        Input time series.

    Returns
    -------
    StatisticsReport
        Descriptive statistical summary.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    clean = series.dropna()

    return StatisticsReport(
        observations=int(series.size),
        missing=int(series.isna().sum()),
        mean=float(clean.mean()),
        median=float(clean.median()),
        minimum=float(clean.min()),
        maximum=float(clean.max()),
        variance=float(clean.var()),
        standard_deviation=float(clean.std()),
        skewness=float(clean.skew()),
        kurtosis=float(clean.kurt()),
    )