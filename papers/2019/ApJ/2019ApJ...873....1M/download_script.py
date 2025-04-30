# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to construct a query using SunPy's VSO interface
to download LASCO data from SOHO. The query specifically targets the LASCO instrument
using the C2 detector. According to the VSO interface details provided, the LASCO C2
data are available from 1995/12/08 to the present. For demonstration purposes,
a one-day time range is chosen within this available period.
"""

# Import necessary modules from sunpy.net
from sunpy.net import Fido, attrs as a

# Define the query parameters:
# Time: A one-day period in 2011, which falls within the available range for LASCO C2.
query_time = a.Time("2011-06-01", "2011-06-02")

# Source: SOHO
query_source = a.Source("SOHO")

# Instrument: LASCO
query_instrument = a.Instrument("LASCO")

# Detector: Using LASCO C2 as it is available from "1995/12/08 - present"
query_detector = a.Detector("C2")

# Build the query for LASCO data using the provided attributes.
result = Fido.search(query_time, query_source, query_instrument, query_detector)

# Print out the query results
print("Query Result:")
print(result)

# To download the data, you would typically use:
# files = Fido.fetch(result)
# However, the fetch command is commented out as per the instructions.
#
# Uncomment the following line to perform the data download:
# files = Fido.fetch(result)

if __name__ == "__main__":
    # The script is self-contained and can be executed directly.
    pass
