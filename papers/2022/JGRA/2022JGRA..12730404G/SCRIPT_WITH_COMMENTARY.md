# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Define the time ranges and instruments based on the context provided
time_ranges = {
    "AIA_193": TimeRange("2018-08-20 00:00", "2018-08-20 23:59"),
    "AIA_211": TimeRange("2018-08-20 08:00", "2018-08-21 08:00"),
    "HMI": TimeRange("2018-08-21 06:00", "2018-08-21 06:30"),
    "LASCO": TimeRange("2018-08-20 21:24", "2018-08-21 23:59"),
    "SECCHI_COR2": TimeRange("2018-08-20 12:00", "2018-08-21 23:59"),
    "SECCHI_HI1": TimeRange("2018-08-22 04:30", "2018-08-22 05:00")
}

# Define the instruments and wavelengths
instruments = {
    "AIA_193": {"instrument": "AIA", "wavelength": 193 * a.u.Angstrom},
    "AIA_211": {"instrument": "AIA", "wavelength": 211 * a.u.Angstrom},
    "HMI": {"instrument": "HMI"},
    "LASCO": {"instrument": "LASCO"},
    "SECCHI_COR2": {"instrument": "SECCHI", "detector": "COR2"},
    "SECCHI_HI1": {"instrument": "SECCHI", "detector": "HI1"}
}

# Perform the queries
queries = {}
for key, time_range in time_ranges.items():
    instrument_attrs = instruments[key]
    query = Fido.search(a.Time(time_range.start, time_range.end), a.Instrument(instrument_attrs["instrument"]))
    if "wavelength" in instrument_attrs:
        query &= a.Wavelength(instrument_attrs["wavelength"])
    if "detector" in instrument_attrs:
        query &= a.Detector(instrument_attrs["detector"])
    queries[key] = query

# Print out the query results
for key, query in queries.items():
    print(f"Query results for {key}:")
    print(query)
    print("\n")

# Uncomment the following lines to fetch the data
# for key, query in queries.items():
#     Fido.fetch(query)
```
