# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query SDO/AIA data for a solar flare
event on 2017-09-10, corresponding to the super-hot current sheet observed during
the SOL2017-09-10T X8.2-class event. The query covers the time period spanning
the initial eruption and current sheet formation (15:35 UT to 16:15 UT) as well
as later intermittent outflow jets (up to 18:10 UT).

The VSO interface shows that SDO/AIA data are available (with wavelengths including
94, 131, 171, 193, 211, 335, etc.) from 2010/05/12 (and also another entry from 2012/05/11) to the present.
Thus, we query SDO/AIA using a time range that spans the critical flare times.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the observation time ranges based on the scientific context
# Here we set a combined query time range from the initial phase to the later examples:
# From 2017-09-10 15:35:00 UT (filament activation and bubble formation)
# to 2017-09-10 18:10:00 UT (final outflow jet imaging)
start_time = "2017-09-10T15:35:00"
end_time   = "2017-09-10T18:10:00"

# Set the instrument and source attributes as per the available VSO interface.
# We query for SDO's Atmospheric Imaging Assembly (AIA) data.
# Although the scientific paper uses multiple wavelengths, the essential required values are the time range and the instrument.
query_attrs = [a.Time(start_time, end_time), a.Instrument("AIA"), a.Source("SDO")]

# Perform the query using Fido. The result will include data for the specified time period from SDO/AIA.
result = Fido.search(*query_attrs)

# Print the query result summary
print("Query results for SDO/AIA data (2017-09-10 15:35 UT to 18:10 UT):")
print(result)

# If desired, you could fetch the data using Fido.fetch.
# Note: The fetch command is commented-out to prevent unintended downloads.
# Uncomment the line below to download the data.
# downloaded_files = Fido.fetch(result)

# End of script

if __name__ == "__main__":
    print("Script completed. Check the above query results for details on the available data.")
