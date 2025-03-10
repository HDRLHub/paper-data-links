# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO module to query white-light coronagraph data from SOHO LASCO.
In our query we select data from the LASCO instrument with detector 'C2'.
The chosen time range (1995-12-08 to 2017-10-31) reflects the period used for CME studies 
in the referenced paper (catalogue of detected CMEs up to the end of October 2017).
The query is designed using the available VSO interface details.

Note:
- We do not actually fetch the data with Fido.fetch. The fetch command is provided but commented out.
- Only the required values (time range and instrument) are used in our query.
"""

import sunpy.net.vso as vso
from sunpy.net import attrs as a

# Define the time range and instrument details for the query.
start_time = "1995-12-08"
end_time   = "2017-10-31"

# Build the query using LASCO instrument and specifying the 'C2' detector.
# We choose detector 'C2' because its data from SOHO LASCO is available from
# 1995-12-08 to present and is appropriate for white-light coronagraph observations.
query_result = vso.Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print out the query results.
print(query_result)

# To actually download the data, you could use the following command:
# downloaded_files = vso.Fido.fetch(query_result)
# print(downloaded_files)

if __name__ == "__main__":
    # The script simply prints the query result.
    pass
