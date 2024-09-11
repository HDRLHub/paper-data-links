# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the observations
time_range = a.Time('2015-07-19', '2015-07-19')

# Define the instruments and their respective attributes based on the context provided
# AIA Instrument on SDO
aia_query = Fido.search(time_range, a.Instrument('AIA'), a.Wavelength(171 * u.Angstrom) | a.Wavelength(193 * u.Angstrom) | a.Wavelength(304 * u.Angstrom))

# GONG Instrument
gong_query = Fido.search(time_range, a.Instrument('GONG'), a.Physobs('intensity'), a.Wavelength(6562.8 * u.Angstrom))

# HMI Instrument on SDO
hmi_query = Fido.search(time_range, a.Instrument('HMI'), a.Physobs('LOS_magnetic_field'))

# LASCO Instrument on SOHO
lasco_query = Fido.search(time_range, a.Instrument('LASCO'), a.Physobs('intensity'))

# Print out the query results
print("AIA Query Results:")
print(aia_query)
print("\nGONG Query Results:")
print(gong_query)
print("\nHMI Query Results:")
print(hmi_query)
print("\nLASCO Query Results:")
print(lasco_query)

# Note: If the results are too large, consider pagination

# Uncomment the following lines to fetch the data
# aia_download = Fido.fetch(aia_query)
# gong_download = Fido.fetch(gong_query)
# hmi_download = Fido.fetch(hmi_query)
# lasco_download = Fido.fetch(lasco_query)
