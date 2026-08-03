import numpy as np
import pandas as pd
import xarray as xr

from climate.ocean import (
    track_warm_pool,
)


def create_sst():

    return xr.DataArray(
        np.array(
            [
                [
                    [30, 30],
                    [30, 28],
                ],
                [
                    [30, 30],
                    [29, 28],
                ],
            ]
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
                -5,
                5,
            ],
            "lon": [
                150,
                170,
            ],
        },
    )


def test_tracking():

    result = track_warm_pool(
        create_sst()
    )

    assert len(result) == 2

    assert (
        "longitude"
        in result.columns
    )

    assert (
        "area_fraction"
        in result.columns
    )