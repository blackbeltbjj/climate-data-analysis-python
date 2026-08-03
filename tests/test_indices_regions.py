from climate.indices import (
    NiñoRegion,
    get_nino_region,
)


def test_region_lookup():
    region = get_nino_region(
        "Nino3.4"
    )

    assert isinstance(
        region,
        NiñoRegion,
    )


def test_region_name():
    region = get_nino_region(
        "Nino3.4"
    )

    assert region.name == "Niño 3.4"


def test_invalid_region():
    import pytest

    with pytest.raises(ValueError):
        get_nino_region("Unknown")