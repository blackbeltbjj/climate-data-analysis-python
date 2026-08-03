"""
Forecasting example.

Demonstrates:
- ARIMA forecasting
- Forecast evaluation
"""

import numpy as np
import pandas as pd

from climate.forecast import (
    arima_forecast,
    persistence_forecast,
    evaluate_forecast,
)


def main():
    dates = pd.date_range(
        "2000-01-01",
        periods=120,
        freq="MS",
    )

    values = (
        np.linspace(0, 5, 120)
        + np.sin(2 * np.pi * np.arange(120) / 12)
    )

    series = pd.Series(
        values,
        index=dates,
    )

    train = series.iloc[:-12]
    test = series.iloc[-12:]

    model = arima_forecast(
        train,
        steps=12,
    )

    forecast = pd.Series(
        model.forecast.values,
        index=test.index,
    )

    evaluation = evaluate_forecast(
        test,
        forecast,
    )

    baseline = persistence_forecast(
        train,
        steps=12,
    )

    print("ARIMA evaluation")
    print("----------------")
    print(evaluation)

    print()
    print("Persistence baseline")
    print("-------------------")
    print(baseline)


if __name__ == "__main__":
    main()