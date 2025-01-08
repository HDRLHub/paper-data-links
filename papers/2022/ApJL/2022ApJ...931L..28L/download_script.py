# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a

# Define the time range for the data collection period
time_range = a.Time('2002-07-23 00:25', '2002-07-23 00:33')

# Define the instrument of interest
instrument = a.Instrument('rhessi')

# Construct the query
query = Fido.search(time_range, instrument)

# Print the query results
print(query)

# Note: The VSOClient results show negative sizes, which is unusual. This might be a display issue or a problem with the data source.
# Note: Be aware of potential pagination issues when dealing with large datasets.

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
