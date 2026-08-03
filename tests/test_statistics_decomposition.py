import numpy as np
import pandas as pd

from climate.statistics import STLReport, stl_decompose


def create_series():
    dates = pd.date_range(
        "2000-01-01",
        periods=120,
        freq="MS",
    )

    trend = np.linspace(0, 2, 120)
    seasonal = np.sin(2 * np.pi * np.arange(120) / 12)

    values = trend + seasonal

    return pd.Series(values, index=dates)


def test_returns_report():
    report = stl_decompose(create_series())

    assert isinstance(report, STLReport)


def test_component_lengths():
    report = stl_decompose(create_series())

    assert len(report.trend) == 120
    assert len(report.seasonal) == 120
    assert len(report.residual) == 120


def test_preserves_datetime_index():
    series = create_series()

    report = stl_decompose(series)

    assert report.trend.index.equals(series.index)
    assert report.seasonal.index.equals(series.index)
    assert report.residual.index.equals(series.index)