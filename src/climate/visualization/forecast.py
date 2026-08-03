"""
Forecast visualization utilities.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_forecast(
    observed: pd.Series,
    forecast: pd.Series,
    *,
    title: str = "Forecast",
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    """
    Plot observed time series and forecast values.
    """

    if not isinstance(observed, pd.Series):
        raise TypeError("Observed values must be a pandas Series.")

    if not isinstance(forecast, pd.Series):
        raise TypeError("Forecast values must be a pandas Series.")

    fig, ax = plt.subplots(
        figsize=(10, 4),
    )

    ax.plot(
        observed.index,
        observed.values,
        label="Observed",
    )

    ax.plot(
        forecast.index,
        forecast.values,
        label="Forecast",
    )

    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    if save_path is not None:
        path = Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=300)

    if show:
        plt.show()

    return fig