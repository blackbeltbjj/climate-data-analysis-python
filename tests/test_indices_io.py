import pandas as pd
import pytest

from climate.indices import load_enso_csv


def test_load_csv_series(tmp_path):

    file = tmp_path / "enso.csv"

    pd.DataFrame(
        {
            "date": [
                "2000-01-01",
                "2000-02-01",
            ],
            "nino34": [
                0.5,
                0.8,
            ],
        }
    ).to_csv(
        file,
        index=False,
    )

    result = load_enso_csv(
        file,
        value_column="nino34",
    )

    assert isinstance(
        result,
        pd.Series,
    )


def test_missing_file():

    with pytest.raises(FileNotFoundError):
        load_enso_csv(
            "missing.csv"
        )


def test_missing_column(tmp_path):

    file = tmp_path / "enso.csv"

    pd.DataFrame(
        {
            "date": [
                "2000-01-01",
            ]
        }
    ).to_csv(
        file,
        index=False,
    )

    with pytest.raises(ValueError):
        load_enso_csv(
            file,
            value_column="nino34",
        )