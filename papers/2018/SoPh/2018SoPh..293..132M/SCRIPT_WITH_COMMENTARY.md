# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO interface (Fido) to query two instruments available in the VSO:
1. SDO/AIA – We query the AIA 171 Å channel around an event on 2015-09-23.
2. SOHO LASCO – We query the LASCO C2 coronagraph around the 2015-09-23 event for contextual white light images.
Note:
  • Although the context describes additional instruments such as the MWA and STEREO-A EUVI, 
    only instruments available in the VSO interface (SDO/AIA and SOHO LASCO) are queried.
  • The required query parameters are the time range and the instrument. Wavelength and detector 
    details are also provided to refine the queries where applicable.
"""

# Import necessary modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ---------------------------
# Query 1: SDO/AIA 171 Å Channel
# ---------------------------
# For the 2015-09-23 event, we choose an observational window spanning 10 minutes 
# starting at 03:07:45 UT. The AIA 171 Å channel is included (using a wavelength range of 170-175 Å to capture 
# the nominal 171 Å emission, given the available wavelength range "171.0 - 175.0" in the VSO interface).
aia_time_start = "2015-09-23 03:07:45"
aia_time_end = "2015-09-23 03:17:45"

# Construct the query for SDO/AIA with the desired time range and wavelength filter for 171 Å.
aia_query = Fido.search(a.Time(aia_time_start, aia_time_end),
                        a.Instrument("AIA"),
                        a.Wavelength(170 * u.angstrom, 175 * u.angstrom))

# Print the query results for SDO/AIA.
print("Query Results for SDO/AIA 171 Å Channel:")
print(aia_query)

# To download the data, you could use the following fetch command (commented out for now):
# aia_files = Fido.fetch(aia_query)

# ---------------------------
# Query 2: SOHO LASCO C2 Coronagraph
# ---------------------------
# For the context provided for the 2015-09-23 event, the nearest LASCO C2 image is noted at approximately 03:12:09 UT.
# We use a wider time window (e.g. 30 minutes) to ensure we capture a relevant image.
lasco_time_start = "2015-09-23 03:00:00"
lasco_time_end = "2015-09-23 03:30:00"

# Construct the query for SOHO LASCO, specifying the detector "C2" to match the instrument details.
lasco_query = Fido.search(a.Time(lasco_time_start, lasco_time_end),
                          a.Instrument("LASCO"),
                          a.Detector("C2"))

# Print the query results for SOHO LASCO C2.
print("\nQuery Results for SOHO LASCO C2 Coronagraph:")
print(lasco_query)

# To download the LASCO data, you could use the following fetch command (commented out for now):
# lasco_files = Fido.fetch(lasco_query)

if __name__ == "__main__":
    # The script prints out the query results for both instruments.
    pass
