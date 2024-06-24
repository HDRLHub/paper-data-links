# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period for the Hα Lyot Filtergraph
ha_lyot_time_range = a.Time('2006-10-21T22:50:00', '2006-10-22T01:27:00')
ha_lyot_instrument = a.Instrument("Hα Lyot Filtergraph")
ha_lyot_wavelengths = a.Wavelength(6563 * u.AA - 5 * u.AA, 6563 * u.AA + 1.2 * u.AA)  # Approximate range around Hα

# Define the observation period for the Vector Magnetograph - Slit fixed mode
vector_magnetograph_time_range_fixed = a.Time('2006-10-21T23:03:00', '2006-10-22T00:53:00')
vector_magnetograph_instrument = a.Instrument("Vector Magnetograph")
vector_magnetograph_wavelengths_fixed = a.Wavelength(6301.5 * u.AA, 6302.5 * u.AA)

# Define the observation period for the Vector Magnetograph - Slit scan mode
vector_magnetograph_time_range_scan = a.Time('2006-10-22T01:00:00', '2006-10-22T01:25:00')
vector_magnetograph_wavelengths_scan = a.Wavelength(6301.5 * u.AA, 6302.5 * u.AA)

# Perform the queries for each instrument and mode
ha_lyot_query = Fido.search(ha_lyot_time_range, ha_lyot_instrument, ha_lyot_wavelengths)
vector_magnetograph_query_fixed = Fido.search(vector_magnetograph_time_range_fixed, vector_magnetograph_instrument, vector_magnetograph_wavelengths_fixed)
vector_magnetograph_query_scan = Fido.search(vector_magnetograph_time_range_scan, vector_magnetograph_instrument, vector_magnetograph_wavelengths_scan)

# Display the query results for each instrument and mode
print("Query for Hα Lyot Filtergraph observations:")
print(ha_lyot_query)
print("Query for Vector Magnetograph (fixed mode) observations:")
print(vector_magnetograph_query_fixed)
print("Query for Vector Magnetograph (scan mode) observations:")
print(vector_magnetograph_query_scan)

# Uncomment the lines below to download the data
# ha_lyot_files = Fido.fetch(ha_lyot_query)
# vector_magnetograph_files_fixed = Fido.fetch(vector_magnetograph_query_fixed)
# vector_magnetograph_files_scan = Fido.fetch(vector_magnetograph_query_scan)
