"""
Tests for OISST loader.
"""

import numpy as np
import xarray as xr

from climate.ocean import load_oisst


def test_load_oisst(tmp_path):

    filename = (
        tmp_path
        /
        "test.nc"
    )

    data = xr.Dataset(
        {
            "analysed_sst": (
                [
                    "time",
                    "lat",
                    "lon",
                ],
                np.ones(
                    (
                        2,
                        3,
                        4,
                    )
                )
                *
                300,
            )
        },
        coords={
            "time": [
                "2000-01-01",
                "2000-01-02",
            ],
            "lat": [
                -1,
                0,
                1,
            ],
            "lon": [
                150,
                160,
                170,
                180,
            ],
        },
    )

    data["analysed_sst"].attrs["units"] = "K"

    data.to_netcdf(
        filename
    )

    sst = load_oisst(
        filename
    )

    assert sst.shape == (
        2,
        3,
        4,
    )

    assert sst.attrs["units"] == "degC"