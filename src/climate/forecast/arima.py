"""
ARIMA forecasting utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


@dataclass(frozen=True)
class ForecastReport:
    """Container for forecast results."""

    forecast: pd.Series
    model_order: tuple[int, int, int]


def arima_forecast(
    series: pd.Series,
    *,
    order: tuple[int, int, int] = (1, 0, 0),
    steps: int = 12,
) -> ForecastReport:
    """
    Fit an ARIMA model and generate forecasts.
    """
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    clean = series.dropna()

    if len(clean) <= steps:
        raise ValueError(
            "Series length must be greater than forecast steps."
        )

    if steps <= 0:
        raise ValueError(
            "Forecast steps must be positive."
        )

    model = ARIMA(
        clean,
        order=order,
    )

    fitted = model.fit()

    forecast = fitted.forecast(
        steps=steps,
    )

    return ForecastReport(
        forecast=forecast,
        model_order=order,
    )