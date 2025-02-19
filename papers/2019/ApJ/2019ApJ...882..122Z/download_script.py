# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries SOHO/LASCO white‐light coronagraph data from the Virtual Solar Observatory (VSO)
for two specific CME events described in the paper:
    1. The November 4, 1997 CME observed with LASCO (primarily using C2 and C3 imagers)
    2. The June 6, 2000 CME observed with LASCO

The VSO interface provided indicates that the LASCO instrument (with detectors C2 and C3) is available
from 1995/12/08 until the present. The only required values for the query are the time range and the instrument.
We use SunPy's Fido to perform two explicit queries for these events. (Fido.fetch commands are provided but commented out.)
"""

# Import the necessary modules from SunPy
from sunpy.net import Fido, attrs as a

# -------------------------
# Query for Event 1: November 4, 1997 CME
# -------------------------
# Define the time range for the November 4, 1997 event.
# The paper notes that LASCO observations were used on this day (e.g., around 07:44:49 UT).
# Here we cover the full day to ensure all relevant images are included.
time_event1 = a.Time("1997-11-04T00:00:00", "1997-11-04T23:59:59")

# Specify the instrument: LASCO (on board SOHO).
# The VSO interface confirms that SOHO/LASCO is available.
instrument_event = a.Instrument("LASCO")

# Create the query using Fido.search for Event 1.
query_event1 = Fido.search(time_event1, instrument_event)

# Print out the query result details for Event 1.
print("Query result for Event 1 (November 4, 1997 CME):")
print(query_event1)

# Uncomment the following line to actually fetch the data for Event 1.
# files_event1 = Fido.fetch(query_event1)

# -------------------------
# Query for Event 2: June 6, 2000 CME
# -------------------------
# Define the time range for the June 6, 2000 event.
# The paper indicates that LASCO observations captured the CME and associated shock around this day.
time_event2 = a.Time("2000-06-06T00:00:00", "2000-06-06T23:59:59")

# Use the same instrument specification for LASCO.
# Query for LASCO data during this event.
query_event2 = Fido.search(time_event2, instrument_event)

# Print out the query result details for Event 2.
print("Query result for Event 2 (June 6, 2000 CME):")
print(query_event2)

# Uncomment the following line to actually fetch the data for Event 2.
# files_event2 = Fido.fetch(query_event2)

if __name__ == "__main__":
    # Running this script will print out the query results.
    # Remove comments on fetch lines to download the data.
    pass
