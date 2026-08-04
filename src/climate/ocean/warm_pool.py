"""
Warm Pool detection utilities.

The Warm Pool threshold is controlled through:

    climate.config.WARM_POOL_THRESHOLD
"""

from __future__ import annotations

import xarray as xr

from climate.config import WARM_POOL_THRESHOLD


# Backward compatibility
DEFAULT_THRESHOLD = WARM_POOL_THRESHOLD



def warm_pool_mask(
    sst: xr.DataArray,
    *,
    threshold: float | None = None,
) -> xr.DataArray:
    """
    Create Warm Pool boolean mask.
    """

    if threshold is None:
        threshold = WARM_POOL_THRESHOLD

    return sst >= threshold



def warm_pool_area(
    sst: xr.DataArray,
    *,
    threshold: float | None = None,
) -> xr.DataArray:
    """
    Calculate Warm Pool area.

    Original API behaviour:
    returns area through spatial reduction.

    Output dimensions:
        time
    """

    if threshold is None:
        threshold = WARM_POOL_THRESHOLD


    mask = warm_pool_mask(
        sst,
        threshold=threshold,
    )


    return mask.sum(
        dim=[
            "lat",
            "lon",
        ]
    )



def warm_pool_area_fraction(
    sst: xr.DataArray,
    *,
    threshold: float | None = None,
) -> float:
    """
    Calculate Warm Pool fraction.
    """

    mask = warm_pool_mask(
        sst,
        threshold=threshold,
    )


    return float(
        mask.sum()
        /
        mask.size
    )



def warm_pool_extent(
    sst: xr.DataArray,
    *,
    threshold: float | None = None,
) -> xr.DataArray:
    """
    Return masked SST Warm Pool field.
    """

    mask = warm_pool_mask(
        sst,
        threshold=threshold,
    )

    return sst.where(
        mask
    )