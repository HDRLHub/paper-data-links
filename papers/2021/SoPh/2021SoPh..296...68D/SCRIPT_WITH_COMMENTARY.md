# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's Fido interface to query the Virtual Solar Observatory (VSO)
for SDO/AIA data, specifically targeting EUV observations in the 193 Å passband.
The query time range is based on the observational case study: from 15:00 UT to 16:35 UT on 9 November 2016.
The SDO/AIA instrument is available in the provided VSO interface and the 193 Å wavelength
lies within the available wavelength range (191.0 - 195.0 Å).

Note: The Fido.fetch() command is commented out to prevent actual downloads.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the SDO/AIA observational data
start_time = '2016-11-09 15:00:00'
end_time = '2016-11-09 16:35:00'

# Define the instrument and source based on the context and the VSO interface relevant to SDO/AIA
# Using the 193 Å passband. Since the available wavelengths include "191.0 - 195.0", 193 Å is appropriate.
time_attr = a.Time(start_time, end_time)
instrument_attr = a.Instrument("AIA")
source_attr = a.Source("SDO")
wavelength_attr = a.Wavelength(193*u.AA, 193*u.AA)

# Build the query using SunPy's Fido.
# This explicit query avoids nested calls and loops.
query_result = Fido.search(time_attr, instrument_attr, source_attr, wavelength_attr)

# Print the query results to review the search output.
print(query_result)

# Uncomment the following line to fetch the data based on the query returned.
# fetched_files = Fido.fetch(query_result)

if __name__ == "__main__":
    pass
