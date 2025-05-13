# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses Sunpy's VSO interface to query for solar data related to the 2015 June 25 event.
Based on the scientific context, we want to obtain data from:
  1. SDO/AIA: to capture the coronal dimming associated with the CME onset (around 9:50 UT on 2015 June 25).
  2. SOHO/LASCO C2: to capture white-light images of the CME as it appears in the coronagraph (starting at ~10:57 UT on 2015 June 25).

Note:
  - LOFAR is a key instrument in the study, but it is not available in the provided VSO interface.
  - The queries below use the time ranges and instruments that are available from the VSO interface.
"""

from sunpy.net import Fido, attrs as a

# -------------------------------------------------------------------
# Query 1: SDO/AIA observations for active region dimming
# -------------------------------------------------------------------
# Define time range for AIA data (active region dimming observed around 9:50 UT on 2015 June 25).
start_time_aia = '2015-06-25T09:50:00'
end_time_aia   = '2015-06-25T10:00:00'

# Query the VSO for SDO/AIA data.
# Note: SDO/AIA observations are often performed in multiple EUV wavelengths.
query_aia = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Instrument('AIA'),
    a.Source('SDO')
)

# Print the query results for SDO/AIA.
print("SDO/AIA Query Result:")
print(query_aia)

# Uncomment the following line to download the AIA data.
# downloaded_aia = Fido.fetch(query_aia)

# -------------------------------------------------------------------
# Query 2: SOHO/LASCO C2 observations for CME detection
# -------------------------------------------------------------------
# Define time range for LASCO C2 data (CME first appearance around 10:57 UT on 2015 June 25).
start_time_lasco = '2015-06-25T10:57:00'
end_time_lasco   = '2015-06-25T11:20:00'

# Query the VSO for SOHO/LASCO data with detector C2.
query_lasco = Fido.search(
    a.Time(start_time_lasco, end_time_lasco),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Source('SOHO')
)

# Print the query results for SOHO/LASCO C2.
print("SOHO/LASCO C2 Query Result:")
print(query_lasco)

# Uncomment the following line to download the LASCO C2 data.
# downloaded_lasco = Fido.fetch(query_lasco)

if __name__ == "__main__":
    print("Queries completed. Check the above output for search results.")
