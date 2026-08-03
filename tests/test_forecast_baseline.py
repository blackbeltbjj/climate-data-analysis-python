import numpy as np
import pandas as pd
import pytest

from climate.forecast import (
    mean_forecast,
    persistence_forecast,
)


def create_series():
    return pd.Series(
        np.arange(10),
        index=pd.date_range(
            "2000-01-01",
            periods=10,
            freq="MS",
        ),
    )


def test_persistence_length():
    forecast = persistence_forecast(
        create_series(),
        steps=5,
    )

    assert len(forecast) == 5


def test_persistence_value():
    forecast = persistence_forecast(
        create_series(),
        steps=5,
    )

    assert forecast.iloc[0] == 9


def test_mean_forecast():
    forecast = mean_forecast(
        create_series(),
        steps=5,
    )

    assert forecast.iloc[0] == 4.5


def test_invalid_input():
    with pytest.raises(TypeError):
        persistence_forecast([1, 2, 3])