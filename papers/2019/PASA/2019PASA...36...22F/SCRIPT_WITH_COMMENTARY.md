# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client to query solar data from the Virtual Solar Observatory.
It builds queries for data used in the study:
  1. SDO/HMI line-of-sight magnetograms on 2013-09-29 and 2016-01-26.
  2. SOHO/LASCO C2 coronagraph data on 2013-09-29 to capture CME observations.
  3. (Optionally) SDO/AIA EUV images on 2013-09-29 (acknowledged in the paper).

Note:
  - Only time range and instrument attributes are specified as required.
  - The Fido.fetch commands are commented out to avoid automatic downloads.
"""

# Import necessary modules from SunPy
import sunpy.net.vso as vso
from sunpy.net import attrs as a

# Create a VSO client instance
client = vso.VSOClient()

# ---------------------------------------------------------------------------
# Query 1: SDO/HMI magnetogram on 2013-09-29 (capturing the pre-eruptive magnetic field)
# Time chosen around the reported HMI observation near 20:17 UT.
# ---------------------------------------------------------------------------
time_start_2013 = "2013-09-29T20:17:00"
time_end_2013   = "2013-09-29T20:20:00"
query_hmi_2013 = client.search(
    a.Time(time_start_2013, time_end_2013),
    a.Instrument("HMI"),
    a.Source("SDO")
)
print("Query results for SDO/HMI on 2013-09-29 (line-of-sight magnetogram):")
print(query_hmi_2013)

# Uncomment the following line to download the data:
# hmi_data_2013 = client.fetch(query_hmi_2013)

# ---------------------------------------------------------------------------
# Query 2: SDO/HMI magnetogram on 2016-01-26 (capturing the pre-eruptive state before filament eruption F2)
# Time chosen around 11:34 UT as indicated in the paper.
# ---------------------------------------------------------------------------
time_start_2016 = "2016-01-26T11:30:00"
time_end_2016   = "2016-01-26T11:40:00"
query_hmi_2016 = client.search(
    a.Time(time_start_2016, time_end_2016),
    a.Instrument("HMI"),
    a.Source("SDO")
)
print("\nQuery results for SDO/HMI on 2016-01-26 (line-of-sight magnetogram):")
print(query_hmi_2016)

# Uncomment the following line to download the data:
# hmi_data_2016 = client.fetch(query_hmi_2016)

# ---------------------------------------------------------------------------
# Query 3: SOHO/LASCO C2 coronagraph data on 2013-09-29 (capturing the CME appearance)
# Time chosen around 22:12 UT as the CME was first recorded above 20 R⊙.
# ---------------------------------------------------------------------------
time_start_lasco = "2013-09-29T22:10:00"
time_end_lasco   = "2013-09-29T22:15:00"
query_lasco = client.search(
    a.Time(time_start_lasco, time_end_lasco),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Source("SOHO")
)
print("\nQuery results for SOHO/LASCO C2 on 2013-09-29:")
print(query_lasco)

# Uncomment the following line to download the data:
# lasco_data = client.fetch(query_lasco)

# ---------------------------------------------------------------------------
# Optional Query: SDO/AIA imaging on 2013-09-29
# Although not detailed in the paper, SDO/AIA data are acknowledged.
# This query is provided for completeness.
# ---------------------------------------------------------------------------
time_start_aia = "2013-09-29T20:00:00"
time_end_aia   = "2013-09-29T20:20:00"
query_aia = client.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument("AIA"),
    a.Source("SDO")
)
print("\nQuery results for SDO/AIA on 2013-09-29 (optional):")
print(query_aia)

# Uncomment the following line to download the data:
# aia_data = client.fetch(query_aia)

if __name__ == "__main__":
    # This main block is here to ensure the script can be executed directly.
    # Running the script will perform the queries and print out the results.
    pass
