# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface (Fido) to query solar observations 
from instruments used in the paper. Two main queries are constructed:

1. UVCS Observations from SOHO:
   - Data from the OVI channel (which covers wavelengths suitable for O vi 1032 Å and 1037 Å).
   - Time range corresponding to the paper's 400‐day observation period (1996 April 4 to 1997 May 15).

2. MDI Helioseismic Observations from SOHO:
   - Data corresponding to the p-mode Doppler measurements (LOS_velocity).
   - Time range chosen to represent the 144-day period (May 1996 to September 1996).

Note:
- The queries include only the necessary parameters: time range and instrument.
- The Fido.fetch commands are commented out. Simply uncomment them to download the data!
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ------------------------------
# Query 1: SOHO/UVCS Observations
# ------------------------------
# Define the time range for the UVCS observations (400-day period)
start_uvcs = '1996-04-04'
end_uvcs   = '1997-05-15'

# Build the search query for UVCS data
# We select:
# - Time range as defined above.
# - Instrument: UVCS from SOHO.
# - Detector: 'OVI' channel, which is optimized for the O vi lines (1032 Å and 1037 Å).
# - Physical Observable: intensity.
query_uvcs = Fido.search(
    a.Time(start_uvcs, end_uvcs),
    a.Source("SOHO"),
    a.Instrument("UVCS"),
    a.Detector("OVI"),
    a.Physobs("intensity")
)

# Print the query result summary for UVCS
print("UVCS Query Result:")
print(query_uvcs)

# Uncomment the following lines to fetch UVCS data
# files_uvcs = Fido.fetch(query_uvcs)
# print("Downloaded UVCS data files:")
# print(files_uvcs)

# -------------------------------------
# Query 2: SOHO/MDI Helioseismic Data
# -------------------------------------
# Define the time range for the MDI observations (a 144-day period from May to September 1996)
start_mdi = '1996-05-01'
end_mdi   = '1996-09-01'

# Build the search query for MDI data
# We select:
# - Time range as defined above.
# - Instrument: MDI from SOHO.
# - Detector: 'MDI'.
# - Physical Observable: LOS_velocity (Doppler measurements relevant for helioseismic studies).
query_mdi = Fido.search(
    a.Time(start_mdi, end_mdi),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Detector("MDI"),
    a.Physobs("LOS_velocity")
)

# Print the query result summary for MDI
print("\nMDI Query Result:")
print(query_mdi)

# Uncomment the following lines to fetch MDI data
# files_mdi = Fido.fetch(query_mdi)
# print("Downloaded MDI data files:")
# print(files_mdi)

if __name__ == "__main__":
    # The script prints out the query summaries.
    # Fetch commands are commented out for safety. Uncomment if data download is desired.
    pass
