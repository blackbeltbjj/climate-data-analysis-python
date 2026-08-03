import matplotlib

matplotlib.use("Agg")

import numpy as np
import pandas as pd
import pytest

from climate.statistics import stl_decompose
from climate.visualization.decomposition import plot_stl_decomposition


def create_report():
    dates = pd.date_range(
        "2000-01-01",
        periods=120,
        freq="MS",
    )

    values = np.linspace(0, 2, 120) + np.sin(2 * np.pi * np.arange(120) / 12)

    series = pd.Series(values, index=dates)

    return stl_decompose(series)


def test_returns_figure():
    figure = plot_stl_decomposition(create_report())

    assert figure is not None


def test_has_three_axes():
    figure = plot_stl_decomposition(create_report())

    assert len(figure.axes) == 3


def test_save_figure(tmp_path):
    filename = tmp_path / "stl_decomposition.png"

    plot_stl_decomposition(
        create_report(),
        save_path=filename,
    )

    assert filename.exists()


def test_invalid_input():
    with pytest.raises(TypeError):
        plot_stl_decomposition([])
