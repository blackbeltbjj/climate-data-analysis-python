"""
Validation utilities for climate time series.

This module contains functions for checking datetime indices,
chronological ordering, duplicated timestamps, and temporal gaps.
"""

from __future__ import annotations

import pandas as pd


def validate_datetime_index(
    data: pd.Series | pd.DataFrame,
    *,
    require_unique: bool = True,
    require_sorted: bool = True,
) -> None:
    """
    Validate the datetime index of a pandas object.

    Parameters
    ----------
    data
        Series or DataFrame to validate.
    require_unique
        Raise an error when duplicated timestamps are present.
    require_sorted
        Raise an error when timestamps are not chronologically ordered.

    Raises
    ------
    TypeError
        If the index is not a pandas DatetimeIndex.
    ValueError
        If duplicated or unsorted timestamps are found.
    """
    if not isinstance(data.index, pd.DatetimeIndex):
        raise TypeError("The object index must be a pandas DatetimeIndex.")

    if require_unique and data.index.has_duplicates:
        duplicated = data.index[data.index.duplicated()].unique()
        raise ValueError(f"Duplicated timestamps found: {duplicated.tolist()}")

    if require_sorted and not data.index.is_monotonic_increasing:
        raise ValueError("The datetime index must be sorted chronologically.")


def find_missing_timestamps(
    data: pd.Series | pd.DataFrame,
    frequency: str,
) -> pd.DatetimeIndex:
    """
    Find missing timestamps in a regular time series.

    Parameters
    ----------
    data
        Series or DataFrame with a DatetimeIndex.
    frequency
        Expected pandas frequency (e.g. "D", "MS", "YS").

    Returns
    -------
    pandas.DatetimeIndex
        Missing timestamps between the first and last observations.
    """
    validate_datetime_index(data)

    if data.empty:
        return pd.DatetimeIndex([], dtype="datetime64[ns]")

    expected = pd.date_range(
        start=data.index.min(),
        end=data.index.max(),
        freq=frequency,
    )

    return expected.difference(data.index)


def has_missing_timestamps(
    data: pd.Series | pd.DataFrame,
    frequency: str,
) -> bool:
    """
    Check whether a regular time series contains temporal gaps.

    Parameters
    ----------
    data
        Series or DataFrame with a DatetimeIndex.
    frequency
        Expected pandas frequency.

    Returns
    -------
    bool
        True if one or more timestamps are missing.
    """
    return len(find_missing_timestamps(data, frequency)) > 0
