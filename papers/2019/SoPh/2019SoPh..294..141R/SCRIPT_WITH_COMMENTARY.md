# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query LASCO data from SOHO.
In the context of the paper, LASCO imaging data (used to examine CME properties
associated with solar energetic particle events) are of interest.
The available VSO interface information confirms that LASCO data (with detectors
C1, C2, and C3) are available from SOHO, with data available from 1995/12/08 to present.
Here we choose to query data from LASCO using a time range corresponding to one of the
events discussed in the paper (e.g. an event around 13 September 2005).
The query selects data from the SOHO/LASCO instrument.
"""

# Import necessary modules from SunPy and its VSO client
from sunpy.net import Fido, attrs as a

# Define the time range for the query.
# We choose 13 September 2005 as an example event date.
time_range = a.Time("2005-09-13T00:00:00", "2005-09-13T23:59:59")

# Define the instrument and source as per VSO interface details for LASCO.
instrument = a.Instrument("LASCO")
source = a.Source("SOHO")

# Construct the query using Fido without any nested calls or loops.
query_result = Fido.search(time_range, instrument, source)

# Print out the query results.
print("VSO Query Results for SOHO/LASCO on 2005-09-13:")
print(query_result)

# Uncomment the following line to download the data once you have verified the query results.
# downloaded_files = Fido.fetch(query_result)

if __name__ == "__main__":
    # This block can be used for additional processing if needed.
    pass
