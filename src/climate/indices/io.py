"""
ENSO index input/output utilities.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_enso_csv(
    path: str | Path,
    *,
    date_column: str = "date",
    value_column: str | None = None,
) -> pd.Series | pd.DataFrame:
    """
    Load an ENSO index CSV file.

    Parameters
    ----------
    path:
        CSV file path.

    date_column:
        Name of the date column.

    value_column:
        Optional column name to return as a Series.

    Returns
    -------
    pandas Series or DataFrame
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    data = pd.read_csv(file_path)

    if date_column not in data.columns:
        raise ValueError(
            f"Missing date column: {date_column}"
        )

    data[date_column] = pd.to_datetime(
        data[date_column]
    )

    data = data.set_index(
        date_column
    )

    if value_column is not None:

        if value_column not in data.columns:
            raise ValueError(
                f"Missing column: {value_column}"
            )

        return data[value_column]

    return data