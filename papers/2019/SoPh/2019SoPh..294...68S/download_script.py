# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client (Fido) to query solar observations from SDO/AIA and SDO/HMI.
The queries are based on the observational parameters provided in the context:
• For SDO/AIA, the imaging data are used to study the multi-wavelength evolution of a quiet‐Sun blowout jet.
  Time Range: 2014 May 16, 03:30:00 UT to 2014 May 16, 05:10:00 UT.
• For SDO/HMI, the magnetogram data are used to study the line-of-sight magnetic field evolution.
  Time Range: 2014 May 16, 02:59:24 UT to 2014 May 16, 05:30:54 UT.
Note: Fido.fetch calls are commented out. Instead, we print the query results.
"""

from sunpy.net import Fido, attrs as a
from sunpy import log

# Increase logging level to see the details of query if needed
log.setLevel('INFO')

# ----------------------------
# Query 1: SDO/AIA (Atmospheric Imaging Assembly)
# ----------------------------
# The query for SDO/AIA is set for the multi-wavelength imaging data covering the full disk.
# The AIA instrument from SDO provides several UV and EUV wavelength channels.
# Here, we query for all available wavelengths within the available data in the given time range.
aia_time_start = "2014-05-16T03:30:00"
aia_time_end   = "2014-05-16T05:10:00"
query_aia = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Source('SDO'),
    a.Instrument('AIA')
)

# Print out the result for the AIA query
print("Query Result for SDO/AIA:")
print(query_aia)

# Uncomment the line below to fetch the data (fetching is disabled as per instructions)
# aia_files = Fido.fetch(query_aia)

# ----------------------------
# Query 2: SDO/HMI (Helioseismic Magnetic Imager)
# ----------------------------
# The query for SDO/HMI targets the line-of-sight magnetic field observations.
# HMI observes the Sun in the Fe I 6173 Å spectral line.
# We use the time range specified to capture the magnetic evolution associated with the jet.
hmi_time_start = "2014-05-16T02:59:24"
hmi_time_end   = "2014-05-16T05:30:54"
query_hmi = Fido.search(
    a.Time(hmi_time_start, hmi_time_end),
    a.Source('SDO'),
    a.Instrument('HMI')
)

# Print out the result for the HMI query
print("\nQuery Result for SDO/HMI:")
print(query_hmi)

# Uncomment the line below to fetch the data (fetching is disabled as per instructions)
# hmi_files = Fido.fetch(query_hmi)

if __name__ == "__main__":
    print("\nSunPy VSO queries executed. Review the printed query results for details.")
