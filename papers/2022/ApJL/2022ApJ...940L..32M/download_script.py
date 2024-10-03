# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Context: We want to construct queries to download data from the SOHO LASCO instrument
# for the observation of a coronal mass ejection (CME) event on October 9, 2021.

# Reasoning:
# 1. We need to query the SOHO LASCO instrument data for the specified date.
# 2. The LASCO instrument has two detectors: C2 and C3.
# 3. We will query data for both C2 and C3 detectors within the specified time range.

# Define the time range for the CME observation
time_range = TimeRange('2021-10-09 00:00', '2021-10-09 23:59')

# Define the instrument and detectors
instrument = 'LASCO'
detectors = ['C2', 'C3']

# Construct the query for SOHO LASCO C2 data
query_c2 = Fido.search(
    a.Time(time_range.start, time_range.end),
    a.Instrument(instrument),
    a.Detector(detectors[0])
)

# Print the query results for LASCO C2
print("Query results for SOHO LASCO C2:")
print(query_c2)

# Construct the query for SOHO LASCO C3 data
query_c3 = Fido.search(
    a.Time(time_range.start, time_range.end),
    a.Instrument(instrument),
    a.Detector(detectors[1])
)

# Print the query results for LASCO C3
print("Query results for SOHO LASCO C3:")
print(query_c3)

# Uncomment the following lines to fetch the data
# files_c2 = Fido.fetch(query_c2)
# files_c3 = Fido.fetch(query_c3)
