# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the query
time_range = a.Time('1996-01-12', '2023-10-01')

# Define the instrument and physical observable
instrument = a.Instrument('swan')
wavelength = a.Wavelength(1215.6 * u.Angstrom)

# Construct the query
query = Fido.search(time_range, instrument, wavelength)

# Print out the query results
print(query)

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
```

This script constructs a query to download data from the SWAN instrument on board SOHO, focusing on Lyα emissions. The time range is set from the start of the available data to the present. The wavelength is specified as 1215.6 Å, which corresponds to Lyα emissions. The query results are printed out, and the data fetching command is commented out.
