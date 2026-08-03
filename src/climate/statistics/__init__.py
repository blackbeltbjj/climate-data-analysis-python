"""
Statistical analysis tools for climate datasets.
"""

from climate.statistics.descriptive import StatisticsReport, describe
from climate.statistics.trend import TrendReport, linear_trend
from climate.statistics.seasonality import (
    SeasonalityReport,
    monthly_anomalies,
    monthly_climatology,
    seasonality_report,
)

__all__ = [
    "StatisticsReport",
    "TrendReport",
    "SeasonalityReport",
    "describe",
    "linear_trend",
    "monthly_climatology",
    "monthly_anomalies",
    "seasonality_report",
]