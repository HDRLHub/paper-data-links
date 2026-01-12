# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs a SunPy VSO query to retrieve SDO/AIA EUV data at 211 Å.
The query is targeted at a snapshot observation at 22:36 UT on 2016 October 8,
which is used in the study to map the solar corona by examining coronal holes and dimming regions.
Note: The Fido.fetch command is commented out to avoid accidental data download.
"""

# Import required modules
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the observation time range using a snapshot at 22:36 UT on 2016 October 8.
start_time = '2016-10-08T22:36:00'
end_time   = '2016-10-08T22:36:00'

# Define instrument information: Using SDO/AIA with the 211 Å channel.
instrument = 'AIA'
wavelength_value = 211 * u.AA  # 211 Angstroms

# Build and execute the VSO query for SDO/AIA 211 Å data at the specified time.
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument(instrument),
    a.Wavelength(wavelength_value)
)

# Print out the query results.
print("Query Results for SDO/AIA 211 Å on 2016 October 8 at 22:36 UT:")
print(query_result)

# To download the data, uncomment the following lines:
# downloaded_files = Fido.fetch(query_result)
# print("Downloaded Files:", downloaded_files)

if __name__ == "__main__":
    # This main guard is optional but useful if the script is to be executed directly.
    pass
