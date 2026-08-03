"""
Warm Pool centroid utilities.

Calculates geographic centroid of SST-defined regions.
"""

from __future__ import annotations

import numpy as np
import xarray as xr


def warm_pool_centroid(
    sst: xr.DataArray,
    *,
    threshold: float = 29.0,
) -> dict[str, float]:
    """
    Calculate the geographic centroid of the warm pool.

    The warm pool is defined as SST >= threshold.

    Returns
    -------
    dict
        Longitude and latitude of the centroid.
    """

    if not isinstance(
        sst,
        xr.DataArray,
    ):
        raise TypeError(
            "Input must be an xarray DataArray."
        )

    if not {
        "lat",
        "lon",
    }.issubset(
        sst.dims
    ):
        raise ValueError(
            "Input must contain lat and lon dimensions."
        )

    mask = sst >= threshold

    weights = mask.astype(float)

    total = weights.sum()

    if total == 0:
        raise ValueError(
            "No warm pool grid cells found."
        )

    lon_grid, lat_grid = xr.broadcast(
        sst.lon,
        sst.lat,
    )

    longitude = (
        (lon_grid * weights)
        .sum()
        / total
    )

    latitude = (
        (lat_grid * weights)
        .sum()
        / total
    )

    return {
        "longitude": float(longitude),
        "latitude": float(latitude),
    }