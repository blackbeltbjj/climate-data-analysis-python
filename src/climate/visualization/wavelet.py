"""
Wavelet visualization utilities.

Torrence & Compo (1998) style plots:

- Wavelet power scalogram
- Global Wavelet Spectrum
- COI boundary
- Significance contours
- Band-averaged power
"""

from __future__ import annotations

import numpy as np

import matplotlib

matplotlib.use(
    "Agg"
)

import matplotlib.pyplot as plt


def wavelet_scalogram(
    power: np.ndarray,
    periods: np.ndarray,
    *,
    time=None,
    coi=None,
    significance=None,
    ax=None,
):
    """
    Plot wavelet power scalogram.
    """

    if ax is None:
        _, ax = plt.subplots()

    if time is None:
        time = np.arange(
            power.shape[1]
        )

    mesh = ax.contourf(
        time,
        periods,
        power,
        levels=50,
    )

    ax.set_yscale(
        "log"
    )

    ax.invert_yaxis()

    ax.set_xlabel(
        "Time"
    )

    ax.set_ylabel(
        "Period"
    )

    plt.colorbar(
        mesh,
        ax=ax,
        label="Wavelet Power",
    )

    if significance is not None:

        ax.contour(
            time,
            periods,
            significance,
            levels=[
                1,
            ],
            colors="k",
            linewidths=1,
        )

    if coi is not None:

        ax.plot(
            time,
            coi,
            "k--",
            linewidth=1,
        )

    return ax


def plot_global_wavelet_spectrum(
    spectrum: np.ndarray,
    periods: np.ndarray,
    *,
    significance=None,
    ax=None,
):
    """
    Plot Global Wavelet Spectrum.
    """

    if ax is None:
        _, ax = plt.subplots()

    ax.plot(
        spectrum,
        periods,
    )

    if significance is not None:

        ax.axvline(
            significance,
            linestyle="--",
        )

    ax.set_yscale(
        "log"
    )

    ax.invert_yaxis()

    ax.set_xlabel(
        "Power"
    )

    ax.set_ylabel(
        "Period"
    )

    return ax


def plot_band_power(
    power: np.ndarray,
    *,
    time=None,
    label="Band-averaged wavelet power",
    ax=None,
):
    """
    Plot scale-averaged wavelet power.

    Used for annual-cycle intensity analysis.
    """

    if ax is None:
        _, ax = plt.subplots()

    if time is None:
        time = np.arange(
            len(power)
        )

    ax.plot(
        time,
        power,
    )

    ax.set_xlabel(
        "Time"
    )

    ax.set_ylabel(
        label
    )

    return ax