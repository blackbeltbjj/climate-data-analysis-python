"""
Pacific Warm Pool utilities.

Defines warm pool detection based on sea surface
temperature thresholds.
"""

from __future__ import annotations

import xarray as xr


DEFAULT_THRESHOLD = 29.0


def warm_pool_mask(
    sst: xr.DataArray,
    *,
    threshold: float = DEFAULT_THRESHOLD,
) -> xr.DataArray:
    """
    Create a warm pool mask.

    Grid cells with SST >= threshold are True.
    """

    if not isinstance(
        sst,
        xr.DataArray,
    ):
        raise TypeError(
            "Input must be an xarray DataArray."
        )

    return sst >= threshold


def warm_pool_area(
    sst: xr.DataArray,
    *,
    threshold: float = DEFAULT_THRESHOLD,
) -> xr.DataArray:
    """
    Calculate warm pool area fraction.

    Returns the fraction of grid cells exceeding
    the SST threshold.
    """

    mask = warm_pool_mask(
        sst,
        threshold=threshold,
    )

    return mask.mean(
        dim=[
            "lat",
            "lon",
        ]
    )