import numpy as np
import pandas as pd

from climate.statistics import (
    SeasonalityReport,
    monthly_anomalies,
    monthly_climatology,
    seasonality_report,
)


def create_series():
    dates = pd.date_range(
        "2020-01-01",
        periods=24,
        freq="MS",
    )

    values = np.arange(24, dtype=float)

    return pd.Series(values, index=dates)


def test_monthly_climatology():
    series = create_series()

    clim = monthly_climatology(series)

    assert len(clim) == 12
    assert clim.loc[1] == 6.0


def test_monthly_anomalies():
    series = create_series()

    anom = monthly_anomalies(series)

    assert np.isclose(anom.groupby(anom.index.month).mean(), 0.0).all()


def test_report():
    report = seasonality_report(create_series())

    assert isinstance(report, SeasonalityReport)


def test_report_lengths():
    report = seasonality_report(create_series())

    assert len(report.climatology) == 12
    assert len(report.anomalies) == 24