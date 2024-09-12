# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido
from sunpy.net import attrs as a

# Define the time range for the query
# Using a slightly broader time range to ensure data capture
# Original time range: a.Time('2006-12-12T20:51:01', '2006-12-12T20:51:01')
time_range = a.Time('2006-12-12T20:00:00', '2006-12-13T00:00:00')

# Define the instrument and source
instrument = a.Instrument('mdi')
source = a.Source('soho')

# Construct the query
query = Fido.search(time_range, instrument, source)

# Print out the query results
print(query)

# Note: The query returned 316 results, which might indicate pagination.
# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
