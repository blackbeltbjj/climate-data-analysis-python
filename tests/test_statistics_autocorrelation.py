import numpy as np
import pandas as pd

from climate.statistics import (
    AutocorrelationReport,
    autocorrelation_report,
)


def create_series():
    np.random.seed(42)

    dates = pd.date_range(
        "2000-01-01",
        periods=200,
        freq="D",
    )

    values = np.random.normal(size=200)

    return pd.Series(values, index=dates)


def test_returns_report():
    report = autocorrelation_report(create_series())

    assert isinstance(report, AutocorrelationReport)


def test_lengths():
    report = autocorrelation_report(
        create_series(),
        nlags=20,
    )

    assert len(report.lags) == 21
    assert len(report.acf_values) == 21
    assert len(report.pacf_values) == 21


def test_first_acf_is_one():
    report = autocorrelation_report(create_series())

    assert report.acf_values[0] == 1.0


def test_first_pacf_is_one():
    report = autocorrelation_report(create_series())

    assert report.pacf_values[0] == 1.0
