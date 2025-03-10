# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs a Sunpy VSO query to obtain SOHO/MDI helioseismic data.
Based on the provided context, we are interested in MDI observations used
for helioseismic frequency studies. The vso_interface available information
indicates that MDI data with observable "LOS_velocity" is available starting
from 1996/03/03 up to 2011/04/12. We use this time range for our query.

Note:
- We only use the required values: the time range and instrument.
- The Fido.fetch command is commented out as per instructions.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the start and end times based on available MDI data for helioseismic observations.
start_time = "1996/03/03"
end_time = "2011/04/12"

# Build the VSO query using the time range and specifying the MDI instrument.
# The query is kept explicit without any nested calls or loops.
query_time = a.Time(start_time, end_time)
query_instrument = a.Instrument("MDI")
query_source = a.Source("SOHO")
query_physobs = a.Physobs("LOS_velocity")  # selecting the LOS_velocity observable for MDI

# Construct the full query.
query_result = Fido.search(query_time, query_source, query_instrument, query_physobs)

# Print out the query result to inspect the matched data.
print("Query Result:")
print(query_result)

# If you want to download the data, uncomment the following lines.
# downloaded_files = Fido.fetch(query_result, progress=True)
# print("Downloaded Files:")
# print(downloaded_files)

if __name__ == "__main__":
    pass
