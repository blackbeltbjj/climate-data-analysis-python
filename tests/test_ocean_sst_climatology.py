import pandas as pd
import pytest

from climate.ocean import monthly_sst_climatology


def create_series():

    dates = pd.date_range(
        "2000-01-01",
        periods=24,
        freq="MS",
    )

    values = range(24)

    return pd.Series(
        values,
        index=dates,
    )


def test_returns_series():

    result = monthly_sst_climatology(
        create_series()
    )

    assert isinstance(
        result,
        pd.Series,
    )


def test_has_12_months():

    result = monthly_sst_climatology(
        create_series()
    )

    assert len(result) == 12


def test_invalid_input():

    with pytest.raises(TypeError):
        monthly_sst_climatology(
            [1, 2, 3]
        )