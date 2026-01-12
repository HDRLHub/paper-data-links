# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.map
from sunpy.net import vso, attrs as a

# Initialize the VSO client
client = vso.VSOClient()

# Define the time range for SOHO/LASCO CME imaging
time_range = a.Time('2001-11-21', '2001-11-22')

# Specify the data source and instrument
source = a.Source('SOHO')
instrument = a.Instrument('LASCO')
detector = a.Detector('C2')
physobs = a.Physobs('intensity')

# Build and execute the VSO query
query_response = client.search(time_range, source, instrument, detector, physobs)

# Display the query results
print("Query results for SOHO/LASCO C2 from 2001-11-21 to 2001-11-22:")
print(query_response)

# To download the data, uncomment the following line:
# downloaded_files = client.fetch(query_response)
