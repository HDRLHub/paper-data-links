# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query LASCO observations from the SOHO mission.
We use the LASCO instrument, which is available in the VSO interface for detectors C2 and C3 
(with available time ranges from 1995/12/08 to present). 

Here, we focus on a time period corresponding to the first event described in the paper,
when a CME was detected around 2003-11-03 between ~09:53 UT and ~10:06 UT.
For safety, we extend the time range slightly (from 09:30 UT to 10:30 UT) to capture the event.

Note: The Fido.fetch command is provided as a comment in case data downloading is desired.
"""

from sunpy.net import Fido, attrs as a

# Define the time range of interest for the CME event (first event: 2003 November 03).
# We extend the time window slightly to ensure full capture of the event.
time_query = a.Time('2003-11-03T09:30:00', '2003-11-03T10:30:00')

# Define the instrument used.
# According to the VSO interface, LASCO on board SOHO with detectors C2 and C3 are available.
instrument_query = a.Instrument('LASCO')

# Define the source of observations: SOHO.
source_query = a.Source('SOHO')

# Construct the query with the defined attributes.
query_result = Fido.search(time_query, source_query, instrument_query)

# Print out the query result summary.
print("Query Results:")
print(query_result)

# Uncomment the following line to fetch the data if required.
# downloaded_files = Fido.fetch(query_result)
# print("Data has been downloaded. Files:", downloaded_files)

if __name__ == "__main__":
    pass
