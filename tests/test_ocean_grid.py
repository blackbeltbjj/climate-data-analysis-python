import numpy as np
import pandas as pd
import pytest
import xarray as xr

from climate.ocean import (
    SSTGridReport,
    spatial_mean,
    sst_grid_report,
)


def create_grid():

    return xr.DataArray(
        np.ones(
            (2, 3, 4)
        ),
        dims=[
            "time",
            "lat",
            "lon",
        ],
        coords={
            "time": pd.date_range(
                "2000-01-01",
                periods=2,
                freq="MS",
            ),
            "lat": [
                -1,
                1,
                3,
            ],
            "lon": [
                100,
                110,
                120,
                130,
            ],
        },
    )


def test_grid_report():

    report = sst_grid_report(
        create_grid()
    )

    assert isinstance(
        report,
        SSTGridReport,
    )

    assert report.latitude_points == 3
    assert report.longitude_points == 4
    assert report.time_points == 2


def test_spatial_mean():

    result = spatial_mean(
        create_grid()
    )

    assert result.dims == (
        "time",
    )


def test_invalid_input():

    with pytest.raises(TypeError):
        sst_grid_report(
            [1, 2, 3]
        )