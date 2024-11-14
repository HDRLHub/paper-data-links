# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u  # Import units from astropy

# Define the time range for the query
time_range = a.Time('1997-04-20T00:00:00', '1997-04-20T23:59:59')

# Define the instrument and source
instrument = a.Instrument('SUMER')
source = a.Source('SOHO')

# Define the wavelength range in Angstroms
wavelength = a.Wavelength(670 * u.Angstrom, 1520 * u.Angstrom)

# Construct the query
query = Fido.search(time_range, instrument, source, wavelength)

# Print the query results
print(query)

# Note: If the query returns a large number of results, pagination might occur.

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
