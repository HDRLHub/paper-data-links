# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use SunPy's VSO interface to query in situ data from the WIND spacecraft.
Based on the context provided, the WIND instrument has been used over a 15-year period at 1 AU
to study CME properties. Since the paper does not specify exact dates, we choose an example time range
covering 15 years. Adjust the dates as necessary.

Note: The Fido.fetch command is provided as a commented-out line.
"""

# Import necessary packages from SunPy
from sunpy.net import Fido, attrs as a

# Define the time range for the WIND in situ data query.
# Here we assume a 15-year duration from 2000-01-01 to 2015-01-01 as an example period.
start_time = "2000-01-01"
end_time = "2015-01-01"

# Define a simple query for the WIND instrument in the VSO.
# The only required values here are the time range and the instrument.
# Note that the VSO interface provided does not list available instruments, but since WIND is commonly available,
# we assume it is valid for this query.
query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("wind")
)

# Print out the query results to review available data.
print("Query Results:")
print(query)

# To fetch the data, uncomment the following line:
# downloaded_files = Fido.fetch(query)
