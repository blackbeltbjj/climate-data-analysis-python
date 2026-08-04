"""
Global configuration parameters.

Scientific parameters should be defined here
rather than hard-coded inside analysis functions.
"""


# --------------------------------------------------
# Warm Pool definition
# --------------------------------------------------

# Sea surface temperature threshold (degC)
#
# Examples:
#
# 28.0  -> broad tropical warm water region
# 28.5  -> intermediate definition
# 29.0  -> traditional Pacific Warm Pool definition
#

WARM_POOL_THRESHOLD = 29.0


# --------------------------------------------------
# Units
# --------------------------------------------------

SST_UNITS = "degC"


# --------------------------------------------------
# Wavelet parameters
# --------------------------------------------------

WAVELET_MORLET_OMEGA0 = 6.0


# Annual band
# daily data

ANNUAL_PERIOD_MIN = 330
ANNUAL_PERIOD_MAX = 400