"""
Autocorrelation analysis utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import acf as sm_acf
from statsmodels.tsa.stattools import pacf as sm_pacf


@dataclass(frozen=True)
class AutocorrelationReport:
    """Autocorrelation and partial autocorrelation results."""

    lags: np.ndarray
    acf_values: np.ndarray
    pacf_values: np.ndarray


def autocorrelation_report(
    series: pd.Series,
    *,
    nlags: int = 40,
) -> AutocorrelationReport:
    """
    Compute ACF and PACF values for a time series.
    """
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    clean = series.dropna()

    if len(clean) <= nlags:
        raise ValueError("The number of observations must be greater than nlags.")

    acf_values = sm_acf(clean, nlags=nlags, fft=True)
    pacf_values = sm_pacf(clean, nlags=nlags, method="ywm")
    lags = np.arange(nlags + 1)

    return AutocorrelationReport(
        lags=lags,
        acf_values=np.asarray(acf_values, dtype=float),
        pacf_values=np.asarray(pacf_values, dtype=float),
    )
