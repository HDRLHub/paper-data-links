# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a

# Define the instrument and time ranges based on the context
instrument = a.Instrument('mdi')

# Using smaller example time range due to potential issue with broad time range
# Original time range: a.Time('1996-01-01', '2011-10-31')
# Trying a smaller time range within the original range to resolve the issue of no results
time_range_training_validation = a.Time('1996-01-01', '1996-01-07')

# Using smaller example time range due to potential issue with broad time range
# Original time range: a.Time('1996-11-01', '2011-12-31')
time_range_test = a.Time('1996-11-01', '1996-11-30')

# Query for the training and validation set
print("Querying for Training and Validation Set:")
query_training_validation = Fido.search(time_range_training_validation, instrument)
print(query_training_validation)

# Uncomment the following line to fetch the data
# Fido.fetch(query_training_validation)

# Query for the test set
print("Querying for Test Set:")
query_test = Fido.search(time_range_test, instrument)
print(query_test)

# Uncomment the following line to fetch the data
# Fido.fetch(query_test)

# Note: The test set query returned 317 results, which might indicate pagination.
# Be aware of potential pagination issues when handling large result sets.
