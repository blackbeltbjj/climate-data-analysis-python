"""
Summary reporting utilities for climate time series.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import pandas as pd

from climate.time.frequency import infer_frequency


@dataclass(frozen=True)
class TimeSeriesReport:
    """
    Summary information describing a time series index.
    """

    start: pd.Timestamp | None
    end: pd.Timestamp | None
    observations: int
    frequency: str | None
    duplicated_timestamps: int
    is_sorted: bool
    is_datetime_index: bool

    def to_dict(self) -> dict[str, object]:
        """
        Convert the report to a dictionary.
        """
        return asdict(self)


def time_series_report(
    data: pd.Series | pd.DataFrame,
) -> TimeSeriesReport:
    """
    Create a structural summary of a pandas time series.

    Unlike strict validation functions, this function reports problems
    instead of raising errors for duplicated or unsorted timestamps.
    """
    index = data.index
    is_datetime = isinstance(index, pd.DatetimeIndex)

    if len(index) == 0:
        return TimeSeriesReport(
            start=None,
            end=None,
            observations=0,
            frequency=None,
            duplicated_timestamps=0,
            is_sorted=True,
            is_datetime_index=is_datetime,
        )

    duplicates = int(index.duplicated().sum())
    is_sorted = bool(index.is_monotonic_increasing)

    frequency = None
    if is_datetime and duplicates == 0 and is_sorted and len(index) >= 3:
        try:
            frequency = infer_frequency(data)
        except ValueError:
            frequency = None

    return TimeSeriesReport(
        start=index.min() if is_datetime else None,
        end=index.max() if is_datetime else None,
        observations=len(index),
        frequency=frequency,
        duplicated_timestamps=duplicates,
        is_sorted=is_sorted,
        is_datetime_index=is_datetime,
    )
