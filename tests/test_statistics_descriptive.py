"""
Tests for climate.statistics.descriptive.
"""

import pandas as pd
import pytest

from climate.statistics import (
    StatisticsReport,
    describe,
)


def test_describe_returns_statistics_report():
    series = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])

    report = describe(series)

    assert isinstance(report, StatisticsReport)


def test_describe_basic_statistics():
    series = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])

    report = describe(series)

    assert report.observations == 5
    assert report.missing == 0

    assert report.mean == pytest.approx(3.0)
    assert report.median == pytest.approx(3.0)

    assert report.minimum == pytest.approx(1.0)
    assert report.maximum == pytest.approx(5.0)

    assert report.variance == pytest.approx(series.var())
    assert report.standard_deviation == pytest.approx(series.std())

    assert report.skewness == pytest.approx(series.skew())
    assert report.kurtosis == pytest.approx(series.kurt())


def test_describe_counts_missing_values():
    series = pd.Series([1.0, None, 3.0, None, 5.0])

    report = describe(series)

    assert report.observations == 5
    assert report.missing == 2
    assert report.mean == pytest.approx(3.0)


def test_describe_rejects_invalid_input():
    with pytest.raises(TypeError):
        describe([1, 2, 3])


def test_statistics_report_to_dict():
    series = pd.Series([1.0, 2.0, 3.0])

    report = describe(series)

    d = report.to_dict()

    assert d["observations"] == 3
    assert d["mean"] == pytest.approx(2.0)
    assert "standard_deviation" in d
    