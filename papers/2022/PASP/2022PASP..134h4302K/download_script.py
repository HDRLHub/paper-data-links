# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the query
# Using a smaller example time range due to potential issues with broad time ranges
time_range = a.Time('1996-01-12', '1996-01-19')  # Example time range
# Full time range: a.Time('1996-01-12', '2023-10-01')

# Define the instrument and physical observable
instrument = a.Instrument('swan')
wavelength = a.Wavelength(1215.6 * u.Angstrom)

# Construct the query
query = Fido.search(time_range, instrument, wavelength)

# Print out the query results
print(query)

# Note: The query results may be paginated due to the large number of results.
# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
