import numpy as np
import pandas as pd

from climate.statistics import (
    StationarityReport,
    adf_test,
    kpss_test,
)


def create_stationary_series():
    np.random.seed(42)

    return pd.Series(
        np.random.normal(size=300),
        index=pd.date_range(
            "2000-01-01",
            periods=300,
            freq="D",
        ),
    )


def test_adf_returns_report():
    report = adf_test(create_stationary_series())

    assert isinstance(report, StationarityReport)
    assert report.test == "ADF"


def test_kpss_returns_report():
    report = kpss_test(create_stationary_series())

    assert isinstance(report, StationarityReport)
    assert report.test == "KPSS"


def test_adf_pvalue_range():
    report = adf_test(create_stationary_series())

    assert 0.0 <= report.p_value <= 1.0


def test_kpss_pvalue_range():
    report = kpss_test(create_stationary_series())

    assert 0.0 <= report.p_value <= 1.0