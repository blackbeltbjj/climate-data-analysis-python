import pytest
import xarray as xr

from climate.io import open_netcdf, save_netcdf


def create_dataset():
    return xr.Dataset(
        data_vars={
            "temperature": (
                ("time",),
                [20.1, 20.3, 20.2],
            )
        },
        coords={
            "time": [0, 1, 2],
        },
    )


def test_save_and_open_netcdf(tmp_path):
    dataset = create_dataset()

    filename = tmp_path / "test.nc"

    save_netcdf(dataset, filename)

    loaded = open_netcdf(filename)

    assert isinstance(loaded, xr.Dataset)
    assert "temperature" in loaded.data_vars


def test_open_missing_file():
    with pytest.raises(FileNotFoundError):
        open_netcdf("does_not_exist.nc")


def test_invalid_extension(tmp_path):
    filename = tmp_path / "invalid.txt"

    filename.write_text("test")

    with pytest.raises(ValueError):
        open_netcdf(filename)


def test_save_requires_dataset(tmp_path):
    with pytest.raises(TypeError):
        save_netcdf([], tmp_path / "test.nc")
