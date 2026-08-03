"""
Time-handling utilities for climate datasets.
"""

from climate.time.validation import (
    find_missing_timestamps,
    has_missing_timestamps,
    validate_datetime_index,
)

from climate.time.frequency import (
    infer_frequency,
)

__all__ = [
    "validate_datetime_index",
    "find_missing_timestamps",
    "has_missing_timestamps",
    "infer_frequency",
]