"""
SST input/output utilities.
"""

from __future__ import annotations

from pathlib import Path

import xarray as xr


def load_sst_netcdf(
    path: str | Path,
    *,
    variable: str = "sst",
) -> xr.DataArray:
    """
    Load SST data from a NetCDF file.

    Parameters
    ----------
    path:
        NetCDF file path.

    variable:
        SST variable name.

    Returns
    -------
    xarray.DataArray
        SST field.
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    dataset = xr.open_dataset(
        file_path
    )

    if variable not in dataset:
        raise ValueError(
            f"Variable not found: {variable}"
        )

    return dataset[variable]