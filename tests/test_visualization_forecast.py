import matplotlib

matplotlib.use("Agg")

import numpy as np
import pandas as pd
import pytest

from climate.visualization.forecast import plot_forecast


def create_series():
    observed = pd.Series(
        np.arange(20),
        index=pd.date_range(
            "2000-01-01",
            periods=20,
            freq="MS",
        ),
    )

    forecast = pd.Series(
        np.arange(5) + 20,
        index=pd.date_range(
            "2021-09-01",
            periods=5,
            freq="MS",
        ),
    )

    return observed, forecast


def test_returns_figure():
    observed, forecast = create_series()

    figure = plot_forecast(
        observed,
        forecast,
    )

    assert figure is not None


def test_has_one_axis():
    observed, forecast = create_series()

    figure = plot_forecast(
        observed,
        forecast,
    )

    assert len(figure.axes) == 1


def test_save_figure(tmp_path):
    observed, forecast = create_series()

    filename = tmp_path / "forecast.png"

    plot_forecast(
        observed,
        forecast,
        save_path=filename,
    )

    assert filename.exists()


def test_invalid_input():
    with pytest.raises(TypeError):
        plot_forecast(
            [1, 2, 3],
            [4, 5, 6],
        )