"""
Continuous Wavelet Transform following
Torrence & Compo (1998).

Implements:
- Complex Morlet wavelet
- Scale calculation
- Fourier equivalent periods
- Wavelet coefficients
- Cone of Influence (COI)
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class WaveletReport:
    """
    Metadata from CWT calculation.
    """

    observations: int
    scales: int
    dt: float
    omega0: float


def morlet_cwt(
    series: pd.Series,
    *,
    dt: float = 1.0,
    dj: float = 0.25,
    s0: float | None = None,
    J: int | None = None,
    omega0: float = 6.0,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    WaveletReport,
]:
    """
    Continuous Wavelet Transform using
    the complex Morlet wavelet.

    Based on Torrence & Compo (1998).

    Parameters
    ----------
    series:
        Input time series.

    dt:
        Sampling interval.

    dj:
        Scale resolution.

    s0:
        Smallest scale.

    J:
        Number of scales.

    omega0:
        Morlet nondimensional frequency.

    Returns
    -------
    wavelet:
        Complex wavelet coefficients.

    scales:
        Wavelet scales.

    periods:
        Fourier equivalent periods.

    report:
        Wavelet metadata.
    """

    if not isinstance(
        series,
        pd.Series,
    ):
        raise TypeError(
            "Input must be a pandas Series."
        )

    data = series.dropna().values

    if len(data) == 0:
        raise ValueError(
            "Series cannot be empty."
        )

    n = len(data)

    data = data - np.mean(data)

    std = np.std(data)

    if std == 0:
        raise ValueError(
            "Series standard deviation cannot be zero."
        )

    data = data / std

    if s0 is None:
        s0 = 2 * dt

    if J is None:
        J = int(
            np.log2(
                n * dt / s0
            )
            / dj
        )

    scales = (
        s0
        *
        2 ** (
            np.arange(J + 1)
            * dj
        )
    )

    fourier_factor = (
        4
        *
        np.pi
        /
        (
            omega0
            +
            np.sqrt(
                2
                +
                omega0**2
            )
        )
    )

    periods = (
        scales
        *
        fourier_factor
    )

    fft = np.fft.fft(
        data
    )

    frequencies = (
        2
        *
        np.pi
        *
        np.fft.fftfreq(
            n,
            d=dt,
        )
    )

    wavelet = np.zeros(
        (
            len(scales),
            n,
        ),
        dtype=complex,
    )

    for index, scale in enumerate(scales):

        daughter = np.zeros_like(
            frequencies,
            dtype=complex,
        )

        positive = frequencies > 0

        daughter[positive] = (
            np.sqrt(
                scale
                *
                frequencies[positive]
            )
            *
            np.exp(
                -(
                    (
                        scale
                        *
                        frequencies[positive]
                        -
                        omega0
                    )
                    ** 2
                )
                /
                2
            )
        )

        wavelet[index, :] = np.fft.ifft(
            fft * daughter
        )

    report = WaveletReport(
        observations=n,
        scales=len(scales),
        dt=dt,
        omega0=omega0,
    )

    return (
        wavelet,
        scales,
        periods,
        report,
    )


def cone_of_influence(
    scales: np.ndarray,
    n: int,
    *,
    dt: float = 1.0,
) -> np.ndarray:
    """
    Calculate the Cone of Influence.

    Following Torrence & Compo (1998),
    the e-folding time for the Morlet wavelet
    is sqrt(2) times the wavelet scale.

    Parameters
    ----------
    scales:
        Wavelet scales.

    n:
        Number of observations.

    dt:
        Sampling interval.

    Returns
    -------
    numpy.ndarray
        COI period at each time point.
    """

    if not isinstance(
        scales,
        np.ndarray,
    ):
        raise TypeError(
            "Scales must be a numpy array."
        )

    if n <= 0:
        raise ValueError(
            "Number of observations must be positive."
        )

    coi = np.minimum(
        np.arange(n) + 1,
        np.arange(n)[::-1] + 1,
    )

    coi = (
        np.sqrt(2)
        *
        coi
        *
        dt
    )

    return coi