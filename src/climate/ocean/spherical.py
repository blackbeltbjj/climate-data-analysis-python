"""
Spherical centroid utilities for SST-defined regions.
"""

from __future__ import annotations

import numpy as np
import xarray as xr


def spherical_warm_pool_centroid(
    sst: xr.DataArray,
    *,
    threshold: float = 29.0,
) -> dict[str, float]:
    """
    Calculate the spherical centroid of a warm pool.

    Uses spherical coordinates and cosine(latitude)
    area weighting.

    Parameters
    ----------
    sst:
        SST DataArray with lat and lon dimensions.

    threshold:
        SST threshold defining the warm pool.

    Returns
    -------
    dict
        Centroid longitude and latitude.
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

    lat_rad = np.deg2rad(
        sst.lat
    )

    lon_rad = np.deg2rad(
        sst.lon
    )

    lon_grid, lat_grid = xr.broadcast(
        lon_rad,
        lat_rad,
    )

    weights = (
        mask.astype(float)
        * np.cos(lat_grid)
    )

    total = weights.sum()

    if total == 0:
        raise ValueError(
            "No warm pool grid cells found."
        )

    x = (
        np.cos(lat_grid)
        * np.cos(lon_grid)
        * weights
    ).sum() / total

    y = (
        np.cos(lat_grid)
        * np.sin(lon_grid)
        * weights
    ).sum() / total

    z = (
        np.sin(lat_grid)
        * weights
    ).sum() / total

    longitude = np.rad2deg(
        np.arctan2(y, x)
    )

    latitude = np.rad2deg(
        np.arctan2(
            z,
            np.sqrt(
                x**2 + y**2
            ),
        )
    )

    return {
        "longitude": float(longitude),
        "latitude": float(latitude),
    }