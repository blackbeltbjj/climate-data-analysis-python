"""
Tests for climate.time.report.
"""

import pandas as pd

from climate.time import time_series_report


def test_time_series_report_for_daily_series():
    series = pd.Series(
        [28.1, 28.2, 28.3],
        index=pd.date_range("2026-01-01", periods=3, freq="D"),
    )

    report = time_series_report(series)

    assert report.start == pd.Timestamp("2026-01-01")
    assert report.end == pd.Timestamp("2026-01-03")
    assert report.observations == 3
    assert report.frequency == "D"
    assert report.duplicated_timestamps == 0
    assert report.is_sorted is True
    assert report.is_datetime_index is True


def test_time_series_report_detects_duplicates():
    series = pd.Series(
        [28.1, 28.2, 28.3],
        index=pd.to_datetime(
            ["2026-01-01", "2026-01-01", "2026-01-02"]
        ),
    )

    report = time_series_report(series)

    assert report.duplicated_timestamps == 1
    assert report.frequency is None


def test_time_series_report_handles_empty_series():
    series = pd.Series(
        [],
        index=pd.DatetimeIndex([]),
        dtype=float,
    )

    report = time_series_report(series)

    assert report.start is None
    assert report.end is None
    assert report.observations == 0
    assert report.frequency is None