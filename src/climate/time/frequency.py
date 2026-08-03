"""
Frequency utilities for climate time series.
"""

from __future__ import annotations

import pandas as pd

from climate.time.validation import validate_datetime_index


def infer_frequency(
    data: pd.Series | pd.DataFrame,
) -> str:
    """
    Infer the temporal frequency of a climate time series.

    Parameters
    ----------
    data
        Series or DataFrame with a valid DatetimeIndex.

    Returns
    -------
    str
        Pandas frequency alias, such as ``"D"``, ``"MS"``, or ``"YS"``.

    Raises
    ------
    ValueError
        If the frequency cannot be inferred.
    """
    validate_datetime_index(data)

    if len(data.index) < 3:
        raise ValueError(
            "At least three timestamps are required to infer frequency."
        )

    frequency = pd.infer_freq(data.index)

    if frequency is None:
        raise ValueError(
            "Could not infer a regular temporal frequency."
        )

    return frequency