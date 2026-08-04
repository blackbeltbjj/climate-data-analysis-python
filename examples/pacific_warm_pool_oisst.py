"""
Pacific Warm Pool OISST Wavelet Analysis.

Research workflow:

OISST NetCDF
      ↓
SST field
      ↓
Warm Pool (SST >= 29°C)
      ↓
Spherical centroid
      ↓
Longitude anomaly
      ↓
Torrence & Compo (1998)
      ↓
Annual cycle variability
"""

from __future__ import annotations

from pathlib import Path

from climate.ocean import (
    load_oisst,
    track_warm_pool,
    warm_pool_longitude_anomaly,
)

from climate.signal import (
    morlet_cwt,
    wavelet_power,
    global_wavelet_spectrum,
    band_average_power,
)


DATA_FILE = Path(
    "data/raw/oisst_daily.nc"
)


def analyze_warm_pool(
    sst,
):

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
            dt=1,
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
        period_min=330,
        period_max=400,
    )

    return {
        "tracking": tracking,
        "longitude_anomaly": longitude_anomaly,
        "power": power,
        "periods": periods,
        "spectrum": spectrum,
        "annual_power": annual_power,
        "report": report,
    }


def main():

    if not DATA_FILE.exists():

        raise FileNotFoundError(
            f"Missing SST file: {DATA_FILE}"
        )

    sst = load_oisst(
        DATA_FILE
    )

    result = analyze_warm_pool(
        sst
    )

    print(
        result["report"]
    )

    print(
        result["tracking"].head()
    )


if __name__ == "__main__":

    main()