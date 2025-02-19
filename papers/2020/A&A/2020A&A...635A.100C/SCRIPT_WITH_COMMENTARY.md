# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO (Virtual Solar Observatory) interface to query data for an event studied in the paper.
The paper focuses on the early CME evolution with multi-viewpoint observations using different instruments:
    1. STEREO/SECCHI EUVI (from STEREO-B) capturing the low-corona in 195 Å.
    2. SDO/AIA capturing the low-corona in 193 Å.
    3. SOHO/LASCO C2 providing white-light coronagraph imagery.
Each query is defined over a very short time interval corresponding to the specific image timestamp indicated in the paper.
Note: The actual data download (Fido.fetch) has been commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# --------------------------
# Query 1: STEREO/SECCHI EUVI on board STEREO-B
# Event: 14 December 2010; time stamp at 15:20 UT, wavelength 195 Å as indicated in the paper.
time_euvi = a.Time("2010-12-14T15:20:00", "2010-12-14T15:20:00")
query_euvi = Fido.search(
    time_euvi,
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    a.Wavelength(195 * u.angstrom)
)
print("Query results for STEREO/SECCHI EUVI (STEREO-B, 195 Å):")
print(query_euvi)

# --------------------------
# Query 2: SDO/AIA on board SDO
# Event: 14 December 2010; time stamp at 15:20 UT, wavelength 193 Å as per the paper.
time_aia = a.Time("2010-12-14T15:20:00", "2010-12-14T15:20:00")
query_aia = Fido.search(
    time_aia,
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.angstrom)
)
print("\nQuery results for SDO/AIA (193 Å):")
print(query_aia)

# --------------------------
# Query 3: SOHO/LASCO C2 on board SOHO
# Event: 14 December 2010; time stamp at 15:59 UT.
# LASCO C2 observes in white-light, so we do not specify a wavelength.
time_lasco = a.Time("2010-12-14T15:59:00", "2010-12-14T15:59:00")
query_lasco = Fido.search(
    time_lasco,
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nQuery results for SOHO/LASCO C2 (white-light):")
print(query_lasco)

# --------------------------
# Optionally, fetch the data:
# The following lines are commented out to avoid downloading data during execution.
# fetched_euvi = Fido.fetch(query_euvi)
# fetched_aia = Fido.fetch(query_aia)
# fetched_lasco = Fido.fetch(query_lasco)

if __name__ == '__main__':
    # This script prints out the query details.
    pass
