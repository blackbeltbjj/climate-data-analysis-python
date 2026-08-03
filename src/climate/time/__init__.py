"""
Time-handling utilities for climate datasets.
"""

from climate.time.validation import (
    find_missing_timestamps,
    has_missing_timestamps,
    validate_datetime_index,
)

__all__ = [
    "find_missing_timestamps",
    "has_missing_timestamps",
    "validate_datetime_index",
]