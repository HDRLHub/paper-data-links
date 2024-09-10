# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido
from sunpy.net import attrs as a

# Define the time range for the query
time_range = a.Time('1996-01-01', '2023-10-01')  # Adjust the end date as needed

# Define the instrument and source
instrument = a.Instrument('GOLF')
source = a.Source('SOHO')

# Construct the query
query = Fido.search(time_range, instrument, source)

# Print out the query results
print(query)

# Note: The query results may be paginated due to the large number of results.
# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
