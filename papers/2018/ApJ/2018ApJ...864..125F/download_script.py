# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries SOHO/MDI magnetogram data from the Virtual Solar Observatory (VSO)
using SunPy's Fido interface. We use SOHO/MDI data for the line-of-sight magnetic field,
which are used to construct synoptic magnetograms as described in the context.

According to the context, SOHO/MDI data were primarily used during sunspot Cycle 23 
(approximately August 1996 to December 2008). Therefore, we query data between these dates.
Note that while the VSO interface provides several observables for MDI, we choose the
'LOS_magnetic_field' observable for our query.

The Fido.fetch command is commented out below, meaning the script will only print the
query results without downloading the data.
"""

from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Define the time range based on context: August 1996 to December 2008
start_time = "1996-08-01"
end_time = "2008-12-31"

# Define the time attribute using SunPy's TimeRange
time_range = a.Time(start_time, end_time)

# Set up attributes for querying SOHO/MDI data:
# - Source: "SOHO" (spacecraft)
# - Instrument: "MDI" (Michelson Doppler Imager)
# - Detector: "MDI" (as per the VSO interface)
# - Physical observable: "LOS_magnetic_field" (used for synoptic magnetograms)
mdi_source = a.Source("SOHO")
mdi_instrument = a.Instrument("MDI")
mdi_detector = a.Detector("MDI")
mdi_physobs = a.Physobs("LOS_magnetic_field")

# Query the VSO for SOHO/MDI LOS magnetic field data within the specified time range.
result = Fido.search(time_range, mdi_source, mdi_instrument, mdi_detector, mdi_physobs)

# Print the query results
print("Query Results for SOHO/MDI LOS Magnetic Field Data (August 1996 to December 2008):")
print(result)

# To actually download the data, uncomment the following line:
# downloaded_files = Fido.fetch(result)

if __name__ == "__main__":
    # Running the query and printing out the results
    pass
