# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs a VSO query using Sunpy to retrieve LASCO data from the SOHO spacecraft.
Based on the context, we are interested in data from February 2, 1999 at 16:35 UT to 
December 31, 2018 at 09:48 UT. We choose the LASCO instrument with the C2 detector 
since its available time range ("1995/12/08 - present") covers our desired window.

Note: The actual download step with Fido.fetch is commented out.
"""

from datetime import datetime
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the start and end times based on the context for LASCO data.
start_time = '1999-02-02T16:35'
end_time   = '2018-12-31T09:48'

# Construct the query using the time range and instrument details.
# Here, we are querying for data from SOHO / LASCO with the C2 detector.
query = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print the query results.
print("Query Result for LASCO (C2) data from SOHO for the time period:")
print("Start Time:", start_time)
print("End Time:", end_time)
print(query)

# Uncomment the following lines to fetch the data files.
# fetched_files = Fido.fetch(query)
# print("Fetched files:", fetched_files)
