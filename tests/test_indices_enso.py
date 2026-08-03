import pandas as pd
import pytest

from climate.indices import (
    ENSOIndexReport,
    enso_report,
)


def create_series():
    return pd.Series(
        [0.1, 0.2, 0.3],
        index=pd.date_range(
            "2000-01-01",
            periods=3,
            freq="MS",
        ),
    )


def test_returns_report():
    report = enso_report(create_series())

    assert isinstance(
        report,
        ENSOIndexReport,
    )


def test_metadata():
    report = enso_report(
        create_series(),
        name="Nino3.4",
    )

    assert report.name == "Nino3.4"
    assert report.observations == 3


def test_invalid_input():
    with pytest.raises(TypeError):
        enso_report([1, 2, 3])


def test_empty_series():
    with pytest.raises(ValueError):
        enso_report(pd.Series(dtype=float))