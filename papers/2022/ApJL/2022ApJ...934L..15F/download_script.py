# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a

# Define the time range for the SEP event observation
time_range = a.Time('2020-11-28', '2020-12-05')

# Define the instrument and source for the query
instrument = a.Instrument('ERNE')
source = a.Source('SOHO')

# Construct the query using the defined attributes
query = Fido.search(time_range, instrument, source)

# Print the query results
print(query)

# Note: If the number of results is very large, consider checking for pagination.
# Uncomment the following line to download the data
# files = Fido.fetch(query)
