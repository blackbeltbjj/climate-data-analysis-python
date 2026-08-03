"""
Forecast evaluation metrics.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ForecastEvaluation:
    """Forecast accuracy metrics."""

    rmse: float
    mae: float
    bias: float
    correlation: float


def evaluate_forecast(
    observed: pd.Series,
    predicted: pd.Series,
) -> ForecastEvaluation:
    """
    Calculate forecast evaluation metrics.
    """

    if not isinstance(observed, pd.Series):
        raise TypeError("Observed values must be a pandas Series.")

    if not isinstance(predicted, pd.Series):
        raise TypeError("Predicted values must be a pandas Series.")

    aligned = pd.concat(
        [observed, predicted],
        axis=1,
        join="inner",
    ).dropna()

    if len(aligned) == 0:
        raise ValueError(
            "Observed and predicted series have no overlapping values."
        )

    errors = aligned.iloc[:, 1] - aligned.iloc[:, 0]

    rmse = float(
        np.sqrt(
            np.mean(errors**2)
        )
    )

    mae = float(
        np.mean(
            np.abs(errors)
        )
    )

    bias = float(
        np.mean(errors)
    )

    correlation = float(
        aligned.iloc[:, 0].corr(aligned.iloc[:, 1])
    )

    return ForecastEvaluation(
        rmse=rmse,
        mae=mae,
        bias=bias,
        correlation=correlation,
    )