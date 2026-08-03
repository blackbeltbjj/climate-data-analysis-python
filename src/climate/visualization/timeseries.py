"""
Time series plotting utilities.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_time_series(
    series: pd.Series,
    *,
    title: str = "",
    xlabel: str = "Date",
    ylabel: str = "",
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    """
    Create a publication-ready time series plot.

    Parameters
    ----------
    series
        Time series to plot.
    title
        Figure title.
    xlabel
        X-axis label.
    ylabel
        Y-axis label.
    save_path
        Optional output file.
    show
        Display the figure interactively.

    Returns
    -------
    matplotlib.figure.Figure
    """

    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series.")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(series.index, series.values, linewidth=1.5)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=300)

    if show:
        plt.show()

    return fig
