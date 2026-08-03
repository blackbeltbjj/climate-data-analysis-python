import numpy as np
import pandas as pd
import pytest

from climate.forecast import (
    ForecastReport,
    arima_forecast,
)


def create_series():
    values = np.linspace(
        0,
        10,
        100,
    )

    return pd.Series(
        values,
        index=pd.date_range(
            "2000-01-01",
            periods=100,
            freq="MS",
        ),
    )


def test_returns_report():
    report = arima_forecast(create_series())

    assert isinstance(report, ForecastReport)


def test_forecast_length():
    report = arima_forecast(
        create_series(),
        steps=12,
    )

    assert len(report.forecast) == 12


def test_model_order():
    report = arima_forecast(
        create_series(),
        order=(2, 0, 1),
    )

    assert report.model_order == (2, 0, 1)


def test_invalid_input():
    with pytest.raises(TypeError):
        arima_forecast([1, 2, 3])