# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time ranges for the observations
time_range_aia = a.Time('2014-08-25T15:15:00', '2014-08-25T15:27:00')
time_range_lasco = a.Time('2014-08-25T15:36:00', '2014-08-25T15:36:00')

# Define the instruments and wavelengths
instrument_aia = a.Instrument('AIA')
wavelength_aia = a.Wavelength(171 * u.Angstrom)

instrument_lasco = a.Instrument('LASCO')
detector_lasco = a.Detector('C2')

# Construct the query for SDO-AIA data
query_aia = Fido.search(time_range_aia, instrument_aia, wavelength_aia)
print("SDO-AIA Query Results:")
print(query_aia)

# Construct the query for SOHO/LASCO-C2 data
query_lasco = Fido.search(time_range_lasco, instrument_lasco, detector_lasco)
print("SOHO/LASCO-C2 Query Results:")
print(query_lasco)

# Uncomment the following lines to fetch the data
# files_aia = Fido.fetch(query_aia)
# files_lasco = Fido.fetch(query_lasco)
```

This script constructs and prints the queries for the specified time ranges and instruments. The `Fido.fetch` commands are commented out to prevent actual data download. The code is explicit and well-commented, reflecting the data used in the context provided.
