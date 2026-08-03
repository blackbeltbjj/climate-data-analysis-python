"""
Tests for climate.time.validation.
"""

import pandas as pd
import pytest

from climate.time import (
    find_missing_timestamps,
    has_missing_timestamps,
    validate_datetime_index,
)


def test_validate_datetime_index_accepts_valid_index():
    series = pd.Series(
        [28.1, 28.4, 28.7],
        index=pd.date_range("2026-01-01", periods=3, freq="D"),
    )

    validate_datetime_index(series)


def test_validate_datetime_index_rejects_non_datetime_index():
    series = pd.Series([28.1, 28.4], index=[0, 1])

    with pytest.raises(TypeError):
        validate_datetime_index(series)


def test_validate_datetime_index_rejects_duplicates():
    index = pd.to_datetime(
        ["2026-01-01", "2026-01-01", "2026-01-02"]
    )
    series = pd.Series([28.1, 28.2, 28.4], index=index)

    with pytest.raises(ValueError, match="Duplicated timestamps"):
        validate_datetime_index(series)


def test_validate_datetime_index_rejects_unsorted_index():
    index = pd.to_datetime(
        ["2026-01-02", "2026-01-01", "2026-01-03"]
    )
    series = pd.Series([28.2, 28.1, 28.4], index=index)

    with pytest.raises(ValueError, match="sorted chronologically"):
        validate_datetime_index(series)


def test_find_missing_daily_timestamp():
    index = pd.to_datetime(
        ["2026-01-01", "2026-01-02", "2026-01-04"]
    )
    series = pd.Series([28.1, 28.2, 28.4], index=index)

    missing = find_missing_timestamps(series, frequency="D")

    expected = pd.DatetimeIndex(["2026-01-03"])
    pd.testing.assert_index_equal(missing, expected)


def test_find_missing_monthly_timestamp():
    index = pd.to_datetime(
        ["2026-01-01", "2026-02-01", "2026-04-01"]
    )
    series = pd.Series([28.1, 28.2, 28.4], index=index)

    missing = find_missing_timestamps(series, frequency="MS")

    expected = pd.DatetimeIndex(["2026-03-01"])
    pd.testing.assert_index_equal(missing, expected)


def test_has_missing_timestamps_returns_true():
    index = pd.to_datetime(
        ["2026-01-01", "2026-01-03"]
    )
    series = pd.Series([28.1, 28.4], index=index)

    assert has_missing_timestamps(series, frequency="D") is True


def test_has_missing_timestamps_returns_false():
    series = pd.Series(
        [28.1, 28.2, 28.4],
        index=pd.date_range("2026-01-01", periods=3, freq="D"),
    )

    assert has_missing_timestamps(series, frequency="D") is False