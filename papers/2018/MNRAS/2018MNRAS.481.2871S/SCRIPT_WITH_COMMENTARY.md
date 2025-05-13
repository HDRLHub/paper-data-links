# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query archival data from the SOHO VIRGO/SPM red channel.
In the context of the paper, the VIRGO/SPM red channel (with an effective wavelength around 0.86 µm)
was used to validate stellar variability models. The data were chosen from the year 2002 over a 300‐hour timeframe
with a 60 s cadence.

Note:
    The VSO interface provided only contains SOHO VIRGO data with various detectors.
    To mimic the red channel data, we use the VIRGO instrument with the SPM detector.
    The query is set for a 300-hour period in 2002 (starting at 2002-01-01T00:00:00) and ending after 300 hours.
    Only the required values (time range and instrument) are specified explicitly.
    
    The Fido.fetch command is commented out to prevent accidental data download.
"""

from sunpy.net import Fido, attrs as a
from datetime import timedelta, datetime

# Define the start time and compute the end time 300 hours later (300 hours = 12.5 days)
start_time = "2002-01-01T00:00:00"
# Calculate end time as 300 hours after start time using datetime arithmetic
start_dt = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
end_dt = start_dt + timedelta(hours=300)
end_time = end_dt.strftime("%Y-%m-%dT%H:%M:%S")

# Print the time range we are querying
print("Querying SOHO VIRGO/SPM red channel data from {} to {}".format(start_time, end_time))

# Build the query.
# We use:
#   a.Time : to set the time range,
#   a.Source : "SOHO" to ensure the source is SOHO,
#   a.Instrument : "VIRGO" to select the VIRGO instrument,
#   a.Detector : "SPM" approximately corresponding to the red channel
query = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("VIRGO"),
    a.Detector("SPM")
)

# Print the query result summary
print("Search Results:")
print(query)

# To actually download the data, one would use Fido.fetch:
# fetched_files = Fido.fetch(query)
# print("Downloaded files:")
# print(fetched_files)

if __name__ == '__main__':
    # The script prints the search results; downloading is commented out.
    pass
