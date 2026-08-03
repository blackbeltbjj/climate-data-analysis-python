"""
Statistical analysis tools for climate datasets.
"""

from climate.statistics.descriptive import StatisticsReport, describe
from climate.statistics.trend import TrendReport, linear_trend

__all__ = [
    "StatisticsReport",
    "TrendReport",
    "describe",
    "linear_trend",
]