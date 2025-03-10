# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query solar data from the Virtual Solar Observatory.
We perform two separate queries based on the context provided:
1. SDO AIA observations of the microflare event on 2011-09-03 (around 14:20–14:30 UT).
2. SoHO SUMER observations of the microflare on 2011 November 8 (from 14:52 UT to 18:02 UT).

Note:
- Only instruments available in the provided VSO interface are used.
- The required query parameters from the context are the time range and instrument.
- The Fido.fetch() commands are commented out. You can uncomment them if you wish to download the data.
"""

from sunpy.net import Fido, attrs as a

# ------------------------------
# Query 1: SDO AIA microflare event on 2011-09-03
# ------------------------------
# Define the time range for the microflare event around the observed peak (14:20 to 14:30 UT)
start_time_aia = '2011-09-03T14:20:00'
end_time_aia   = '2011-09-03T14:30:00'

# Construct the query for SDO AIA using the instrument "AIA" from source "SDO"
query_aia = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Instrument('AIA'),
    a.Source('SDO')
)

# Print the query summary for SDO AIA
print("Query Result for SDO AIA microflare event (2011-09-03 14:20-14:30 UT):")
print(query_aia)

# Uncomment the following line to download the SDO AIA data locally
# aia_files = Fido.fetch(query_aia)

# ------------------------------
# Query 2: SoHO SUMER microflare observation on 2011 November 8
# ------------------------------
# Define the time range for the observation (14:52 to 18:02 UT)
start_time_sumer = '2011-11-08T14:52:00'
end_time_sumer   = '2011-11-08T18:02:00'

# Construct the query for SoHO SUMER using the instrument "SUMER" from source "SOHO".
query_sumer = Fido.search(
    a.Time(start_time_sumer, end_time_sumer),
    a.Instrument('SUMER'),
    a.Source('SOHO')
)

# Print the query summary for SoHO SUMER
print("\nQuery Result for SoHO SUMER microflare observation (2011-11-08 14:52-18:02 UT):")
print(query_sumer)

# Uncomment the following line to download the SoHO SUMER data locally
# sumer_files = Fido.fetch(query_sumer)

if __name__ == '__main__':
    print("\nData queries have been executed. Review the printed query results above for details.")
