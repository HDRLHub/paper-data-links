# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use sunpy's VSO client to query
for data from SOHO instruments available in the VSO interface.
Based on the provided Scientific Observation Instrumentation Form,
we will query data for the SOHO/EIT instrument and the SOHO/LASCO (specifically LASCO/C2)
for the 23 July 2004 event.

The SOHO/EIT query is intended to capture the filament eruption visible
in EIT images around 18:48 UT on 23 July 2004, while the SOHO/LASCO query (using detector C2)
will cover the halo CME observed around the event (noting that LASCO/C1 is not available for 2004).
"""

# Import necessary libraries from sunpy
from sunpy.net import Fido, attrs as a

# Define the time ranges for the 23 July 2004 event.
# SOHO/EIT observed filament eruption: around 18:48 UT.
eit_start_time = "2004-07-23T18:40:00"
eit_end_time   = "2004-07-23T18:55:00"

# LASCO/C2 captured the halo CME; we choose a time window
# that covers the last CME observation (~17:42 UT) near the type II feature.
lasco_start_time = "2004-07-23T17:00:00"
lasco_end_time   = "2004-07-23T18:30:00"

# ---------------------------
# Query 1: SOHO/EIT
# ---------------------------
# Here we construct a query for SOHO/EIT data.
# The available wavelengths for EIT in the VSO are: 171, 195, 284, 304 Angstroms.
# (For this example, we do not constrain the wavelength so that all channels are returned.)
query_eit = Fido.search(
    a.Time(eit_start_time, eit_end_time),
    a.Source("SOHO"),
    a.Instrument("EIT"),
    a.Detector("EIT")
)
# Print out the query results for SOHO/EIT.
print("Query Results for SOHO/EIT:")
print(query_eit)

# Uncomment the line below to fetch the SOHO/EIT data (if desired).
# downloaded_files_eit = Fido.fetch(query_eit)

# ---------------------------
# Query 2: SOHO/LASCO (using detector C2)
# ---------------------------
# Construct a query for SOHO LASCO data.
# Note: LASCO/C1 is not available for 2004, so we use LASCO/C2 which is available from 1995/12/08.
query_lasco = Fido.search(
    a.Time(lasco_start_time, lasco_end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
# Print out the query results for SOHO/LASCO.
print("\nQuery Results for SOHO/LASCO (C2):")
print(query_lasco)

# Uncomment the line below to fetch the SOHO/LASCO data (if desired).
# downloaded_files_lasco = Fido.fetch(query_lasco)

# End of script.
if __name__ == "__main__":
    print("\nSunpy VSO query script executed successfully.")
