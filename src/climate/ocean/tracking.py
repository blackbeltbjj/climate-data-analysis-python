"""
Warm Pool tracking utilities.
"""

from __future__ import annotations

import pandas as pd
import xarray as xr

from climate.config import WARM_POOL_THRESHOLD

from climate.ocean.spherical import (
    spherical_centroid,
)

from climate.ocean.warm_pool import (
    warm_pool_area_fraction,
)



def track_warm_pool(
    sst: xr.DataArray,
    *,
    threshold: float | None = None,
) -> pd.DataFrame:
    """
    Track Warm Pool centroid through time.
    """

    if threshold is None:
        threshold = WARM_POOL_THRESHOLD


    records = []


    for time in sst.time:

        field = sst.sel(
            time=time
        )


        centroid = spherical_centroid(
            field,
            threshold=threshold,
        )


        centroid["area_fraction"] = (
            warm_pool_area_fraction(
                field,
                threshold=threshold,
            )
        )


        centroid["time"] = pd.Timestamp(
            time.values
        )


        records.append(
            centroid
        )


    return pd.DataFrame(
        records
    )