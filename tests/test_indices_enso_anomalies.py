import pandas as pd
import pytest

from climate.indices import monthly_anomalies


def create_series():
    dates = pd.date_range(
        "2000-01-01",
        periods=24,
        freq="MS",
    )

    values = [
        1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12,
        2, 3, 4, 5, 6, 7,
        8, 9, 10, 11, 12, 13,
    ]

    return pd.Series(
        values,
        index=dates,
    )


def test_returns_series():
    result = monthly_anomalies(
        create_series()
    )

    assert isinstance(
        result,
        pd.Series,
    )


def test_anomaly_mean_zero_by_month():
    result = monthly_anomalies(
        create_series()
    )

    monthly_mean = result.groupby(
        result.index.month
    ).mean()

    assert all(
        abs(monthly_mean) < 1e-10
    )


def test_invalid_input():
    with pytest.raises(TypeError):
        monthly_anomalies([1, 2, 3])


def test_invalid_index():
    with pytest.raises(TypeError):
        monthly_anomalies(
            pd.Series([1, 2, 3])
        )