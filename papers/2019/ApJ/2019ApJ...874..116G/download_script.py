# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query data from the SDO/HMI instrument using SunPy's VSO Fido interface.
We use a time range of 2010-04-01 to 2018-07-31. This roughly corresponds to the time interval used in the
study for high-resolution HMI synoptic maps (≈2010.4–2018.7). The query employs only the essential
attributes: time and instrument (with SDO as the source), as specified by the available VSO interface.
"""

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the query
start_time = '2010-04-01'
end_time = '2018-07-31'

# Query the Virtual Solar Observatory (VSO) data archive for SDO/HMI data.
# The query uses:
# - a.Time to specify the period of interest.
# - a.Instrument to select 'HMI'.
# - a.Source to ensure we retrieve data from 'SDO'.
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SDO'),
    a.Instrument('HMI')
)

# Print the query result to check the discovered datasets
print("Query Result:")
print(query_result)

# To actually download the queried data, uncomment the following line:
# downloaded_files = Fido.fetch(query_result)

if __name__ == "__main__":
    print("SDO/HMI query completed. Review the printed query result for available observations.")
