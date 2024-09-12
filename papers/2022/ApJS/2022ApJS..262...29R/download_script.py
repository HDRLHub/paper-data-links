# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the query
# Using smaller example time range due to broad original range
time_range = a.Time('2017-01-01', '2017-12-31')  # Example time range within the original range

# Define the instrument and source
instrument = a.Instrument('sem')
source = a.Source('soho')  # Corrected source to match the instrument

# Construct the query
query = Fido.search(time_range, source, instrument)

# Print out the query results
print(query)

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
