"""
Tests for climate.time.frequency.
"""

import pandas as pd
import pytest

from climate.time import infer_frequency


def test_infer_daily_frequency():
    series = pd.Series(
        [28.1, 28.2, 28.3],
        index=pd.date_range("2026-01-01", periods=3, freq="D"),
    )

    assert infer_frequency(series) == "D"


def test_infer_monthly_frequency():
    series = pd.Series(
        [28.1, 28.2, 28.3],
        index=pd.date_range("2026-01-01", periods=3, freq="MS"),
    )

    assert infer_frequency(series) == "MS"


def test_infer_frequency_requires_three_timestamps():
    series = pd.Series(
        [28.1, 28.2],
        index=pd.date_range("2026-01-01", periods=2, freq="D"),
    )

    with pytest.raises(ValueError, match="At least three timestamps"):
        infer_frequency(series)


def test_infer_frequency_rejects_irregular_series():
    index = pd.to_datetime(["2026-01-01", "2026-01-02", "2026-01-04"])
    series = pd.Series([28.1, 28.2, 28.4], index=index)

    with pytest.raises(
        ValueError,
        match="Could not infer a regular temporal frequency",
    ):
        infer_frequency(series)
