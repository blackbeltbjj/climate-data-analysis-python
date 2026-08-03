"""
Tests for climate.time.resample.
"""

import pandas as pd
import pytest

from climate.time import (
    daily_to_annual,
    daily_to_monthly,
    monthly_to_annual,
)


def test_daily_to_monthly_mean():
    series = pd.Series(
        [20.0, 22.0, 24.0, 26.0],
        index=pd.to_datetime(
            [
                "2026-01-01",
                "2026-01-02",
                "2026-02-01",
                "2026-02-02",
            ]
        ),
    )

    result = daily_to_monthly(series)

    expected = pd.Series(
        [21.0, 25.0],
        index=pd.to_datetime(["2026-01-01", "2026-02-01"]),
    )
    expected.index.freq = "MS"

    pd.testing.assert_series_equal(result, expected)


def test_monthly_to_annual_mean():
    series = pd.Series(
        range(1, 13),
        index=pd.date_range("2026-01-01", periods=12, freq="MS"),
        dtype=float,
    )

    result = monthly_to_annual(series)

    assert result.iloc[0] == pytest.approx(6.5)
    assert result.index[0] == pd.Timestamp("2026-01-01")


def test_daily_to_annual_sum():
    series = pd.Series(
        [1.0, 2.0, 3.0],
        index=pd.date_range("2026-01-01", periods=3, freq="D"),
    )

    result = daily_to_annual(series, aggregation="sum")

    assert result.iloc[0] == pytest.approx(6.0)


def test_resampling_rejects_invalid_aggregation():
    series = pd.Series(
        [1.0, 2.0, 3.0],
        index=pd.date_range("2026-01-01", periods=3, freq="D"),
    )

    with pytest.raises(ValueError, match="Unsupported aggregation"):
        daily_to_monthly(series, aggregation="invalid")
