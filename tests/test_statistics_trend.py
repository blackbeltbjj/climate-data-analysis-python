import pandas as pd
import pytest

from climate.statistics import TrendReport, linear_trend


def test_linear_trend_returns_report():
    series = pd.Series([1, 2, 3, 4, 5], dtype=float)

    report = linear_trend(series)

    assert isinstance(report, TrendReport)


def test_linear_trend_positive_slope():
    series = pd.Series([1, 2, 3, 4, 5], dtype=float)

    report = linear_trend(series)

    assert report.slope == pytest.approx(1.0)
    assert report.r_squared > 0.99


def test_linear_trend_requires_series():
    with pytest.raises(TypeError):
        linear_trend([1, 2, 3])


def test_linear_trend_requires_two_points():
    series = pd.Series([1.0])

    with pytest.raises(ValueError):
        linear_trend(series)