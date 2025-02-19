# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client (Fido) to query solar data relevant to our study of plasmoid evolution associated with the X8.3 flare on September 10, 2017.
We construct queries for:
  1. SDO/AIA data at 131 Å covering the time from 15:30 UT to 19:00 UT on September 10, 2017.
  2. SOHO/LASCO data from the C2 detector covering the outer corona from 17:00 UT to 20:00 UT on September 10, 2017.

Note: The K-Cor instrument is used in the study but is not available in the VSO interface provided. Similarly, while LASCO/C3 data is mentioned, no specific time range is provided so we only query LASCO/C2 here.
"""

# Import required modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ---------------------------
# Query 1: SDO/AIA (131 Å)
# ---------------------------
# Define the time range for the AIA observation.
time_start_aia = "2017-09-10T15:30:00"
time_end_aia   = "2017-09-10T19:00:00"

# The wavelength for AIA is specified as 131 Å.
wavelength_aia = 131 * u.Angstrom

# Build the query for SDO/AIA data. 
# We use the instrument, source, time, and wavelength attributes.
query_aia = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Wavelength(wavelength_aia, wavelength_aia)
)

print("Query Results for SDO/AIA (131 Å):")
print(query_aia)

# Uncomment the line below to download the AIA data:
# downloaded_files_aia = Fido.fetch(query_aia)

# ---------------------------
# Query 2: SOHO/LASCO - Detector C2 (White-light coronagraph)
# ---------------------------
# Define the time range for LASCO/C2 observation.
# The study tracks plasmoids in the outer corona up to 20:00 UT on September 10, 2017.
time_start_lasco = "2017-09-10T17:00:00"
time_end_lasco   = "2017-09-10T20:00:00"

# Build the query for SOHO/LASCO data from detector C2.
# Note that for LASCO, the VSO uses attributes for instrument "LASCO" with the appropriate detector specified.
query_lasco_c2 = Fido.search(
    a.Time(time_start_lasco, time_end_lasco),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Source("SOHO")
)

print("\nQuery Results for SOHO/LASCO (Detector C2) White-light Data:")
print(query_lasco_c2)

# Uncomment the line below to download the LASCO/C2 data:
# downloaded_files_lasco_c2 = Fido.fetch(query_lasco_c2)

if __name__ == "__main__":
    # The main block can be used to execute additional commands or checks if needed.
    pass
