# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time ranges and instruments for the queries based on the context provided
# We will query data for SDO/AIA and SOHO/LASCO C2 instruments

# SDO/AIA EUV observations for PSP Encounter 1
time_range_aia_1 = a.Time('2018-10-01', '2018-11-30')
instrument_aia = a.Instrument('AIA')
# Corrected to use a valid wavelength range
wavelengths_aia = a.Wavelength(171 * u.Angstrom, 304 * u.Angstrom)

# SDO/AIA EUV observations for PSP Encounter 2
time_range_aia_2 = a.Time('2019-03-01', '2019-04-30')

# SDO/AIA EUV observations for PSP Encounter 3
time_range_aia_3 = a.Time('2019-08-01', '2019-09-30')

# SOHO/LASCO C2 white-light observations for PSP Encounter 1
time_range_lasco_1 = a.Time('2018-10-30', '2018-11-13')
instrument_lasco = a.Instrument('LASCO')
detector_lasco = a.Detector('C2')

# SOHO/LASCO C2 white-light observations for PSP Encounter 2
time_range_lasco_2 = a.Time('2019-03-01', '2019-04-30')

# SOHO/LASCO C2 white-light observations for PSP Encounter 3
time_range_lasco_3 = a.Time('2019-08-01', '2019-09-30')

# Perform the queries for SDO/AIA
print("Querying SDO/AIA data for PSP Encounter 1...")
query_aia_1 = Fido.search(time_range_aia_1, instrument_aia, wavelengths_aia)
print(query_aia_1)

print("Querying SDO/AIA data for PSP Encounter 2...")
query_aia_2 = Fido.search(time_range_aia_2, instrument_aia, wavelengths_aia)
print(query_aia_2)

print("Querying SDO/AIA data for PSP Encounter 3...")
query_aia_3 = Fido.search(time_range_aia_3, instrument_aia, wavelengths_aia)
print(query_aia_3)

# Perform the queries for SOHO/LASCO C2
print("Querying SOHO/LASCO C2 data for PSP Encounter 1...")
query_lasco_1 = Fido.search(time_range_lasco_1, instrument_lasco, detector_lasco)
print(query_lasco_1)

print("Querying SOHO/LASCO C2 data for PSP Encounter 2...")
query_lasco_2 = Fido.search(time_range_lasco_2, instrument_lasco, detector_lasco)
print(query_lasco_2)

print("Querying SOHO/LASCO C2 data for PSP Encounter 3...")
query_lasco_3 = Fido.search(time_range_lasco_3, instrument_lasco, detector_lasco)
print(query_lasco_3)

# Uncomment the following lines to fetch the data
# Fido.fetch(query_aia_1)
# Fido.fetch(query_aia_2)
# Fido.fetch(query_aia_3)
# Fido.fetch(query_lasco_1)
# Fido.fetch(query_lasco_2)
# Fido.fetch(query_lasco_3)
