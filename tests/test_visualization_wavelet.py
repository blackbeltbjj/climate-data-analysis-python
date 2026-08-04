"""
Tests for wavelet visualization.
"""

import numpy as np

from climate.visualization import (
    wavelet_scalogram,
    plot_global_wavelet_spectrum,
)


def test_wavelet_scalogram():

    power = np.ones(
        (
            10,
            100,
        )
    )

    periods = np.arange(
        1,
        11,
    )

    coi = np.ones(
        100
    )

    ax = wavelet_scalogram(
        power,
        periods,
        coi=coi,
    )

    assert ax is not None


def test_global_spectrum_plot():

    spectrum = np.ones(
        10
    )

    periods = np.arange(
        1,
        11,
    )

    ax = plot_global_wavelet_spectrum(
        spectrum,
        periods,
        significance=1,
    )

    assert ax is not None