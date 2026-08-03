import numpy as np
import pandas as pd

from climate.statistics import (
    CrossCorrelationReport,
    cross_correlation_report,
)


def create_series():
    np.random.seed(42)

    dates = pd.date_range(
        "2000-01-01",
        periods=200,
        freq="D",
    )

    x = pd.Series(
        np.random.normal(size=200),
        index=dates,
    )

    y = x.shift(3).fillna(0)

    return x, y


def test_returns_report():
    x, y = create_series()

    report = cross_correlation_report(x, y)

    assert isinstance(report, CrossCorrelationReport)


def test_lengths():
    x, y = create_series()

    report = cross_correlation_report(
        x,
        y,
        max_lag=20,
    )

    assert len(report.lags) == 41
    assert len(report.correlations) == 41


def test_zero_lag_is_float():
    x, y = create_series()

    report = cross_correlation_report(x, y)

    assert isinstance(report.zero_lag_correlation, float)


def test_maximum_lag_is_valid():
    x, y = create_series()

    report = cross_correlation_report(x, y)

    assert report.max_correlation_lag in report.lags
