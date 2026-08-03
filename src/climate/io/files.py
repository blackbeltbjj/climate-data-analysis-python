"""
CSV input/output utilities.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(
    file_path: str | Path,
    *,
    parse_dates: list[str] | None = None,
    index_col: str | int | None = None,
) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".csv":
        raise ValueError("Expected a CSV file.")

    return pd.read_csv(
        path,
        parse_dates=parse_dates,
        index_col=index_col,
    )


def save_csv(
    dataframe: pd.DataFrame,
    file_path: str | Path,
    *,
    index: bool = True,
) -> Path:
    """
    Save a pandas DataFrame as a CSV file.
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    dataframe.to_csv(path, index=index)

    return path