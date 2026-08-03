"""
Cross-correlation analysis utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class CrossCorrelationReport:
    """Cross-correlation results across a range of lags."""

    lags: np.ndarray
    correlations: np.ndarray
    max_correlation: float
    max_correlation_lag: int
    max_absolute_correlation: float
    max_absolute_correlation_lag: int
    zero_lag_correlation: float


def cross_correlation_report(
    x: pd.Series,
    y: pd.Series,
    *,
    max_lag: int = 12,
) -> CrossCorrelationReport:
    """
    Compute lagged cross-correlation between two aligned time series.

    Positive lag compares x(t) with y(t-lag).
    """
    if not isinstance(x, pd.Series) or not isinstance(y, pd.Series):
        raise TypeError("Inputs must be pandas Series.")

    if max_lag < 0:
        raise ValueError("max_lag must be non-negative.")

    aligned = pd.concat([x, y], axis=1, join="inner").dropna()

    if len(aligned) <= max_lag:
        raise ValueError(
            "The number of aligned observations must be greater than max_lag."
        )

    x_clean = aligned.iloc[:, 0]
    y_clean = aligned.iloc[:, 1]

    lags = np.arange(-max_lag, max_lag + 1)
    correlations = np.empty(len(lags), dtype=float)

    for i, lag in enumerate(lags):
        correlations[i] = x_clean.corr(y_clean.shift(lag))

    valid = ~np.isnan(correlations)

    if not np.any(valid):
        raise ValueError("Cross-correlation could not be calculated.")

    valid_lags = lags[valid]
    valid_correlations = correlations[valid]

    max_index = int(np.argmax(valid_correlations))
    max_abs_index = int(np.argmax(np.abs(valid_correlations)))

    zero_lag_index = int(np.where(lags == 0)[0][0])

    return CrossCorrelationReport(
        lags=lags,
        correlations=correlations,
        max_correlation=float(valid_correlations[max_index]),
        max_correlation_lag=int(valid_lags[max_index]),
        max_absolute_correlation=float(
            valid_correlations[max_abs_index]
        ),
        max_absolute_correlation_lag=int(
            valid_lags[max_abs_index]
        ),
        zero_lag_correlation=float(correlations[zero_lag_index]),
    )