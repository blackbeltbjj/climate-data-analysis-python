"""
Tests for Torrence & Compo (1998)
Morlet Continuous Wavelet Transform.
"""

import numpy as np
import pandas as pd

from climate.signal import (
    WaveletReport,
    cone_of_influence,
    morlet_cwt,
)


def create_series():

    time = pd.date_range(
        "2000-01-01",
        periods=256,
        freq="W",
    )

    signal = np.sin(
        2 * np.pi * np.arange(256) / 52
    )

    return pd.Series(
        signal,
        index=time,
    )


def test_morlet_cwt():

    wavelet, scales, periods, report = (
        morlet_cwt(
            create_series()
        )
    )

    assert isinstance(
        report,
        WaveletReport,
    )

    assert wavelet.shape[1] == 256
    assert len(scales) == len(periods)
    assert wavelet.shape[0] == len(scales)


def test_wavelet_is_complex():

    wavelet, _, _, _ = (
        morlet_cwt(
            create_series()
        )
    )

    assert np.iscomplexobj(
        wavelet
    )


def test_custom_sampling():

    _, scales, periods, report = (
        morlet_cwt(
            create_series(),
            dt=7,
        )
    )

    assert report.dt == 7
    assert len(scales) == len(periods)


def test_cone_of_influence():

    scales = np.arange(
        1,
        10,
    )

    coi = cone_of_influence(
        scales,
        n=256,
    )

    assert len(coi) == 256
    assert coi[0] < coi[128]