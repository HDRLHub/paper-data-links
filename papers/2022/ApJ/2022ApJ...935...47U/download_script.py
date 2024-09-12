# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido
import sunpy.net.attrs as a
from sunpy.time import parse_time
import astropy.units as u

# Define the time ranges for the two phases
time_range1 = a.Time(parse_time("2011-06-07 05:40"), parse_time("2011-06-07 06:22"))
time_range2 = a.Time(parse_time("2011-06-07 06:22"), parse_time("2011-06-07 08:00"))

# Define the instrument and wavelength
instrument = a.Instrument('AIA')
wavelength = a.Wavelength(193 * u.Angstrom)

# Construct the query for the initial eruption and rising phase
query1 = Fido.search(time_range1, instrument, wavelength)
print("Query Results for Initial Eruption and Rising Phase:")
print(query1)

# Construct the query for the falling phase
query2 = Fido.search(time_range2, instrument, wavelength)
print("Query Results for Falling Phase:")
print(query2)

# Uncomment the following lines to fetch the data
# files1 = Fido.fetch(query1)
# files2 = Fido.fetch(query2)
