"""
Spectral analysis utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.signal import periodogram


@dataclass(frozen=True)
class SpectralReport:
    """Periodogram results."""

    frequency: np.ndarray
    power: np.ndarray


def spectral_report(
    series: pd.Series,
    *,
    sampling_frequency: float = 1.0,
    detrend: str = "linear",
) -> SpectralReport:
    """
    Compute a periodogram for a time series.
    """
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    clean = series.dropna()

    if len(clean) < 2:
        raise ValueError("At least two observations are required.")

    frequency, power = periodogram(
        clean.to_numpy(dtype=float),
        fs=sampling_frequency,
        detrend=detrend,
        scaling="density",
    )

    return SpectralReport(
        frequency=np.asarray(frequency, dtype=float),
        power=np.asarray(power, dtype=float),
    )
