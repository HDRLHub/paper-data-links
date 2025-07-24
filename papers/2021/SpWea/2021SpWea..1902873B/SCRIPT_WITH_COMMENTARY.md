# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query STEREO-A SECCHI data,
specifically for the HI1 and HI2 detectors. In the context of our study,
we focus on CME observations from 2010 to 2020 as described in the paper.
The VSO interface confirms that data from STEREO_A with instrument "SECCHI"
and detectors "HI1" and "HI2" are available from 2006/11/06 to present.
We limit our search to the observation period 2010-01-01 to 2020-12-31.
"""

import sunpy.net.attrs as a
from sunpy.net import Fido

# Define the time range for the query as per the context (CME events observed between 2010 and 2020)
time_start = "2010-01-01"
time_end = "2020-12-31"

# Query 1: STEREO-A SECCHI/HI1 data 
# HI1 is used for high- and lower-quality white-light imaging of CME fronts.
query_hi1 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("HI1")
)

print("Query Result for STEREO-A SECCHI/HI1:")
print(query_hi1)

# Uncomment the following line to download the HI1 data (do not run fetch commands as per instructions)
# hi1_files = Fido.fetch(query_hi1)

# Query 2: STEREO-A SECCHI/HI2 data
# HI2 extends the field of view to larger elongations to track CME evolution farther from the Sun.
query_hi2 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("HI2")
)

print("Query Result for STEREO-A SECCHI/HI2:")
print(query_hi2)

# Uncomment the following line to download the HI2 data (do not run fetch commands as per instructions)
# hi2_files = Fido.fetch(query_hi2)

if __name__ == "__main__":
    print("SunPy VSO query script executed. Review the printed query results above.")
