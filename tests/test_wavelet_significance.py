"""
Tests for Torrence & Compo significance methods.
"""

import numpy as np
import pytest

from climate.signal import (
    lag1_autocorrelation,
    red_noise_spectrum,
    wavelet_significance_level,
)


def test_lag1_autocorrelation():

    data = np.array(
        [
            1,
            2,
            3,
            4,
            5,
        ]
    )

    result = lag1_autocorrelation(
        data
    )

    assert result > 0


def test_red_noise():

    frequencies = np.linspace(
        0,
        0.5,
        10,
    )

    result = red_noise_spectrum(
        frequencies,
        lag1=0.5,
    )

    assert len(result) == 10


def test_wavelet_significance_level():

    result = wavelet_significance_level(
        variance=1.0
    )

    assert result > 1.0


def test_invalid_input():

    with pytest.raises(TypeError):

        lag1_autocorrelation(
            [1, 2, 3]
        )