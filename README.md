Translate xarray datasets to a custom data model.

Contrary to netCDF the GRIB data format is not self-describing and several details of the mapping
to the *Unidata Common Data Model* are arbitrarily set by the software components decoding the format.
Details like names and units of the coordinates are particularly important because
*xarray* broadcast and selection rules depend on them.
`cf2cfm` is a small coordinate translation module that make it easy to
translate CF compliant coordinates to a user-defined
custom data model with set `out_name`, `units` and `stored_direction`.

For example to translate a *cfgrib* styled `xr.Dataset` to the classic *ECMWF* coordinate
naming conventions you can:

```python

>>> import cf2cdm
>>> ds = xr.open_dataset('era5-levels-members.grib', engine='cfgrib')
>>> cf2cdm.translate_coords(ds, cf2cdm.ECMWF)
<xarray.Dataset>
Dimensions:     (number: 10, time: 4, level: 2, latitude: 61, longitude: 120)
Coordinates:
  * number      (number) int64 0 1 2 3 4 5 6 7 8 9
  * time        (time) datetime64[ns] 2017-01-01 ... 2017-01-02T12:00:00
    step        timedelta64[ns] ...
  * level       (level) float64 850.0 500.0
  * latitude    (latitude) float64 90.0 87.0 84.0 81.0 ... -84.0 -87.0 -90.0
  * longitude   (longitude) float64 0.0 3.0 6.0 9.0 ... 348.0 351.0 354.0 357.0
    valid_time  (time) datetime64[ns] ...
Data variables:
    z           (number, time, level, latitude, longitude) float32 ...
    t           (number, time, level, latitude, longitude) float32 ...
Attributes:
    GRIB_edition:            1
    GRIB_centre:             ecmf
    GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
    GRIB_subCentre:          0
    Conventions:             CF-1.7
    institution:             European Centre for Medium-Range Weather Forecasts
    history:                 ...
```

To translate to the Common Data Model of the Climate Data Store use:

```python

>>> import cf2cdm
>>> cf2cdm.translate_coords(ds, cf2cdm.CDS)
<xarray.Dataset>
Dimensions:                  (realization: 10, forecast_reference_time: 4,
                              plev: 2, lat: 61, lon: 120)
Coordinates:
  * realization              (realization) int64 0 1 2 3 4 5 6 7 8 9
  * forecast_reference_time  (forecast_reference_time) datetime64[ns] 2017-01...
    leadtime                 timedelta64[ns] ...
  * plev                     (plev) float64 8.5e+04 5e+04
  * lat                      (lat) float64 -90.0 -87.0 -84.0 ... 84.0 87.0 90.0
  * lon                      (lon) float64 0.0 3.0 6.0 9.0 ... 351.0 354.0 357.0
    time                     (forecast_reference_time) datetime64[ns] ...
Data variables:
    z                        (realization, forecast_reference_time, plev, lat, lon) float32 ...
    t                        (realization, forecast_reference_time, plev, lat, lon) float32 ...
Attributes:
    GRIB_edition:            1
    GRIB_centre:             ecmf
    GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
    GRIB_subCentre:          0
    Conventions:             CF-1.7
    institution:             European Centre for Medium-Range Weather Forecasts
    history:                 ...
```

## License

```
Copyright 2017-2021 European Centre for Medium-Range Weather Forecasts (ECMWF).
Copyright 2023 B-Open Solutions srl.


Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
