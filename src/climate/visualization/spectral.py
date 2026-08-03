"""
Spectral plotting utilities.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from climate.statistics import SpectralReport


def plot_spectrum(
    report: SpectralReport,
    *,
    title: str = "Spectral Analysis",
    xlabel: str = "Frequency",
    ylabel: str = "Power",
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    """
    Plot a periodogram spectrum.
    """
    if not isinstance(report, SpectralReport):
        raise TypeError("Input must be a SpectralReport.")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(
        report.frequency,
        report.power,
        linewidth=1.5,
    )

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    if save_path is not None:
        path = Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=300)

    if show:
        plt.show()

    return fig
