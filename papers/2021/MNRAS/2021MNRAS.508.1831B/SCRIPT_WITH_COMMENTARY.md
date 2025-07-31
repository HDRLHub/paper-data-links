# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the Virtual Solar Observatory (VSO) using SunPy.
Based on the provided context, we focus on SDO observations of Active Region 11150.
The VSO interface only offers SDO instruments, so we construct queries for:
  1. AIA, which provides high-cadence EUV imaging (e.g., 171 Å, 193 Å, 211 Å, 94 Å)
     over the period when AR 11150 was observed (27 January 2011 – 10 February 2011).
  2. HMI, which provides line-of-sight magnetograms. Here we query a magnetogram
     taken on 29 January 2011 at 12:00 UT.
Note: Hinode/EIS is mentioned in the context but is not available in the provided VSO interface.
The Fido.fetch commands are commented out to avoid automatic downloads.
"""

from sunpy.net import Fido, attrs as a

# -----------------------------
# Query 1: AIA EUV Imaging Data
# -----------------------------
# Define the time range for AR 11150 observations with AIA:
# "27 January 2011 – 10 February 2011" as mentioned in the context.
aia_time_start = "2011-01-27"
aia_time_end = "2011-02-10"

# Construct the query for SDO/AIA. The query uses time and instrument attributes.
# The available wavelengths in the VSO interface for AIA include channels like 171, 211, and 94 Å.
# For this example, we leave the wavelength specification open because the context requires a broad range.
query_aia = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Instrument("AIA")
)

# Print the query results for AIA
print("Query results for SDO/AIA data (27 Jan 2011 – 10 Feb 2011):")
print(query_aia)

# Uncomment the following line to fetch the data
# downloaded_aia_files = Fido.fetch(query_aia)

# -----------------------------
# Query 2: HMI Magnetogram Data
# -----------------------------
# Define the time range for the HMI magnetogram.
# The context specifies a key observation on "29 January 2011 at 12:00 UT".
hmi_time = "2011-01-29T12:00"

# Construct the query for SDO/HMI using a single timestamp.
query_hmi = Fido.search(
    a.Time(hmi_time, hmi_time),
    a.Instrument("HMI")
)

# Print the query results for HMI
print("\nQuery results for SDO/HMI magnetogram data (29 Jan 2011 at 12:00 UT):")
print(query_hmi)

# Uncomment the following line to fetch the data
# downloaded_hmi_files = Fido.fetch(query_hmi)

if __name__ == "__main__":
    print("\nVSO queries executed. Review the printed query results for details.")
