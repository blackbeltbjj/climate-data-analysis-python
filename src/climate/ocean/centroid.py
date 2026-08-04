"""
Warm Pool centroid calculations.

The Warm Pool threshold is configurable through:

    climate.config.WARM_POOL_THRESHOLD
"""

from __future__ import annotations

import numpy as np
import xarray as xr

from climate.config import WARM_POOL_THRESHOLD



def warm_pool_centroid(
    sst: xr.DataArray,
    *,
    threshold: float | None = None,
) -> dict[str, float]:
    """
    Calculate spherical centroid of Warm Pool.

    Parameters
    ----------
    sst:
        SST DataArray with lat/lon dimensions.

    threshold:
        SST threshold.

        If None:
            uses WARM_POOL_THRESHOLD.

    Returns
    -------
    dict
        latitude
        longitude
        threshold
    """

    if threshold is None:
        threshold = WARM_POOL_THRESHOLD


    if not isinstance(
        sst,
        xr.DataArray,
    ):
        raise TypeError(
            "sst must be an xarray.DataArray"
        )


    mask = (
        sst >= threshold
    )


    if mask.sum() == 0:
        raise ValueError(
            "No Warm Pool grid cells found."
        )


    lat = sst["lat"].values
    lon = sst["lon"].values


    lon_grid, lat_grid = np.meshgrid(
        lon,
        lat,
    )


    weights = mask.values.astype(
        float
    )


    lat_rad = np.deg2rad(
        lat_grid
    )

    lon_rad = np.deg2rad(
        lon_grid
    )


    x = (
        np.cos(lat_rad)
        *
        np.cos(lon_rad)
    )

    y = (
        np.cos(lat_rad)
        *
        np.sin(lon_rad)
    )

    z = np.sin(
        lat_rad
    )


    total = np.sum(
        weights
    )


    x_mean = np.sum(
        x * weights
    ) / total

    y_mean = np.sum(
        y * weights
    ) / total

    z_mean = np.sum(
        z * weights
    ) / total


    longitude = np.rad2deg(
        np.arctan2(
            y_mean,
            x_mean,
        )
    )


    latitude = np.rad2deg(
        np.arctan2(
            z_mean,
            np.sqrt(
                x_mean**2
                +
                y_mean**2
            ),
        )
    )


    return {
        "latitude": round(
            float(latitude)
        ),
        "longitude": round(
            float(longitude)
        ),
        "threshold": float(
            threshold
        ),
    }