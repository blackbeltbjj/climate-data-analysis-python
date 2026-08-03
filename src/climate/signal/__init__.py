"""
Signal processing utilities.
"""

from climate.signal.spectrum import (
    global_wavelet_spectrum,
)

from climate.signal.significance import (
    lag1_autocorrelation,
    red_noise_spectrum,
    wavelet_significance_level,
)

from climate.signal.wavelet import (
    WaveletReport,
    morlet_cwt,
)

from climate.signal.wavelet import (
    WaveletReport,
    morlet_cwt,
    cone_of_influence,
)

from climate.signal.spectrum import (
    wavelet_power,
    global_wavelet_spectrum,
)

from climate.signal.spectrum import (
    wavelet_power,
    global_wavelet_spectrum,
    band_average_power,
)

__all__ = [
    "WaveletReport",
    "morlet_cwt",
    "global_wavelet_spectrum",
    "lag1_autocorrelation",
    "red_noise_spectrum",
    "wavelet_significance_level",
    "cone_of_influence",
    "wavelet_power",
    "band_average_power",
]