# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query SDO/AIA data available from the Virtual Solar Observatory (VSO)
using sunpy. The query is designed in reference to a paper investigating the formation times of eruptive 
hot magnetic flux ropes using long (more than eight hours) sequences of AIA images, especially in the 131 Å passband.
The query selects data from the Atmospheric Imaging Assembly (AIA) on board SDO with a user-specified time range.
The wavelengths available from AIA include passbands such as 94, 131, 171, 193, 211, 304, and 335 Å. 
Due to the focus of the study, we demonstrate a query for the 131 Å channel.
Note: Actual data download via Fido.fetch is commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the observation. The paper uses more than eight hours ending a few minutes after the eruption.
# Here we choose an example eight-hour interval.
start_time = "2015-06-15T00:00:00"
end_time   = "2015-06-15T08:00:00"

# Define the instrument attributes.
# We query for data from the Atmospheric Imaging Assembly (AIA) on board the Solar Dynamics Observatory (SDO).
instrument = a.Instrument("AIA")

# Define the wavelength attribute.
# The paper primarily focuses on the 131 Å passband (among others).
wavelength = a.Wavelength(130*u.Angstrom, 132*u.Angstrom)

# Define the time attribute.
time_range = a.Time(start_time, end_time)

# Build the query explicitly with the defined parameters.
# This query is specific for the SDO AIA data as used in the study.
print("Querying VSO for SDO/AIA 131 Å data from {} to {}...".format(start_time, end_time))
result = Fido.search(time_range, instrument, wavelength)

# Print out the query results.
print(result)

# Uncomment the following lines to download the data once the query is verified.
# download_files = Fido.fetch(result)
# print("Download completed. Files:", download_files)

if __name__ == '__main__':
    pass
