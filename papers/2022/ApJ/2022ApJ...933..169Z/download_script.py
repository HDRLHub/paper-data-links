# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Define a time range for the search
# Note: If the time range is too broad, it may result in no data being found.
# Example time range provided to avoid this issue.
time_range = TimeRange("2022-01-01", "2022-01-02")  # Using smaller example time range

# Perform a search for solar data using VSO
# Note: Large result sets may be paginated. Consider this when processing results.
result = Fido.search(a.Time(time_range.start, time_range.end), a.Instrument('AIA'))  # Example instrument

# Display the search results
print(result)
