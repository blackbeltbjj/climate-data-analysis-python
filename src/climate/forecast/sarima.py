"""
SARIMA forecasting utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX


@dataclass(frozen=True)
class SARIMAForecastReport:
    """Container for SARIMA forecast results."""

    forecast: pd.Series
    order: tuple[int, int, int]
    seasonal_order: tuple[int, int, int, int]


def sarima_forecast(
    series: pd.Series,
    *,
    order: tuple[int, int, int] = (1, 0, 0),
    seasonal_order: tuple[int, int, int, int] = (1, 0, 0, 12),
    steps: int = 12,
) -> SARIMAForecastReport:
    """
    Fit a SARIMA model and generate forecasts.
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

    model = SARIMAX(
        clean,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=False,
        enforce_invertibility=False,
    )

    fitted = model.fit(
        disp=False,
    )

    forecast = fitted.forecast(
        steps=steps,
    )

    return SARIMAForecastReport(
        forecast=forecast,
        order=order,
        seasonal_order=seasonal_order,
    )