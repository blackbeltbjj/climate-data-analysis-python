"""
Tests for wavelet spectrum functions.
"""

import numpy as np

from climate.signal import (
    band_average_power,
    global_wavelet_spectrum,
)


def test_global_wavelet_spectrum():

    power = np.ones(
        (
            10,
            100,
        )
    )

    result = global_wavelet_spectrum(
        power
    )

    assert result.shape == (
        10,
    )


def test_band_average_power():

    power = np.ones(
        (
            10,
            100,
        )
    )

    periods = np.arange(
        10,
        110,
        10,
    )

    result = band_average_power(
        power,
        periods,
        period_min=20,
        period_max=40,
    )

    assert result.shape == (
        100,
    )