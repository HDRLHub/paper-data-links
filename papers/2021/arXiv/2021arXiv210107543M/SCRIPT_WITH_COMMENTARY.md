# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query RHESSI data.
The provided VSO interface shows that only RHESSI data are available.
We construct two queries corresponding to the two RHESSI observation periods mentioned in the context:
    1. Pre-eclipse imaging (an image produced at 11:01:20 UT)
    2. Post-eclipse imaging (an image produced at 11:37:32 UT)
We assume the event date is 2017-09-09 based on the GOES context.
Only the time range and instrument are used in the search.
Note: The Fido.fetch calls are commented out as per instructions.
"""

# Import required modules from sunpy
from sunpy.net import Fido, attrs as a

# Define the event date
event_date = "2017-09-09"

# Define the time range for RHESSI pre-eclipse imaging
# The image was produced at 11:01:20 UT.
# We query a small interval (1 second) around this time.
pre_eclipse_start = f"{event_date} 11:01:20"
pre_eclipse_end   = f"{event_date} 11:01:21"

# Define the time range for RHESSI post-eclipse imaging
# The image was produced at 11:37:32 UT.
# We query a small interval (1 second) around this time.
post_eclipse_start = f"{event_date} 11:37:32"
post_eclipse_end   = f"{event_date} 11:37:33"

# Define the instrument attribute for RHESSI based on the provided VSO interface.
instrument_attr = a.Instrument("RHESSI")

# Query 1: Pre-eclipse RHESSI imaging data
print("Querying RHESSI pre-eclipse imaging data (around 11:01:20 UT)...")
pre_eclipse_query = Fido.search(a.Time(pre_eclipse_start, pre_eclipse_end), instrument_attr)
print(pre_eclipse_query)
# Uncomment the next line to fetch data for pre-eclipse imaging
# pre_eclipse_files = Fido.fetch(pre_eclipse_query)

# Query 2: Post-eclipse RHESSI imaging data
print("\nQuerying RHESSI post-eclipse imaging data (around 11:37:32 UT)...")
post_eclipse_query = Fido.search(a.Time(post_eclipse_start, post_eclipse_end), instrument_attr)
print(post_eclipse_query)
# Uncomment the next line to fetch data for post-eclipse imaging
# post_eclipse_files = Fido.fetch(post_eclipse_query)

print("\nQueries completed. Inspect the printed search results for details on the available data.")
 
if __name__ == "__main__":
    pass
