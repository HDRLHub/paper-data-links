# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import sunpy.net.vso as vso
from sunpy.net import Fido, attrs as a

# Define the time range for the query
time_range = a.Time('2014-09-28 02:39:00', '2014-09-28 03:24:05')

# Define the instrument for the query
instrument = a.Instrument('AIA')

# Define the wavelengths of interest (171, 193, 211 Å)
wavelengths = [a.Wavelength(171 * u.Angstrom), a.Wavelength(193 * u.Angstrom), a.Wavelength(211 * u.Angstrom)]

# Create the query
query = Fido.search(time_range, instrument, *wavelengths)

# Print the query results
print(query)

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
```

This script sets up a query to the VSO for data from the SDO/AIA instrument within the specified time range and wavelengths. The `Fido.search` function is used to perform the query, and the results are printed out. The `Fido.fetch` command is commented out to prevent automatic downloading of the data.
