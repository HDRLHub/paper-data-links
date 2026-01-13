# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a
from sunpy.time import parse_time

# Define the time ranges and instruments based on the context
time_range_iris = a.Time('2014-02-21T11:24:46', '2014-02-21T12:24:46')
time_range_sdo_aia = a.Time('2014-02-21T11:24:46', '2014-02-21T12:24:46')

# Define the instruments and wavelengths
instrument_iris = a.Instrument('IRIS')
# Adjusted wavelength ranges for IRIS
wavelength_iris_si_iv = a.Wavelength(1393.0 * u.Angstrom, 1407.0 * u.Angstrom)
wavelength_iris_mg_ii = a.Wavelength(2794.0 * u.Angstrom, 2806.0 * u.Angstrom)
instrument_sdo_aia = a.Instrument('AIA')
wavelength_sdo_aia = a.Wavelength(17.1 * u.nm, 17.1 * u.nm)

# Construct the queries
query_iris_si_iv = Fido.search(time_range_iris, instrument_iris, wavelength_iris_si_iv)
query_iris_mg_ii = Fido.search(time_range_iris, instrument_iris, wavelength_iris_mg_ii)
query_sdo_aia = Fido.search(time_range_sdo_aia, instrument_sdo_aia, wavelength_sdo_aia)

# Print out the query results
print("IRIS Si IV 140 nm Query Results:")
print(query_iris_si_iv)
print("\nIRIS Mg II k 279.6 nm Query Results:")
print(query_iris_mg_ii)
print("\nSDO/AIA 17.1 nm Query Results:")
print(query_sdo_aia)

# Note: The SDO/AIA query returns 300 results, indicating pagination.
# Uncomment the following lines to fetch the data
# files_iris_si_iv = Fido.fetch(query_iris_si_iv)
# files_iris_mg_ii = Fido.fetch(query_iris_mg_ii)
# files_sdo_aia = Fido.fetch(query_sdo_aia)
