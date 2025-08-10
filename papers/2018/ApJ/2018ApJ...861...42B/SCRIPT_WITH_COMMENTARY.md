# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3

"""
This script queries the SunPy VSO client for SDO/EVE data.
The query is based on the scientific context of studying the cyclic variation 
of the solar coronal Ne/O abundance ratio using full disk integrated EUV spectra.
The primary data are obtained from the EVE instrument onboard SDO.
We focus on measurements from the MEGS-A and MEGS-B detectors covering the wavelength 
ranges approximately from 50–370 Å (MEGS-A) and 350–1050 Å (MEGS-B), as described in the paper.
The observations are collected from April 2010 to May 2014.
Note: In the VSO interface provided, the SDO/EVE entry with detectors “MEGS-A, MEGS-B”
covers the wavelength range 60.0–1060.0 Å, which we use in this query.
"""

from sunpy.net import Fido, attrs as a

# Define the time range for the query (April 2010 to May 2014)
start_time = "2010-04-30"
end_time = "2014-05-01"

# Build the query using the VSO attributes:
# - Time: from start_time to end_time
# - Source: SDO
# - Instrument: EVE
# - Detector: MEGS-A, MEGS-B (as indicated in the VSO interface for full disk irradiance)
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SDO"),
    a.Instrument("EVE"),
    a.Detector("MEGS-A, MEGS-B")
)

# Print out the query results returned by Fido. 
print("VSO Query Results:")
print(query_result)

# Uncomment the two lines below to fetch the data if required.
# fetched_files = Fido.fetch(query_result)
# print("Downloaded files:")
# print(fetched_files)

if __name__ == "__main__":
    pass
