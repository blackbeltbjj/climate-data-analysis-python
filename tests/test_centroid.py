import numpy as np
import xarray as xr
import pytest

from climate.ocean import warm_pool_centroid


def create_sst():

    return xr.DataArray(
        np.array(
            [
                [30.0, 30.0],
                [28.0, 28.0],
            ]
        ),
        dims=[
            "lat",
            "lon",
        ],
        coords={
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


def test_centroid():

    result = warm_pool_centroid(
        create_sst()
    )

    assert result["longitude"] == 160
    assert result["latitude"] == -5


def test_no_warm_pool():

    sst = xr.DataArray(
        np.ones(
            (2, 2)
        ) * 20,
        dims=[
            "lat",
            "lon",
        ],
        coords={
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

    with pytest.raises(ValueError):
        warm_pool_centroid(
            sst
        )