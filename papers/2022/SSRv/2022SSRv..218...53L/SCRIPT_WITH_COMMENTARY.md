# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# Define the time ranges and instruments for the queries
time_ranges = [
    ("1996-05-01", "1997-12-31"),
    ("1998-01-01", "2020-12-31")
]

# Define the instruments and their respective wavelengths
instruments = [
    ("LASCO", "C2", 540 * u.nm, 640 * u.nm),
    ("LASCO", "C3", 540 * u.nm, 640 * u.nm)
]

# Perform the queries
for start_time, end_time in time_ranges:
    for instrument, detector, wave_min, wave_max in instruments:
        query = Fido.search(
            a.Time(start_time, end_time),
            a.Instrument(instrument),
            a.Detector(detector),
            a.Wavelength(wave_min, wave_max)
        )
        print(f"Query results for {instrument} {detector} from {start_time} to {end_time}:")
        print(query)
        # Uncomment the following line to fetch the data
        # files = Fido.fetch(query)
```

This script defines the time ranges and instruments for the queries, performs the queries using SunPy's Fido interface, and prints out the query results. The `Fido.fetch` commands are commented out to avoid downloading the data. The code is explicit and well-commented, reflecting the data used in the context provided.
