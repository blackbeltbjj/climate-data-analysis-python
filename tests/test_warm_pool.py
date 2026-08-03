import numpy as np
import pytest
import xarray as xr

from climate.ocean import (
    warm_pool_area,
    warm_pool_mask,
)


def create_sst():

    return xr.DataArray(
        np.array(
            [
                [
                    [28.0, 29.0],
                    [30.0, 27.0],
                ]
            ]
        ),
        dims=[
            "time",
            "lat",
            "lon",
        ],
    )


def test_mask():

    result = warm_pool_mask(
        create_sst()
    )

    assert result.sum() == 2


def test_area():

    result = warm_pool_area(
        create_sst()
    )

    assert result.shape == (1,)


def test_invalid_input():

    with pytest.raises(TypeError):
        warm_pool_mask(
            [1, 2, 3]
        )