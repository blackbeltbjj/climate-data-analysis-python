import numpy as np
import pytest
import xarray as xr

from climate.ocean import load_sst_netcdf


def create_file(tmp_path):

    data = xr.Dataset(
        {
            "sst": (
                [
                    "time",
                    "lat",
                    "lon",
                ],
                np.ones(
                    (2, 2, 2)
                ),
            )
        }
    )

    path = tmp_path / "sst.nc"

    data.to_netcdf(
        path
    )

    return path


def test_load_sst(tmp_path):

    result = load_sst_netcdf(
        create_file(tmp_path)
    )

    assert isinstance(
        result,
        xr.DataArray,
    )


def test_missing_file():

    with pytest.raises(FileNotFoundError):
        load_sst_netcdf(
            "missing.nc"
        )


def test_missing_variable(tmp_path):

    path = tmp_path / "bad.nc"

    xr.Dataset(
        {
            "temperature": (
                ["x"],
                [1],
            )
        }
    ).to_netcdf(
        path
    )

    with pytest.raises(ValueError):
        load_sst_netcdf(
            path
        )