"""
Statistical analysis tools for climate datasets.
"""

from climate.statistics.autocorrelation import (
    AutocorrelationReport,
    autocorrelation_report,
)
from climate.statistics.cross_correlation import (
    CrossCorrelationReport,
    cross_correlation_report,
)
from climate.statistics.decomposition import STLReport, stl_decompose
from climate.statistics.descriptive import StatisticsReport, describe
from climate.statistics.seasonality import (
    SeasonalityReport,
    monthly_anomalies,
    monthly_climatology,
    seasonality_report,
)
from climate.statistics.spectral import SpectralReport, spectral_report
from climate.statistics.stationarity import (
    StationarityReport,
    adf_test,
    kpss_test,
)
from climate.statistics.trend import TrendReport, linear_trend

__all__ = [
    "AutocorrelationReport",
    "CrossCorrelationReport",
    "STLReport",
    "SeasonalityReport",
    "SpectralReport",
    "StationarityReport",
    "StatisticsReport",
    "TrendReport",
    "adf_test",
    "autocorrelation_report",
    "cross_correlation_report",
    "describe",
    "kpss_test",
    "linear_trend",
    "monthly_anomalies",
    "monthly_climatology",
    "seasonality_report",
    "spectral_report",
    "stl_decompose",
]
