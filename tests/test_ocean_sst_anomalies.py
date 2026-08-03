import pandas as pd
import pytest

from climate.ocean import monthly_sst_anomalies


def create_series():

    dates = pd.date_range(
        "2000-01-01",
        periods=24,
        freq="MS",
    )

    values = [
        20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31,
        21, 22, 23, 24, 25, 26,
        27, 28, 29, 30, 31, 32,
    ]

    return pd.Series(
        values,
        index=dates,
    )


def test_returns_series():

    result = monthly_sst_anomalies(
        create_series()
    )

    assert isinstance(
        result,
        pd.Series,
    )


def test_monthly_mean_is_zero():

    result = monthly_sst_anomalies(
        create_series()
    )

    means = result.groupby(
        result.index.month
    ).mean()

    assert all(
        abs(means) < 1e-10
    )


def test_invalid_input():

    with pytest.raises(TypeError):
        monthly_sst_anomalies(
            [20, 21]
        )


def test_invalid_index():

    with pytest.raises(TypeError):
        monthly_sst_anomalies(
            pd.Series([20, 21])
        )