import pandas as pd
import pytest

from climate.ocean import (
    monthly_anomaly,
)


def create_series():

    return pd.Series(
        range(24),
        index=pd.date_range(
            "2000-01-01",
            periods=24,
            freq="MS",
        ),
    )


def test_monthly_anomaly():

    result = monthly_anomaly(
        create_series()
    )

    assert isinstance(
        result,
        pd.Series,
    )


def test_zero_monthly_mean():

    result = monthly_anomaly(
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
        monthly_anomaly(
            [1, 2, 3]
        )