import matplotlib

matplotlib.use("Agg")

import numpy as np
import pandas as pd
import pytest

from climate.statistics import autocorrelation_report
from climate.visualization.autocorrelation import plot_autocorrelation


def create_report():
    rng = np.random.default_rng(42)

    series = pd.Series(
        rng.normal(size=200),
        index=pd.date_range(
            "2000-01-01",
            periods=200,
            freq="D",
        ),
    )

    return autocorrelation_report(series, nlags=20)


def test_returns_figure():
    figure = plot_autocorrelation(create_report())

    assert figure is not None


def test_has_two_axes():
    figure = plot_autocorrelation(create_report())

    assert len(figure.axes) == 2


def test_save_figure(tmp_path):
    filename = tmp_path / "autocorrelation.png"

    plot_autocorrelation(
        create_report(),
        save_path=filename,
    )

    assert filename.exists()


def test_invalid_input():
    with pytest.raises(TypeError):
        plot_autocorrelation([])
