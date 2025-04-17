# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for SOHO/LASCO white‐light coronagraph data.
Since the paper uses CME height–time observations from SOHO/LASCO during the ascending phase of Solar Cycle 24,
we query the data for the time range 2009-01-01 to 2013-12-31.
Note: The available VSO entries show three detectors (C1, C2, C3) for LASCO.
Since LASCO/C1 only covers 1995/12/08 - 2000/08/09 (outside our period), 
this script focuses on LASCO/C2 and LASCO/C3 which are available “1995/12/08 - present”.
"""

from sunpy.net import Fido, attrs as a

# Define the time range based on the study period (Solar Cycle 24 ascending phase)
start_time = "2009-01-01"
end_time = "2013-12-31"

# Query LASCO/C2 data from SOHO
query_c2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("Query results for SOHO/LASCO C2:")
print(query_c2)

# Uncomment the following line to download the data for LASCO/C2 (disabled by default)
# files_c2 = Fido.fetch(query_c2)

# Query LASCO/C3 data from SOHO
query_c3 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("\nQuery results for SOHO/LASCO C3:")
print(query_c3)

# Uncomment the following line to download the data for LASCO/C3 (disabled by default)
# files_c3 = Fido.fetch(query_c3)

if __name__ == "__main__":
    # The script only queries and prints the available data search results without downloading.
    pass
