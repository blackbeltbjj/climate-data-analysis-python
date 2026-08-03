import matplotlib

matplotlib.use("Agg")

import numpy as np
import pandas as pd
import pytest

from climate.statistics import spectral_report
from climate.visualization.spectral import plot_spectrum


def create_report():
    rng = np.random.default_rng(42)

    series = pd.Series(
        rng.normal(size=256),
        index=pd.date_range(
            "2000-01-01",
            periods=256,
            freq="D",
        ),
    )

    return spectral_report(series)


def test_returns_figure():
    figure = plot_spectrum(create_report())

    assert figure is not None


def test_has_one_axis():
    figure = plot_spectrum(create_report())

    assert len(figure.axes) == 1


def test_save_figure(tmp_path):
    filename = tmp_path / "spectrum.png"

    plot_spectrum(
        create_report(),
        save_path=filename,
    )

    assert filename.exists()


def test_invalid_input():
    with pytest.raises(TypeError):
        plot_spectrum([])