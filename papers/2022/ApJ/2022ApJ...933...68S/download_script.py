# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the time ranges for the observations
time_range_aia = a.Time('2010-10-07 03:19:34', '2010-10-07 23:59:59')
time_range_lasco = a.Time('2010-10-07 07:24:05', '2010-10-07 23:59:59')
time_range_stereo = a.Time('2010-10-07 09:46:15', '2010-10-07 23:59:59')

# Define the instruments and wavelengths for the queries
instrument_aia = a.Instrument('AIA')
wavelength_aia_193 = a.Wavelength(193 * u.Angstrom)
wavelength_aia_304 = a.Wavelength(304 * u.Angstrom)
instrument_lasco = a.Instrument('LASCO')  # LASCO observes in white-light, so no specific wavelength is needed
instrument_stereo_secchi = a.Instrument('SECCHI')
detector_stereo_euvi = a.Detector('EUVI')
wavelength_stereo_304 = a.Wavelength(304 * u.Angstrom)
wavelength_stereo_195 = a.Wavelength(195 * u.Angstrom)
detector_stereo_cor1 = a.Detector('COR1')
detector_stereo_cor2 = a.Detector('COR2')  # COR1 and COR2 observe in white-light, so no specific wavelength is needed

# Perform the queries
# Query for AIA data
query_aia_193 = Fido.search(time_range_aia, instrument_aia, wavelength_aia_193)
query_aia_304 = Fido.search(time_range_aia, instrument_aia, wavelength_aia_304)

# Query for LASCO data
query_lasco = Fido.search(time_range_lasco, instrument_lasco)

# Query for STEREO EUVI data
query_stereo_euvi_304 = Fido.search(time_range_stereo, instrument_stereo_secchi, detector_stereo_euvi, wavelength_stereo_304)
query_stereo_euvi_195 = Fido.search(time_range_stereo, instrument_stereo_secchi, detector_stereo_euvi, wavelength_stereo_195)

# Query for STEREO COR1 and COR2 data
query_stereo_cor1 = Fido.search(time_range_stereo, instrument_stereo_secchi, detector_stereo_cor1)
query_stereo_cor2 = Fido.search(time_range_stereo, instrument_stereo_secchi, detector_stereo_cor2)

# Print the query results
# Note: Large number of results may indicate pagination; consider handling it if necessary
print("AIA 193 Å Query Results:")
print(query_aia_193)
print("\nAIA 304 Å Query Results:")
print(query_aia_304)
print("\nLASCO Query Results:")
print(query_lasco)
print("\nSTEREO EUVI 304 Å Query Results:")
print(query_stereo_euvi_304)
print("\nSTEREO EUVI 195 Å Query Results:")
print(query_stereo_euvi_195)
print("\nSTEREO COR1 Query Results:")
print(query_stereo_cor1)
print("\nSTEREO COR2 Query Results:")
print(query_stereo_cor2)

# Uncomment the following lines to fetch the data
# Fido.fetch(query_aia_193)
# Fido.fetch(query_aia_304)
# Fido.fetch(query_lasco)
# Fido.fetch(query_stereo_euvi_304)
# Fido.fetch(query_stereo_euvi_195)
# Fido.fetch(query_stereo_cor1)
# Fido.fetch(query_stereo_cor2)
