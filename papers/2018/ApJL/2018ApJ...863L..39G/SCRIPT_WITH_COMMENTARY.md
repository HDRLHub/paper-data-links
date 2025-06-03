# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client to query SDO/AIA data corresponding to the flare onset
observations described in the paper. The query is for SDO/AIA observations around the time
of the 2017 September 10 event where the flare onset occurred shortly after 15:40 UT.
We have chosen a query time interval from 2017-09-10 15:40:00 to 2017-09-10 16:20:00.
The script constructs the query and prints out the search results.
(Note: The fetch function is provided as a commented-out example.)
"""

import datetime
from sunpy.net import Fido, attrs as a

# Define the start and end times based on the context for the flare onset.
start_time = datetime.datetime(2017, 9, 10, 15, 40, 0)
end_time = datetime.datetime(2017, 9, 10, 16, 20, 0)

# Construct the query for SDO/AIA data.
# According to our VSO interface, SDO/AIA is available with intensity observations in multiple EUV channels.
# We will rely on the default wavelengths for AIA since the context implies the use of multi-channel EUV movies.
# Here, we explicitly set the source as 'SDO' and the instrument as 'AIA'.
query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("AIA"),
    a.Source("SDO")
)

# Print out the query result summary.
print("Query Results for SDO/AIA data during the flare onset on 2017-09-10:")
print(query)

# Uncomment the following lines to actually download the data.
# Note: The fetch command is commented out as per the directive.

# download_files = Fido.fetch(query)
# print("Downloaded Files:")
# print(download_files)

if __name__ == '__main__':
    pass
