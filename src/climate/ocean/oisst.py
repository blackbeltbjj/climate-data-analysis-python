"""
NOAA OISST data utilities.

Handles daily sea surface temperature
NetCDF datasets.
"""

from __future__ import annotations

from pathlib import Path

import xarray as xr


def _find_sst_variable(
    dataset: xr.Dataset,
) -> str:
    """
    Identify SST variable in dataset.
    """

    candidates = [
        "sst",
        "sst_data",
        "analysed_sst",
        "sea_surface_temperature",
    ]

    for name in candidates:

        if name in dataset:
            return name

    raise ValueError(
        "Could not identify SST variable."
    )


def _standardize_dimensions(
    sst: xr.DataArray,
) -> xr.DataArray:
    """
    Standardize coordinate names.
    """

    rename = {}

    for dim in sst.dims:

        lower = dim.lower()

        if lower in [
            "latitude",
            "y",
        ]:
            rename[dim] = "lat"

        elif lower in [
            "longitude",
            "x",
        ]:
            rename[dim] = "lon"

        elif lower in [
            "date",
        ]:
            rename[dim] = "time"

    if rename:
        sst = sst.rename(
            rename
        )

    return sst


def _convert_units(
    sst: xr.DataArray,
) -> xr.DataArray:
    """
    Convert Kelvin SST to Celsius.

    Leaves Celsius unchanged.
    """

    units = (
        sst.attrs
        .get(
            "units",
            "",
        )
        .lower()
    )

    if units in [
        "k",
        "kelvin",
    ]:
        sst = sst - 273.15

        sst.attrs["units"] = (
            "degC"
        )

    return sst


def load_oisst(
    filename: str | Path,
) -> xr.DataArray:
    """
    Load NOAA OISST NetCDF SST data.

    Returns
    -------
    xarray.DataArray

    Dimensions:
        time, lat, lon

    Units:
        degrees Celsius
    """

    filename = Path(
        filename
    )

    if not filename.exists():
        raise FileNotFoundError(
            filename
        )

    dataset = xr.open_dataset(
        filename
    )

    variable = _find_sst_variable(
        dataset
    )

    sst = dataset[variable]

    sst = _standardize_dimensions(
        sst
    )

    required = {
        "time",
        "lat",
        "lon",
    }

    if not required.issubset(
        sst.dims
    ):
        raise ValueError(
            "OISST must contain time, lat and lon dimensions."
        )

    sst = _convert_units(
        sst
    )

    sst = sst.where(
        sst > -100
    )

    return sst