"""
Standard ENSO Niño region definitions.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NiñoRegion:
    """
    Geographic definition of an ENSO monitoring region.
    """

    name: str
    longitude_min: float
    longitude_max: float
    latitude_min: float
    latitude_max: float


NINO_REGIONS = {
    "Nino1+2": NiñoRegion(
        name="Niño 1+2",
        longitude_min=-90,
        longitude_max=-80,
        latitude_min=-10,
        latitude_max=0,
    ),
    "Nino3": NiñoRegion(
        name="Niño 3",
        longitude_min=-150,
        longitude_max=-90,
        latitude_min=-5,
        latitude_max=5,
    ),
    "Nino3.4": NiñoRegion(
        name="Niño 3.4",
        longitude_min=-170,
        longitude_max=-120,
        latitude_min=-5,
        latitude_max=5,
    ),
    "Nino4": NiñoRegion(
        name="Niño 4",
        longitude_min=160,
        longitude_max=-150,
        latitude_min=-5,
        latitude_max=5,
    ),
}


def get_nino_region(name: str) -> NiñoRegion:
    """
    Return a standard Niño region definition.
    """

    if name not in NINO_REGIONS:
        raise ValueError(
            f"Unknown ENSO region: {name}"
        )

    return NINO_REGIONS[name]