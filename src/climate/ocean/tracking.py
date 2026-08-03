"""
Warm Pool time-series tracking utilities.
"""

from __future__ import annotations

import pandas as pd
import xarray as xr

from climate.ocean.spherical import (
    spherical_warm_pool_centroid,
)

from climate.ocean.warm_pool import (
    warm_pool_area,
)


def track_warm_pool(
    sst: xr.DataArray,
    *,
    threshold: float = 29.0,
) -> pd.DataFrame:
    """
    Track Warm Pool centroid and area through time.

    Parameters
    ----------
    sst:
        SST DataArray with dimensions:
        time, lat, lon.

    threshold:
        SST threshold defining the Warm Pool.

    Returns
    -------
    pandas.DataFrame

    Columns:
        longitude
        latitude
        area_fraction
    """

    if not isinstance(
        sst,
        xr.DataArray,
    ):
        raise TypeError(
            "Input must be an xarray DataArray."
        )

    if not {
        "time",
        "lat",
        "lon",
    }.issubset(
        sst.dims
    ):
        raise ValueError(
            "Input must contain time, lat, and lon dimensions."
        )

    records = []

    for time in sst.time:

        field = sst.sel(
            time=time
        )

        centroid = spherical_warm_pool_centroid(
            field,
            threshold=threshold,
        )

        area = warm_pool_area(
            field,
            threshold=threshold,
        )

        records.append(
            {
                "time": pd.Timestamp(
                    time.values
                ),
                "longitude": centroid["longitude"],
                "latitude": centroid["latitude"],
                "area_fraction": float(area),
            }
        )

    return pd.DataFrame(
        records
    ).set_index(
        "time"
    )