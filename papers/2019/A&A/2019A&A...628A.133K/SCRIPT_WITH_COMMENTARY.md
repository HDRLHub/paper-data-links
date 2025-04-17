# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for SoHO/SUMER data.
The query uses the time range and instrument details extracted from the context and
the provided VSO interface information.
- Time Range: 1996-01-22 to 2017-04-04
- Instrument: SUMER (with SoHO as the source)
The script prints the query result summary. The Fido.fetch command is provided in comments,
and can be uncommented to download the data.
"""

from sunpy.net import Fido, attrs as a

# Define the observation time range based on the VSO interface information.
time_start = "1996-01-22"
time_end = "2017-04-04"

# Construct the query for SoHO/SUMER data using the SunPy VSO client.
# The query uses:
#   - The provided time range.
#   - Source 'SOHO' and Instrument 'SUMER', as these are the fixed values in the context.
query_result = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("SUMER")
)

# Print the summary of the query results.
print("Query Results:")
print(query_result)

# Uncomment the next lines to download the data after verifying the query results.
# downloaded_files = Fido.fetch(query_result)
# print("Downloaded files:")
# print(downloaded_files)

if __name__ == "__main__":
    # The script is being executed as the main module.
    print("VSO query for SoHO/SUMER data completed.")
