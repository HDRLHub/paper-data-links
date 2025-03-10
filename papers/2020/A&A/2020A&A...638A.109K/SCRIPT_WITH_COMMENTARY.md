# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs a SunPy VSO query for downloading MDI synoptic magnetogram data
from the Michelson Doppler Imager (MDI) onboard SOHO. According to the paper's context,
we focus on the high-resolution synoptic magnetograms used for detailed Carrington maps,
specifically for Carrington rotation 2066 in early 2008, which captures the line-of-sight
magnetic field measurements (photospheric magnetic flux density). The selected query
parameters are consistent with the VSO interface entries available for SOHO/MDI.
"""

from sunpy.net import Fido, attrs as a

# Define the time range around early 2008.
# Carrington rotation 2066 during the solar minimum in early 2008 is approximated here as February 2008.
start_time = "2008-02-01"
end_time = "2008-02-28"

# Set up the query parameters using SunPy VSO attributes.
# a.Time: Defines the start and end times for the data search.
# a.Source: Specifies the data source, which is SOHO in this case.
# a.Instrument: Specifies the instrument; we use MDI.
# a.Physobs: Specifies the physical observable; here, we request line-of-sight magnetic field data.
query_time = a.Time(start_time, end_time)
query_source = a.Source("SOHO")
query_instrument = a.Instrument("MDI")
query_physobs = a.Physobs("LOS_magnetic_field")

# Perform the query.
# The result will contain the metadata corresponding to the available MDI data that matches our criteria.
result = Fido.search(query_time, query_source, query_instrument, query_physobs)

# Print the details of the query result.
print("Query Results:")
print(result)

# To download the data, you can use Fido.fetch.
# Uncomment the following lines to fetch the data files.
# downloaded_files = Fido.fetch(result)
# print("Downloaded Files:")
# print(downloaded_files)
