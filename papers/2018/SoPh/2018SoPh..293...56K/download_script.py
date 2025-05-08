# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs a VSO query using SunPy for SOHO/MDI magnetogram data (LOS_magnetic_field)
that are available in the Virtual Solar Observatory. The query is configured to retrieve data from
October 15, 2007 between 08:00 UT and 11:00 UT. This time range and instrument choice directly
reflect the scientific campaign described in the context for MDI high-resolution magnetograms.
Note: The data are not fetched but only the query results are printed. The Fido.fetch call is provided
and commented out for further use if desired.
"""

# Import necessary classes from sunpy.net
from sunpy.net import Fido, attrs as a

# Define the observation time range
start_time = "2007-10-15T08:00:00"
end_time = "2007-10-15T11:00:00"

# Construct the VSO query for SOHO/MDI LOS_magnetic_field data.
# The instrument 'MDI' on board SOHO provides magnetograms used for photospheric magnetic field studies.
query = Fido.search(
    a.Time(start_time, end_time),            # Specify the time range from context
    a.Source("SOHO"),                        # Ensure source is SOHO
    a.Instrument("MDI"),                     # Instrument must be MDI, as available from VSO interface
    a.Physobs("LOS_magnetic_field")          # We select the LOS_magnetic_field observable required for magnetograms
)

# Print out the query results.
print("Query Results:")
print(query)

# The following line is the command to fetch the data,
# but it is commented out to prevent actual downloading.
# downloaded_files = Fido.fetch(query)

if __name__ == '__main__':
    # The script has executed the query and printed results.
    pass
