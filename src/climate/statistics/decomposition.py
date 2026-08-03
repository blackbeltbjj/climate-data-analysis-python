"""
STL decomposition utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from statsmodels.tsa.seasonal import STL


@dataclass(frozen=True)
class STLReport:
    """Result of an STL decomposition."""

    trend: pd.Series
    seasonal: pd.Series
    residual: pd.Series


def stl_decompose(
    series: pd.Series,
    *,
    period: int = 12,
    robust: bool = True,
) -> STLReport:
    """
    Perform STL decomposition of a time series.

    Parameters
    ----------
    series : pandas.Series
        Time series with a DatetimeIndex.
    period : int, default=12
        Seasonal period.
    robust : bool, default=True
        Use robust fitting.

    Returns
    -------
    STLReport
        Trend, seasonal and residual components.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    if not isinstance(series.index, pd.DatetimeIndex):
        raise TypeError("Series must have a DatetimeIndex.")

    result = STL(
        series,
        period=period,
        robust=robust,
    ).fit()

    return STLReport(
        trend=result.trend,
        seasonal=result.seasonal,
        residual=result.resid,
    )