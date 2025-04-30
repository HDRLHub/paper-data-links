# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a

# Define the time range for the query
# Note: The original time range is very large and may result in paginated results.
# Using a smaller example time range for demonstration purposes.
time_range = a.Time('1996-01-01', '1996-01-31')  # Example time range within the original range

# Define the instrument and source
instrument = a.Instrument('LASCO')
source = a.Source('SOHO')

# Query for LASCO C2 and C3 data within the specified time range
query_result = Fido.search(time_range, source, instrument, a.Detector('C2') | a.Detector('C3'))

# Print the query results
print(query_result)

# Uncomment the following line to download the data
# files = Fido.fetch(query_result)

# Warning: The results may be paginated due to the large number of results.
