"""
Wavelet spectra following
Torrence & Compo (1998).
"""

from __future__ import annotations

import numpy as np


def wavelet_power(
    wavelet: np.ndarray,
) -> np.ndarray:
    """
    Calculate wavelet power.

    Power = |W(t,s)|²
    """

    if not isinstance(
        wavelet,
        np.ndarray,
    ):
        raise TypeError(
            "Input must be a numpy array."
        )

    if not np.iscomplexobj(
        wavelet
    ):
        raise ValueError(
            "Wavelet coefficients must be complex."
        )

    return np.abs(
        wavelet
    ) ** 2


def global_wavelet_spectrum(
    wavelet_power_array: np.ndarray,
) -> np.ndarray:
    """
    Calculate Global Wavelet Spectrum.

    GWS(s) = mean(|W(t,s)|²)
    """

    if not isinstance(
        wavelet_power_array,
        np.ndarray,
    ):
        raise TypeError(
            "Input must be a numpy array."
        )

    if wavelet_power_array.ndim != 2:
        raise ValueError(
            "Wavelet power must be 2-dimensional."
        )

    return np.mean(
        wavelet_power_array,
        axis=1,
    )


def band_average_power(
    power: np.ndarray,
    periods: np.ndarray,
    *,
    period_min: float,
    period_max: float,
) -> np.ndarray:
    """
    Calculate scale-averaged wavelet power.

    Following Torrence & Compo (1998).

    Parameters
    ----------
    power:
        Wavelet power matrix
        (scale x time).

    periods:
        Fourier equivalent periods.

    period_min:
        Minimum period.

    period_max:
        Maximum period.

    Returns
    -------
    numpy.ndarray
        Time series of averaged band power.
    """

    if not isinstance(
        power,
        np.ndarray,
    ):
        raise TypeError(
            "Power must be a numpy array."
        )

    if not isinstance(
        periods,
        np.ndarray,
    ):
        raise TypeError(
            "Periods must be a numpy array."
        )

    if power.ndim != 2:
        raise ValueError(
            "Power must be 2-dimensional."
        )

    if len(periods) != power.shape[0]:
        raise ValueError(
            "Periods must match power scales."
        )

    selected = (
        (periods >= period_min)
        &
        (periods <= period_max)
    )

    if not np.any(selected):
        raise ValueError(
            "No periods found in requested band."
        )

    return np.mean(
        power[selected, :],
        axis=0,
    )