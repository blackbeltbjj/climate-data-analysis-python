import pandas as pd
import pytest

from climate.ocean import (
    SSTReport,
    sst_report,
)


def create_series():
    return pd.Series(
        [25.1, 25.3, 25.5],
        index=pd.date_range(
            "2000-01-01",
            periods=3,
            freq="MS",
        ),
    )


def test_returns_report():

    report = sst_report(
        create_series()
    )

    assert isinstance(
        report,
        SSTReport,
    )


def test_metadata():

    report = sst_report(
        create_series(),
        name="Niño 3.4 SST",
    )

    assert report.name == "Niño 3.4 SST"
    assert report.observations == 3


def test_invalid_input():

    with pytest.raises(TypeError):
        sst_report([25, 26, 27])


def test_invalid_index():

    with pytest.raises(TypeError):
        sst_report(
            pd.Series([25, 26, 27])
        )