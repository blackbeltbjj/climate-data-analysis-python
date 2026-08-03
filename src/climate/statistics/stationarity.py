"""
Stationarity analysis utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss


@dataclass(frozen=True)
class StationarityReport:
    """Result of a stationarity test."""

    statistic: float
    p_value: float
    is_stationary: bool
    test: str


def adf_test(
    series: pd.Series,
    *,
    alpha: float = 0.05,
) -> StationarityReport:
    """
    Perform the Augmented Dickey-Fuller test.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    statistic, p_value, *_ = adfuller(series.dropna())

    return StationarityReport(
        statistic=float(statistic),
        p_value=float(p_value),
        is_stationary=p_value < alpha,
        test="ADF",
    )


def kpss_test(
    series: pd.Series,
    *,
    alpha: float = 0.05,
) -> StationarityReport:
    """
    Perform the KPSS stationarity test.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    statistic, p_value, *_ = kpss(
        series.dropna(),
        regression="c",
        nlags="auto",
    )

    return StationarityReport(
        statistic=float(statistic),
        p_value=float(p_value),
        is_stationary=p_value > alpha,
        test="KPSS",
    )