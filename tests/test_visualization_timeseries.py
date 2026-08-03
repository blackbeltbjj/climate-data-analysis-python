import matplotlib

matplotlib.use("Agg")

import numpy as np
import pandas as pd
import pytest

from climate.visualization.timeseries import plot_time_series


def create_series():
    dates = pd.date_range(
        "2000-01-01",
        periods=100,
        freq="D",
    )

    values = np.random.default_rng(42).normal(size=100)

    return pd.Series(values, index=dates)


def test_returns_figure():
    figure = plot_time_series(create_series())

    assert figure is not None


def test_save_figure(tmp_path):
    filename = tmp_path / "timeseries.png"

    plot_time_series(
        create_series(),
        save_path=filename,
    )

    assert filename.exists()


def test_invalid_input():
    with pytest.raises(TypeError):
        plot_time_series([1, 2, 3])