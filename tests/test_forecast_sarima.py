import numpy as np
import pandas as pd
import pytest

from climate.forecast import (
    SARIMAForecastReport,
    sarima_forecast,
)


def create_series():
    values = (
        np.linspace(0, 10, 120)
        + np.sin(2 * np.pi * np.arange(120) / 12)
    )

    return pd.Series(
        values,
        index=pd.date_range(
            "2000-01-01",
            periods=120,
            freq="MS",
        ),
    )


def test_returns_report():
    report = sarima_forecast(create_series())

    assert isinstance(
        report,
        SARIMAForecastReport,
    )


def test_forecast_length():
    report = sarima_forecast(
        create_series(),
        steps=12,
    )

    assert len(report.forecast) == 12


def test_seasonal_order():
    report = sarima_forecast(
        create_series(),
        seasonal_order=(1, 0, 1, 12),
    )

    assert report.seasonal_order == (1, 0, 1, 12)


def test_invalid_input():
    with pytest.raises(TypeError):
        sarima_forecast([1, 2, 3])