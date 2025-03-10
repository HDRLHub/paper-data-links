# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface (via Fido) to query solar observational data.
We perform two separate queries based on the context:

1. SOHO Coronagraph Data for the 2017 July event:
   - Time Range: Around 2017-07-23T05:09 UT (we use a 20‐minute window from 05:00 to 05:20 UT).
   - Instrument: SOHO (typically provides coronagraph imagery in white light).

2. STEREO A Remote-Sensing Data for the 2012 July event:
   - Time Range: From approximately 2012-07-23T02:20:00 (eruption onset) to 2012-07-23T20:55:00 (shock arrival).
   - Instrument: STEREO A.

Note: This script queries the VSO but the actual data fetching (Fido.fetch) is commented out.
"""

# Import necessary modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import sunpy
import astropy.units as u

# ---------------------------
# Query 1: SOHO Coronagraph Data on 2017 July 23
# ---------------------------
# Define the start and end times for SOHO data query.
soho_start_time = "2017-07-23T05:00:00"
soho_end_time   = "2017-07-23T05:20:00"

# Print a message indicating the current query.
print("Querying SOHO coronagraph data for the 2017 July event:")
# Build and run the query with required time and instrument attributes.
soho_query = Fido.search(a.Time(soho_start_time, soho_end_time),
                           a.Instrument("soho"))
# Print out the query results.
print(soho_query)

# Uncomment the following line to fetch the data once satisfied with the query:
# soho_files = Fido.fetch(soho_query)

# ---------------------------
# Query 2: STEREO A Remote-Sensing Data on 2012 July 23
# ---------------------------
# Define the time window covering remote-sensing and in situ observations.
stereo_a_start_time = "2012-07-23T02:20:00"
stereo_a_end_time   = "2012-07-23T20:55:00"

print("\nQuerying STEREO A data for the 2012 July event:")
# Build and run the query with required time and instrument attributes.
stereo_a_query = Fido.search(a.Time(stereo_a_start_time, stereo_a_end_time),
                             a.Instrument("stereo_a"))
# Print out the query results.
print(stereo_a_query)

# Uncomment the following line to fetch the data once satisfied with the query:
# stereo_a_files = Fido.fetch(stereo_a_query)

# End of the script.
if __name__ == "__main__":
    print("\nQueries completed. Review the query results above.")
