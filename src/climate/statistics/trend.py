"""
Trend analysis utilities.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict

import numpy as np
import pandas as pd
from scipy.stats import linregress


@dataclass(frozen=True)
class TrendReport:
    """Summary of a linear trend."""

    slope: float
    intercept: float
    r_value: float
    r_squared: float
    p_value: float
    standard_error: float

    def to_dict(self) -> dict:
        return asdict(self)


def linear_trend(series: pd.Series) -> TrendReport:
    """
    Fit a simple linear trend to a pandas Series.
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    clean = series.dropna()

    if len(clean) < 2:
        raise ValueError("At least two observations are required.")

    x = np.arange(len(clean), dtype=float)

    result = linregress(x, clean.values)

    return TrendReport(
        slope=float(result.slope),
        intercept=float(result.intercept),
        r_value=float(result.rvalue),
        r_squared=float(result.rvalue ** 2),
        p_value=float(result.pvalue),
        standard_error=float(result.stderr),
    )