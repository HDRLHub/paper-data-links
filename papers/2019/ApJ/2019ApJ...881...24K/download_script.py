# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query SDO/AIA data in the EUV 211 Å channel.
According to the context, we are interested in imaging the flux rope and shock observed in the EUV on 2016-03-16 between 06:36:34 UT and 06:38:22 UT.
The VSO interface indicates that SDO/AIA data are available (with 211 Å among the wavelengths) and this query reflects those explicit values.
Note: The Fido.fetch command is commented out to avoid automatic data download.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range from the observation (2016-03-16 06:36:34 to 06:38:22 UT)
time_start = '2016-03-16T06:36:34'
time_end = '2016-03-16T06:38:22'
time_range = a.Time(time_start, time_end)

# Define the instrument as SDO/AIA (the VSO interface contains data for SDO/AIA)
instrument = a.Instrument('AIA')

# Define the wavelength filter using the 211 Å channel (EUV; available as per the VSO interface)
wavelength = a.Wavelength(211*u.AA, 211*u.AA)

# Construct and execute the query
print("Querying VSO for SDO/AIA 211 Å data from {} to {}...".format(time_start, time_end))
result = Fido.search(time_range, instrument, wavelength)

# Print the query result summary details
print(result)

# Downloading data:
# Uncomment the following line to download the data once you have verified the query results.
# downloaded_files = Fido.fetch(result)

if __name__ == '__main__':
    pass
