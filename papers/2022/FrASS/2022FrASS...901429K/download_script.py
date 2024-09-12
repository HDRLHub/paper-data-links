# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range and instruments based on the context provided
# Time range for AIA observations is not explicitly provided, so we will use a general range
# Define the time range for AIA observations (example range)
time_range_aia = a.Time('2010-05-12', '2010-05-13')  # Example time range

# Define the time range for ERNE observations
# Using a smaller example time range to avoid pagination issues
time_range_erne = a.Time('2010-01-01', '2010-01-31')  # Example smaller time range
# Original time range: a.Time('2010-01-01', '2017-12-31')

# Define the instruments
instrument_aia = a.Instrument('AIA')
instrument_erne = a.Instrument('ERNE')

# Define the wavelength for AIA (EUV wavelengths)
wavelength_aia = a.Wavelength(94 * u.Angstrom, 335 * u.Angstrom)

# Define the physical observable for ERNE (proton events in the energy range of 17-22 MeV)
# Note: ERNE does not use wavelength, so we do not specify it

# Construct the query for AIA observations
query_aia = Fido.search(time_range_aia, instrument_aia, wavelength_aia)

# Construct the query for ERNE observations
query_erne = Fido.search(time_range_erne, instrument_erne)

# Print out the query results
print("AIA Query Results:")
print(query_aia)

print("\nERNE Query Results:")
print(query_erne)

# Uncomment the following lines to fetch the data
# files_aia = Fido.fetch(query_aia)
# files_erne = Fido.fetch(query_erne)
