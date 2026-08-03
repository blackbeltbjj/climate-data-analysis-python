"""
Statistical analysis tools for climate datasets.
"""

from climate.statistics.decomposition import STLReport, stl_decompose
from climate.statistics.descriptive import StatisticsReport, describe
from climate.statistics.seasonality import (
    SeasonalityReport,
    monthly_anomalies,
    monthly_climatology,
    seasonality_report,
)
from climate.statistics.stationarity import (
    StationarityReport,
    adf_test,
    kpss_test,
)
from climate.statistics.trend import TrendReport, linear_trend

__all__ = [
    "StatisticsReport",
    "TrendReport",
    "SeasonalityReport",
    "STLReport",
    "StationarityReport",
    "describe",
    "linear_trend",
    "monthly_climatology",
    "monthly_anomalies",
    "seasonality_report",
    "stl_decompose",
    "adf_test",
    "kpss_test",
]