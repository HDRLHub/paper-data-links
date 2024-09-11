# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a
import astropy.units as u  # Import the astropy.units module

# Define the time ranges and instrument details based on the context provided
time_range_1 = a.Time('2010-08-14 08:40', '2014-12-21 10:50')
time_range_2 = a.Time('2017-10-25 06:45', '2021-11-17 08:00')
instrument = a.Instrument('AIA')
wavelength = a.Wavelength(193 * u.Angstrom)

# Construct the first query for the general CME detection and analysis period
# Note: The time range might be too broad, consider narrowing it down if no results are returned
query_1 = Fido.search(time_range_1, instrument, wavelength)
print("Query 1 Results:")
print(query_1)

# Construct the second query for the verification against CDAW catalogue period
# Note: The time range might be too broad, consider narrowing it down if no results are returned
query_2 = Fido.search(time_range_2, instrument, wavelength)
print("Query 2 Results:")
print(query_2)

# Uncomment the following lines to fetch the data
# files_1 = Fido.fetch(query_1)
# files_2 = Fido.fetch(query_2)
