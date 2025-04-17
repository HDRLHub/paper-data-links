# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the VIRGO SPM data from the Virtual Solar Observatory (VSO)
using SunPy. The VIRGO SPM instrument, onboard SOHO, provides long-duration photometric
observations, which in our context are used to study solar oscillations over an 11-year cycle.
The observed lightcurves have 180-day segments with 90-day overlaps.
The available data for VIRGO SPM in the VSO is from "1995/12/06" to the present.
For this query, we choose a time range within the available period.
"""

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from datetime import datetime

# Define the time range for the query.
# Here we select an 11-year period representative for capturing one complete solar cycle.
start_time = "2000-01-01"
end_time = "2011-01-01"

# Construct the Fido query for VIRGO SPM data at SOHO.
# We use the following attributes:
#   - a.Time: The time range for the observation.
#   - a.Source: Data source "SOHO".
#   - a.Instrument: Instrument "VIRGO".
#   - a.Detector: Specific detector "SPM" to query the sun photometer data.
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("VIRGO"),
    a.Detector("SPM")
)

# Print out the query results.
print("VSO Query Result for VIRGO SPM Data:")
print(query_result)

# Uncomment the following line to download the data from VSO.
# downloaded_files = Fido.fetch(query_result)

if __name__ == "__main__":
    pass
