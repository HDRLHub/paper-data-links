# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query SOHO/LASCO C2 data.
According to the paper's context, the LASCO C2 observation is used to track the CME 
appearing at 07:31 UT on March 21, 1998.
The query uses the time range centered around that observation and targets the SOHO source,
LASCO instrument, with the "C2" detector.
Note: The Fido.fetch command is commented out as per instructions.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the CME observation from LASCO C2.
start_time = '1998-03-21T07:31:00'
end_time = '1998-03-21T08:00:00'  # A ~30 minute window to capture the CME event

# Build the query for SOHO/LASCO C2.
query = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)

# Print out the query results.
print("Query results for SOHO/LASCO C2 data:")
print(query)

# The following line fetches the data.
# It is commented out to avoid running the actual download.
# downloaded_files = Fido.fetch(query)

if __name__ == '__main__':
    pass
