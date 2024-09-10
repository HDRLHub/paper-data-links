# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time ranges for the observations
time_range_aia = a.Time('2014-08-25T15:15:00', '2014-08-25T15:27:00')
# Broaden the time range slightly for LASCO to avoid missing data
time_range_lasco = a.Time('2014-08-25T15:30:00', '2014-08-25T15:40:00')  # Adjusted time range

# Define the instruments and wavelengths
instrument_aia = a.Instrument('AIA')
wavelength_aia = a.Wavelength(171 * u.Angstrom)
instrument_lasco = a.Instrument('LASCO')
detector_lasco = a.Detector('C2')

# Construct the query for SDO-AIA data
query_aia = Fido.search(time_range_aia, instrument_aia, wavelength_aia)
print("SDO-AIA Query Results:")
print(query_aia)

# Add a comment to warn the user about potential pagination issues
# Note: If the number of results is very large, consider breaking down the time range to avoid pagination issues.

# Construct the query for SOHO/LASCO-C2 data
query_lasco = Fido.search(time_range_lasco, instrument_lasco, detector_lasco)
print("SOHO/LASCO-C2 Query Results:")
print(query_lasco)

# Uncomment the following lines to fetch the data
# files_aia = Fido.fetch(query_aia)
# files_lasco = Fido.fetch(query_lasco)
