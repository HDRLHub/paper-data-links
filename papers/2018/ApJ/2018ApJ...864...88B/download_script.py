# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query white-light coronagraph data from the LASCO instrument on board SOHO.
Based on the Scientific Observation Instrumentation Form, we are interested in imaging data of halo CMEs.
Since the paper discusses observations related to LASCO, we query data from the LASCO C2 detector,
which has an available full time range from 1995/12/08 to present.
For this example, we select a one-hour time window around the January 23, 2012 CME event (starting at 4:00 UT).
"""

from sunpy.net import Fido, attrs as a
from datetime import datetime

# Define the time range for the event: January 23, 2012 from 04:00 UT to 05:00 UT.
start_time = "2012-01-23 04:00:00"
end_time = "2012-01-23 05:00:00"

# Construct a search query for LASCO white-light coronagraph data.
# We use the following parameters:
#   Source: SOHO
#   Instrument: LASCO
#   Detector: C2 (chosen based on the available instrument configuration in the VSO interface)
#   Physical Observable: intensity (white-light imaging)
# The query is limited in time to the defined event window.
query = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Physobs("intensity")
)

# Print the query results (this shows what VSO would return based on the query parameters)
print("Query Results:")
print(query)

# Uncomment the following lines to perform the data download.
# Make sure you have a proper setup and network connectivity.
#
# print("Fetching the data...")
# downloaded_files = Fido.fetch(query)
# print("Downloaded files:")
# print(downloaded_files)

if __name__ == '__main__':
    # Main execution to ensure the script runs directly.
    print("SunPy VSO query script executed successfully.")
