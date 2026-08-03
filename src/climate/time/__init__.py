"""
Time-handling utilities for climate datasets.
"""

from climate.time.frequency import infer_frequency
from climate.time.report import TimeSeriesReport, time_series_report
from climate.time.resample import (
    daily_to_annual,
    daily_to_monthly,
    monthly_to_annual,
)
from climate.time.validation import (
    find_missing_timestamps,
    has_missing_timestamps,
    validate_datetime_index,
)

__all__ = [
    "TimeSeriesReport",
    "daily_to_annual",
    "daily_to_monthly",
    "find_missing_timestamps",
    "has_missing_timestamps",
    "infer_frequency",
    "monthly_to_annual",
    "time_series_report",
    "validate_datetime_index",
]