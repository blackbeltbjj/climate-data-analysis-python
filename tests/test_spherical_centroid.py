import numpy as np
import xarray as xr
import pytest

from climate.ocean import (
    spherical_warm_pool_centroid,
)


def create_sst():

    return xr.DataArray(
        np.array(
            [
                [30.0, 30.0],
                [30.0, 30.0],
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


def test_spherical_centroid():

    result = spherical_warm_pool_centroid(
        create_sst()
    )

    assert abs(
        result["longitude"] - 160
    ) < 1e-10

    assert abs(
        result["latitude"]
    ) < 1e-10


def test_invalid_input():

    with pytest.raises(TypeError):
        spherical_warm_pool_centroid(
            [1, 2, 3]
        )