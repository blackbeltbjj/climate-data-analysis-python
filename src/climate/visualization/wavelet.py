"""
Wavelet visualization utilities.

Designed for Torrence & Compo (1998)
style wavelet analysis figures.
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

    ax.set_ylabel(
        "Period"
    )

    ax.set_xlabel(
        "Time"
    )

    ax.invert_yaxis()

    plt.colorbar(
        mesh,
        ax=ax,
        label="Wavelet Power",
    )

    return ax


def plot_global_wavelet_spectrum(
    spectrum: np.ndarray,
    periods: np.ndarray,
    *,
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

    ax.set_yscale(
        "log"
    )

    ax.set_xlabel(
        "Power"
    )

    ax.set_ylabel(
        "Period"
    )

    ax.invert_yaxis()

    return ax