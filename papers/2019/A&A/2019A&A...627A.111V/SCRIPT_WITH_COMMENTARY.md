# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries SOHO/LASCO C2 coronagraph data from the Virtual Solar Observatory (VSO)
for the period of 2015-06-17 to 2015-06-29. These data correspond to the CME observations used
in the study as described in the context.
Note:
- The VSO interface provides LASCO data for detectors C1, C2, and C3.
- For the 2015 event period, LASCO C1 data are not available (its time range ends in 2000),
  so we select LASCO C2 (which is available from 1995-12-08 to the present).

This script uses SunPy's VSO client for querying.
"""

# Import necessary modules from sunpy.net
from sunpy.net import Fido, attrs as a

# Define the start and end times for the query (as per the context for the CME observation period)
start_time = "2015-06-17"
end_time = "2015-06-29"

# Define the query attributes
# We specify the source as SOHO, instrument as LASCO, and choose detector C2.
time_attr = a.Time(start_time, end_time)
source_attr = a.Source("SOHO")
instrument_attr = a.Instrument("LASCO")
detector_attr = a.Detector("C2")

# Compose the full query using the defined attributes
query_result = Fido.search(time_attr, source_attr, instrument_attr, detector_attr)

# Print the query result details
print("Query Results for SOHO/LASCO C2 data from", start_time, "to", end_time)
print(query_result)

# Uncomment the following line to fetch the data once you have verified the query results.
# downloaded_files = Fido.fetch(query_result)
