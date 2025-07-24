# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query
UVCS/SOHO data from the Virtual Solar Observatory.

Context Recap:
--------------
The context mentions several instruments; however, only data for
UVCS on board SOHO is available in the provided VSO interface.
UVCS observations in this context are used as an independent benchmark
for Doppler‐dimming wind‑speed measurements. The available time range
for UVCS data is from 1996/01/20 to present.
Since the context does not provide a specific time range for UVCS,
we choose a representative interval for demonstration.

Script Overview:
----------------
1. Import the necessary SunPy modules.
2. Define the time range (ensuring it is within the available range).
3. Query for data from the instrument "UVCS" with a given time interval.
4. Print the search results.
5. Provide a commented out Fido.fetch call for actual data download.
"""

# Import required modules from sunpy
from sunpy.net import Fido, attrs as a

# Define the time interval for the query - chosen to be within UVCS's available full range.
# Here we use a one-day interval starting from 1996-01-20.
start_time = '1996-01-20'
end_time = '1996-01-21'

# Create a query for SOHO/UVCS data. The only required parameters are the time range and instrument.
# Note: Other detector types (e.g., LVA, OVI, VLD) are available but as the context provides no
# specific detector preference, we query for the instrument UVCS as a whole.
query = Fido.search(a.Time(start_time, end_time), a.Instrument("UVCS"), a.Source("SOHO"))

# Print the query results
print("Query Results for SOHO/UVCS data from", start_time, "to", end_time)
print(query)

# Uncomment the following lines to download the data (disabled by instruction)
# download_files = Fido.fetch(query)
# print("Data downloaded. Files:", download_files)

if __name__ == '__main__':
    # Execute the query when running the script directly
    print("Script executed: Querying for SOHO/UVCS data...")
    # Note: The query has been already executed above.
    pass
