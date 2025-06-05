# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query LASCO data through the SunPy VSO interface.
Based on the study description, we are interested in SOHO/LASCO data corresponding 
to the observation of coronal mass ejections (CMEs) detected on June 13, 2014. 
According to the paper, the LASCO instrument (a space-based optical coronagraph) 
was used for detecting CME timing (with events at ~07:36 UT, ~08:24 UT, and ~12:24 UT).
For this query we use the LASCO instrument on board SOHO with the detector “C2”
since its full observational time range ("1995/12/08 - present") covers the 2014 date.
The query will request data covering the full day of June 13, 2014.
"""

from sunpy.net import Fido, attrs as a

# Define the time range for June 13, 2014.
start_time = '2014-06-13T00:00:00'
end_time = '2014-06-13T23:59:59'

# Build the query.
# Note: We choose the LASCO instrument with detector 'C2' as it is available for this period.
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)

# Print out the query result details.
print("Query Result:")
print(query_result)

# If you wish to download the data, uncomment the following line:
# downloaded_files = Fido.fetch(query_result)
# print("Download complete. Files:")
# print(downloaded_files)
