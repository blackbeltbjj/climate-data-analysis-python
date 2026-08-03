import numpy as np
import pandas as pd

from climate.statistics import (
    SpectralReport,
    spectral_report,
)


def create_series():
    np.random.seed(42)

    dates = pd.date_range(
        "2000-01-01",
        periods=256,
        freq="D",
    )

    values = np.random.normal(size=256)

    return pd.Series(values, index=dates)


def test_returns_report():
    report = spectral_report(create_series())

    assert isinstance(report, SpectralReport)


def test_frequency_and_power_have_same_length():
    report = spectral_report(create_series())

    assert len(report.frequency) == len(report.power)


def test_frequency_starts_at_zero():
    report = spectral_report(create_series())

    assert report.frequency[0] == 0.0


def test_power_is_non_negative():
    report = spectral_report(create_series())

    assert np.all(report.power >= 0.0)