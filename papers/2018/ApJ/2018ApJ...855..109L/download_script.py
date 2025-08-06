# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Script to query SOHO/LASCO C2 white-light coronagraph data
for the period 1996-01-01 to 2015-12-31 using Sunpy's VSO client.
"""

import sunpy.net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the observation time range based on the context (1996–2015)
start_time = "1996-01-01 00:00"
end_time   = "2015-12-31 23:59"

# Build individual query attributes for clarity and explicitness
time_range     = a.Time(start_time, end_time)
source         = a.Source('SOHO')
instrument     = a.Instrument('LASCO')
detector       = a.Detector('C2')
physobs        = a.Physobs('intensity')

# Execute the VSO search for SOHO LASCO C2 intensity data
results = Fido.search(time_range, source, instrument, detector, physobs)

# Print the search results summary to the console
print("Search results for SOHO/LASCO C2 from 1996-01-01 to 2015-12-31:")
print(results)

# To fetch and download the data products, uncomment the following line:
# downloaded_files = Fido.fetch(results)

if __name__ == "__main__":
    # The script can be run directly. All operations already performed above.
    pass
