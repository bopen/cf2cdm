import os.path

import xarray as xr

from cf2cdm import cfcoords, datamodels

SAMPLE_DATA_FOLDER = os.path.join(os.path.dirname(__file__), "sample-data")
TEST_DATA1 = os.path.join(SAMPLE_DATA_FOLDER, "era5-levels-members.zarr")
TEST_DATA2 = os.path.join(SAMPLE_DATA_FOLDER, "lambert_grid.zarr")


def test_cds() -> None:
    ds = xr.open_dataset(TEST_DATA1)

    res = cfcoords.translate_coords(ds, coord_model=datamodels.CDS)

    assert set(res.dims) == {
        "forecast_reference_time",
        "lat",
        "lon",
        "plev",
        "realization",
    }
    assert set(res.coords) == {
        "forecast_reference_time",
        "lat",
        "leadtime",
        "lon",
        "plev",
        "realization",
        "time",
    }

    ds = xr.open_dataset(TEST_DATA2)

    res = cfcoords.translate_coords(ds, coord_model=datamodels.CDS)

    assert set(res.dims) == {"x", "y"}
    assert set(res.coords) == {
        "forecast_reference_time",
        "heightAboveGround",
        "lat",
        "leadtime",
        "lon",
        "time",
    }


def test_ecmwf() -> None:
    ds = xr.open_dataset(TEST_DATA1)

    res = cfcoords.translate_coords(ds, coord_model=datamodels.ECMWF)

    assert set(res.dims) == {"latitude", "level", "longitude", "number", "time"}
    assert set(res.coords) == {
        "latitude",
        "level",
        "longitude",
        "number",
        "step",
        "time",
        "valid_time",
    }

    ds = xr.open_dataset(TEST_DATA2)

    res = cfcoords.translate_coords(ds, coord_model=datamodels.ECMWF)

    assert set(res.dims) == {"x", "y"}
    assert set(res.coords) == {
        "heightAboveGround",
        "latitude",
        "longitude",
        "step",
        "time",
        "valid_time",
    }
