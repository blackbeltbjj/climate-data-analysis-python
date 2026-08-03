"""
Wavelet significance tests following
Torrence & Compo (1998).

Implements AR(1) red-noise background
and wavelet power confidence levels.
"""

from __future__ import annotations

import numpy as np


def lag1_autocorrelation(
    series: np.ndarray,
) -> float:
    """
    Calculate lag-1 autocorrelation.
    """

    if not isinstance(
        series,
        np.ndarray,
    ):
        raise TypeError(
            "Input must be a numpy array."
        )

    if len(series) < 2:
        raise ValueError(
            "Series must contain at least two values."
        )

    x = series[:-1]
    y = series[1:]

    return float(
        np.corrcoef(
            x,
            y,
        )[0, 1]
    )


def red_noise_spectrum(
    frequencies: np.ndarray,
    *,
    lag1: float,
    dt: float = 1.0,
) -> np.ndarray:
    """
    Calculate AR(1) red-noise background spectrum.

    Based on Torrence & Compo (1998).
    """

    if not isinstance(
        frequencies,
        np.ndarray,
    ):
        raise TypeError(
            "Frequencies must be a numpy array."
        )

    return (
        (
            1 - lag1**2
        )
        /
        (
            1
            +
            lag1**2
            -
            2
            *
            lag1
            *
            np.cos(
                2
                *
                np.pi
                *
                frequencies
                *
                dt
            )
        )
    )


def wavelet_significance_level(
    variance: float,
    *,
    confidence: float = 0.95,
    dof: int = 2,
) -> float:
    """
    Calculate wavelet power significance level.

    Following Torrence & Compo (1998),
    using the chi-square distribution.

    Parameters
    ----------
    variance:
        Variance of the original series.

    confidence:
        Confidence level.

    dof:
        Degrees of freedom.
        Morlet wavelet default = 2.

    Returns
    -------
    float
        Significance power threshold.
    """

    from scipy.stats import chi2

    if variance <= 0:
        raise ValueError(
            "Variance must be positive."
        )

    if not 0 < confidence < 1:
        raise ValueError(
            "Confidence must be between 0 and 1."
        )

    if dof <= 0:
        raise ValueError(
            "Degrees of freedom must be positive."
        )

    chi_square = chi2.ppf(
        confidence,
        dof,
    )

    return (
        variance
        *
        chi_square
        /
        dof
    )