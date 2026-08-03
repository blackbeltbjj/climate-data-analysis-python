"""
NetCDF input/output utilities.
"""

from __future__ import annotations

from pathlib import Path

import xarray as xr


def open_netcdf(
    file_path: str | Path,
) -> xr.Dataset:
    """
    Open a NetCDF file as an xarray Dataset.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() not in {".nc", ".nc4", ".cdf"}:
        raise ValueError(
            "Expected a NetCDF file with extension .nc, .nc4, or .cdf."
        )

    return xr.open_dataset(path)


def save_netcdf(
    dataset: xr.Dataset,
    file_path: str | Path,
) -> Path:
    """
    Save an xarray Dataset as a NetCDF file.
    """
    if not isinstance(dataset, xr.Dataset):
        raise TypeError("Input must be an xarray Dataset.")

    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    dataset.to_netcdf(path)

    return path