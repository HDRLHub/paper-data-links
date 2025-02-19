# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses sunpy’s VSO client to query SOHO/LASCO white‐light coronagraph data.
According to the study context, LASCO data are used for CME analysis and the relevant
observational periods are:
   1. Solar Cycle 23 (August 1996 – December 2008) – primarily using LASCO C2 and C3.
   2. Solar Cycle 24 (January 2009 – December 2016) – again using LASCO C2 and C3.
We query separately for both detectors since after the loss of C1 (post-1998) the analysis
relies on C2 and C3. The queries below are constructed with the required time ranges and the
instrument details derived from the provided VSO interface.
"""

from sunpy.net import Fido, attrs as a

# ---------------------------
# Query for Solar Cycle 23: August 1996 – December 2008
# ---------------------------

# Query LASCO C2 data
query_cycle23_C2 = Fido.search(
    a.Time("1996-08-01", "2008-12-31"),  # Solar Cycle 23 time range
    a.Source("SOHO"),                   # Source from VSO interface
    a.Instrument("LASCO"),              # LASCO coronagraph instrument
    a.Detector("C2")                    # Use detector C2 (C1 not used after 1998)
)
print("Solar Cycle 23 - LASCO C2 query result:")
print(query_cycle23_C2)

# Query LASCO C3 data
query_cycle23_C3 = Fido.search(
    a.Time("1996-08-01", "2008-12-31"),  # Solar Cycle 23 time range
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")                    # Use detector C3 as well
)
print("\nSolar Cycle 23 - LASCO C3 query result:")
print(query_cycle23_C3)

# ---------------------------
# Query for Solar Cycle 24: January 2009 – December 2016
# ---------------------------

# Query LASCO C2 data for Cycle 24
query_cycle24_C2 = Fido.search(
    a.Time("2009-01-01", "2016-12-31"),  # Solar Cycle 24 time range (analysis period)
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nSolar Cycle 24 - LASCO C2 query result:")
print(query_cycle24_C2)

# Query LASCO C3 data for Cycle 24
query_cycle24_C3 = Fido.search(
    a.Time("2009-01-01", "2016-12-31"),  # Solar Cycle 24 time range (analysis period)
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("\nSolar Cycle 24 - LASCO C3 query result:")
print(query_cycle24_C3)

# ---------------------------
# Fetching Data (Commented Out)
# ---------------------------
# The following commands would download the data based on the queries above.
# Uncomment them to perform the data download.
#
# from sunpy.net import Fido
#
# data_cycle23_C2 = Fido.fetch(query_cycle23_C2)
# data_cycle23_C3 = Fido.fetch(query_cycle23_C3)
# data_cycle24_C2 = Fido.fetch(query_cycle24_C2)
# data_cycle24_C3 = Fido.fetch(query_cycle24_C3)

if __name__ == "__main__":
    print("\nVSO queries constructed successfully. Review the printed query details before downloading data.")
