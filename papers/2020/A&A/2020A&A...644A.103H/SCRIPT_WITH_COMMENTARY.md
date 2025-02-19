# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query SOHO/MDI data for the LOS_velocity observable.
The time range is chosen according to the available MDI data from 1996-03-03 to 2011-04-12,
which aligns with the observational context discussed in the paper regarding long-lived velocity features.
"""

# Import required modules from SunPy
from sunpy.net import Fido, attrs as a

# Define the time range based on the available full time range for SOHO MDI LOS_velocity data.
start_time = "1996-03-03"
end_time = "2011-04-12"

# Construct the query with explicit attributes:
# 1. Time: Defined from start_time to end_time.
# 2. Instrument: "MDI".
# 3. Source: "SOHO".
# 4. Physical Observable (Physobs): "LOS_velocity".
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("MDI"),
    a.Source("SOHO"),
    a.Physobs("LOS_velocity")
)

# Print out the query results to inspect available data records.
print("Query Results:")
print(query_result)

# Uncomment the next two lines to download the data if needed.
# downloaded_files = Fido.fetch(query_result)
# print("Downloaded files:", downloaded_files)

if __name__ == "__main__":
    # The script will print the query result when executed.
    pass
