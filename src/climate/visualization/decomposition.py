"""
STL decomposition plotting utilities.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from climate.statistics import STLReport


def plot_stl_decomposition(
    report: STLReport,
    *,
    title: str = "STL Decomposition",
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    """
    Plot trend, seasonal, and residual STL components.
    """
    if not isinstance(report, STLReport):
        raise TypeError("Input must be an STLReport.")

    fig, axes = plt.subplots(
        3,
        1,
        figsize=(10, 8),
        sharex=True,
    )

    axes[0].plot(report.trend.index, report.trend.values)
    axes[0].set_ylabel("Trend")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(report.seasonal.index, report.seasonal.values)
    axes[1].set_ylabel("Seasonal")
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(report.residual.index, report.residual.values)
    axes[2].set_ylabel("Residual")
    axes[2].set_xlabel("Date")
    axes[2].grid(True, alpha=0.3)

    fig.suptitle(title)
    fig.tight_layout()

    if save_path is not None:
        path = Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=300)

    if show:
        plt.show()

    return fig
