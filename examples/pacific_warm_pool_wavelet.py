"""
Pacific Warm Pool Wavelet Analysis Example.

Demonstrates:

- SST field generation
- Warm Pool tracking
- Seasonal anomaly removal
- Torrence & Compo (1998)
  wavelet analysis

This example uses synthetic SST data.
Replace with OISST NetCDF input for research use.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import xarray as xr

from climate.ocean import (
    track_warm_pool,
)

from climate.ocean import (
    warm_pool_longitude_anomaly,
)

from climate.signal import (
    morlet_cwt,
    wavelet_power,
    global_wavelet_spectrum,
    band_average_power,
)


def create_synthetic_sst():

    time = pd.date_range(
        "1982-01-01",
        periods=240,
        freq="W",
    )

    lat = np.linspace(
        -10,
        10,
        20,
    )

    lon = np.linspace(
        120,
        200,
        40,
    )

    shape = (
        len(time),
        len(lat),
        len(lon),
    )

    sst = (
        28
        +
        np.random.normal(
            0,
            0.2,
            shape,
        )
    )

    # Add warm pool region
    for i in range(len(time)):

        seasonal = (
            np.sin(
                2
                *
                np.pi
                *
                i
                /
                52
            )
        )

        sst[i, :, 15:30] += (
            1.5
            +
            0.3
            *
            seasonal
        )

    return xr.DataArray(
        sst,
        dims=[
            "time",
            "lat",
            "lon",
        ],
        coords={
            "time": time,
            "lat": lat,
            "lon": lon,
        },
        name="sst",
    )


def main():

    sst = create_synthetic_sst()

    tracking = track_warm_pool(
        sst
    )

    longitude_anomaly = (
        warm_pool_longitude_anomaly(
            tracking
        )
    )

    wavelet, scales, periods, report = (
        morlet_cwt(
            longitude_anomaly,
            dt=7,
        )
    )

    power = wavelet_power(
        wavelet
    )

    spectrum = global_wavelet_spectrum(
        power
    )

    annual_power = band_average_power(
        power,
        periods,
        period_min=48,
        period_max=54,
    )

    print(report)

    print(
        "Annual band power length:",
        len(annual_power),
    )

    print(
        "Dominant period:",
        periods[
            np.argmax(
                spectrum
            )
        ],
        "weeks",
    )


if __name__ == "__main__":

    main()