# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Example time range for the query
time_range = TimeRange("2022-01-01", "2022-01-02")

# Perform a VSO search for AIA data as an example
# Note: The result set is large, which may indicate pagination. Be aware of this when processing results.
result = Fido.search(a.Time(time_range.start, time_range.end), a.Instrument('AIA'))

# Print the search results
print(result)
