"""
Gridded sea surface temperature utilities.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import xarray as xr


@dataclass(frozen=True)
class SSTGridReport:
    """
    Metadata for a gridded SST dataset.
    """

    latitude_points: int
    longitude_points: int
    time_points: int


def sst_grid_report(
    dataset: xr.DataArray,
) -> SSTGridReport:
    """
    Generate metadata for a gridded SST field.
    """

    if not isinstance(
        dataset,
        xr.DataArray,
    ):
        raise TypeError(
            "Input must be an xarray DataArray."
        )

    required = {
        "lat",
        "lon",
        "time",
    }

    if not required.issubset(
        dataset.dims
    ):
        raise ValueError(
            "Dataset must contain lat, lon, and time dimensions."
        )

    return SSTGridReport(
        latitude_points=dataset.sizes["lat"],
        longitude_points=dataset.sizes["lon"],
        time_points=dataset.sizes["time"],
    )


def spatial_mean(
    dataset: xr.DataArray,
) -> xr.DataArray:
    """
    Calculate spatial mean SST.

    Averages latitude and longitude dimensions.
    """

    if not isinstance(
        dataset,
        xr.DataArray,
    ):
        raise TypeError(
            "Input must be an xarray DataArray."
        )

    return dataset.mean(
        dim=[
            "lat",
            "lon",
        ]
    )