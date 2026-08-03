import numpy as np
import pandas as pd
import pytest

from climate.forecast import (
    ForecastEvaluation,
    evaluate_forecast,
)


def create_series():
    dates = pd.date_range(
        "2000-01-01",
        periods=20,
        freq="MS",
    )

    observed = pd.Series(
        np.arange(20),
        index=dates,
    )

    predicted = pd.Series(
        np.arange(20) + 1,
        index=dates,
    )

    return observed, predicted


def test_returns_report():
    observed, predicted = create_series()

    report = evaluate_forecast(
        observed,
        predicted,
    )

    assert isinstance(
        report,
        ForecastEvaluation,
    )


def test_metrics_are_positive():
    observed, predicted = create_series()

    report = evaluate_forecast(
        observed,
        predicted,
    )

    assert report.rmse > 0
    assert report.mae > 0


def test_bias():
    observed, predicted = create_series()

    report = evaluate_forecast(
        observed,
        predicted,
    )

    assert report.bias == 1.0


def test_invalid_input():
    with pytest.raises(TypeError):
        evaluate_forecast(
            [1, 2],
            [1, 2],
        )