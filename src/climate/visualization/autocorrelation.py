"""
Autocorrelation plotting utilities.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from climate.statistics import AutocorrelationReport


def plot_autocorrelation(
    report: AutocorrelationReport,
    *,
    title: str = "Autocorrelation Analysis",
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    """
    Plot ACF and PACF values.
    """
    if not isinstance(report, AutocorrelationReport):
        raise TypeError("Input must be an AutocorrelationReport.")

    fig, axes = plt.subplots(
        2,
        1,
        figsize=(10, 7),
        sharex=True,
    )

    axes[0].stem(
        report.lags,
        report.acf_values,
        basefmt=" ",
    )
    axes[0].set_ylabel("ACF")
    axes[0].grid(True, alpha=0.3)

    axes[1].stem(
        report.lags,
        report.pacf_values,
        basefmt=" ",
    )
    axes[1].set_xlabel("Lag")
    axes[1].set_ylabel("PACF")
    axes[1].grid(True, alpha=0.3)

    fig.suptitle(title)
    fig.tight_layout()

    if save_path is not None:
        path = Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=300)

    if show:
        plt.show()

    return fig
