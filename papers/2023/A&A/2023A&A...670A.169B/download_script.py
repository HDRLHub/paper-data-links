# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.vso as vso
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the query
time_range = a.Time('2014-09-28 02:39:00', '2014-09-28 03:24:05')

# Define the instrument for the query
instrument = a.Instrument('AIA')

# Define the wavelengths of interest (171, 193, 211 Å)
wavelengths = a.Wavelength(171 * u.Angstrom, 211 * u.Angstrom)

# Create the query
query = Fido.search(time_range, instrument, wavelengths)

# Print the query results
print(query)

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)

# Note: Be aware of potential pagination issues if the query returns a large number of results.
