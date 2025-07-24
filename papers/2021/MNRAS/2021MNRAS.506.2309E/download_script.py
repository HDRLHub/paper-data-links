# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query SOHO/MDI magnetograms measuring the line‐of‐sight magnetic field.
Based on the provided vso_interface and context:
• The instrument is SOHO/MDI.
• We choose to query the LOS_magnetic_field observable.
• The time range is picked as an example (July 1–2, 2001) which falls within the available MDI observation period.
Note: Although the context mentions GONG and HMI datasets, only SOHO/MDI is available in the provided VSO interface.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range.
# The chosen date range (2001-07-01 to 2001-07-02) lies within the available SOHO/MDI magnetogram period.
time_range = a.Time("2001-07-01", "2001-07-02")

# Define query attributes for the instrument SOHO/MDI.
# Source is set to "SOHO", instrument is "MDI" and we request the line-of-sight magnetic field observable.
source = a.Source("SOHO")
instrument = a.Instrument("MDI")
physobs = a.Physobs("LOS_magnetic_field")

# Construct the query using Fido.search.
result = Fido.search(time_range, source, instrument, physobs)

# Print out the query results.
print("Search results for SOHO/MDI LOS_magnetic_field data:")
print(result)

# To download the data, uncomment the following lines.
# downloaded_files = Fido.fetch(result)
# print("Downloaded files:")
# print(downloaded_files)
