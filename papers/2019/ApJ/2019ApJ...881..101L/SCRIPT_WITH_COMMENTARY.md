# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client (via the Fido interface) to query for SDO/HMI data.
Based on the context of the paper, we are interested in definitive SDO/HMI data used
for forecast training, which covers the time range 2010-05-01 to 2015-12-31.

Note:
- We query the Virtual Solar Observatory for SDO/HMI data.
- Only the time range and instrument are required parameters.
- The query selects data from SDO with the HMI instrument.
- The Fido.fetch() line is provided as a comment in case downloading is desired.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the start and end times for the definitive SDO/HMI data period used in forecasting.
start_time = '2010-05-01'
end_time = '2015-12-31'

# Set up the query attributes: time range, instrument ('HMI'), and source ('SDO').
time_attr = a.Time(start_time, end_time)
instrument_attr = a.Instrument('HMI')
source_attr = a.Source('SDO')

# Construct the query using Fido.search.
# This searches for data that matches the provided time range and instrument.
query_result = Fido.search(time_attr, instrument_attr, source_attr)

# Print out the query summary results.
print("Query Results for SDO/HMI definitive data (2010-05-01 to 2015-12-31):")
print(query_result)

# Uncomment the following line to download the data corresponding to the query result.
# files = Fido.fetch(query_result)
    
if __name__ == '__main__':
    pass
