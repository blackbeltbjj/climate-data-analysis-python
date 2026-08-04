"""
Create synthetic OISST-like NetCDF file
with a migrating Warm Pool.

Used for pipeline validation.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr


OUTPUT = Path(
    "data/raw/oisst_daily_test.nc"
)


def main():

    time = pd.date_range(
        "2000-01-01",
        periods=730,
        freq="D",
    )

    lat = np.linspace(
        -20,
        20,
        41,
    )

    lon = np.linspace(
        120,
        220,
        101,
    )

    sst = np.zeros(
        (
            len(time),
            len(lat),
            len(lon),
        )
    )

    lon2d, lat2d = np.meshgrid(
        lon,
        lat,
    )

    for t in range(len(time)):

        seasonal = (
            0.3
            *
            np.sin(
                2
                *
                np.pi
                *
                t
                /
                365
            )
        )

        field = (
            27.5
            +
            seasonal
        ) * np.ones_like(
            lon2d
        )

        # migrating warm pool centre
        centre = (
            170
            +
            10
            *
            np.sin(
                2
                *
                np.pi
                *
                t
                /
                365
            )
        )

        warm_pool = np.exp(
            -(
                (
                    lon2d
                    -
                    centre
                )
                ** 2
                /
                2
                /
                8**2
            )
        )

        field += (
            3
            *
            warm_pool
        )

        sst[t] = field


    ds = xr.Dataset(
        {
            "sst": (
                [
                    "time",
                    "lat",
                    "lon",
                ],
                sst,
            )
        },
        coords={
            "time": time,
            "lat": lat,
            "lon": lon,
        },
    )

    ds["sst"].attrs["units"] = (
        "degC"
    )

    ds.to_netcdf(
        OUTPUT
    )

    print(
        f"Created {OUTPUT}"
    )


if __name__ == "__main__":

    main()