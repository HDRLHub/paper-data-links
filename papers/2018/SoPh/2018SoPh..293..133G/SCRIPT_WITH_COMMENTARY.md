# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Query Script for Downloading SWAP Data from PROBA2

This script sets up a query using Sunpy's Fido interface to search for
SWAP data on board PROBA2. According to the study context, SWAP EUV images 
at 174 Å were recorded during the solar eruptive event, with the time range
of interest from 10:31:21 UT to 10:55:12 UT on 2014-09-01. The available VSO
interface confirms that PROBA2/SWAP data is available with an appropriate 
wavelength range (171 - 174 Å or 174 Å), which is well suited for the event.

The script prints out the query result details. The Fido.fetch command 
is provided as a commented-out line for actual download if needed.
"""

from sunpy.net import Fido, attrs as a

# Define the time range for the SWAP observations as given in the context
start_time = '2014-09-01T10:31:21'
end_time = '2014-09-01T10:55:12'
time_range = a.Time(start_time, end_time)

# Define the instrument and source.
# Instrument: SWAP from PROBA2 (Sun Watcher using Active Pixel System)
instrument = a.Instrument('SWAP')
source = a.Source('PROBA2')

# Combine the attributes in a single query for clarity.
# Note: We use the available time range and instrument as the primary query parameters.
query = Fido.search(time_range, instrument, source)

# Print out the query result details
print("Query Result:")
print(query)

# Uncomment the following line to fetch the data files.
# downloaded_files = Fido.fetch(query)
