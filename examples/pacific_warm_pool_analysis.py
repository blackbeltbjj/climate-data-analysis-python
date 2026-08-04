"""
Pacific Warm Pool Research Workflow.

Based on:

Torrence & Compo (1998)
Wavelet Analysis.

Workflow:

OISST SST
    ↓
Warm Pool (SST >= 29°C)
    ↓
Spherical centroid
    ↓
Longitude anomaly
    ↓
Morlet CWT
    ↓
Wavelet power
    ↓
Global spectrum
    ↓
Annual band power
    ↓
Figures
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from climate.visualization import (
    plot_band_power,
)

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

from climate.visualization import (
    wavelet_scalogram,
    plot_global_wavelet_spectrum,
)


#DATA_FILE = Path(
#    "data/raw/oisst_daily.nc"
#)

DATA_FILE = Path(
    "data/raw/oisst_daily_test.nc"
)  

OUTPUT = Path(
    "outputs/figures"
)


def main():

    OUTPUT.mkdir(
        parents=True,
        exist_ok=True,
    )

    sst = load_oisst(
        DATA_FILE
    )

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


    fig, ax = plt.subplots()

    wavelet_scalogram(
        power,
        periods,
        ax=ax,
    )

    fig.savefig(
        OUTPUT
        /
        "warm_pool_wavelet_scalogram.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(
        fig
    )


    fig, ax = plt.subplots()

    plot_global_wavelet_spectrum(
        spectrum,
        periods,
        ax=ax,
    )

    fig.savefig(
        OUTPUT
        /
        "warm_pool_global_spectrum.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(
        fig
    )

    fig, ax = plt.subplots()

    plot_band_power(
        annual_power,
        ax=ax,
        label="Annual band power",
    )

    fig.savefig(
        OUTPUT
        /
        "warm_pool_annual_band_power.png",
    dpi=300,
    bbox_inches="tight",
    )

    plt.close(
        fig
    )


    print(report)

    print(
        "Tracking records:",
        len(tracking),
    )

    print(
        "Annual band length:",
        len(annual_power),
    )


if __name__ == "__main__":

    main()