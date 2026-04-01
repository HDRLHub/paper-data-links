# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query SDO/AIA data corresponding to the modeling study
described in the paper. Specifically, we query SDO/AIA EUV observations for Carrington Rotation CR2208,
with an observation time of 22:00:00 UT on 2018 September 15. The wavelengths chosen correspond to 
Fe ion emission channels: 94 Å, 193 Å (using the available range 191-195 Å to capture 193 Å) and 211 Å.
The query parameters (time and instrument) are taken from the provided context.
Note that STEREO-A/EUVI and LASCO data are not available in the provided VSO interface.
"""

import sys
from sunpy.net import Fido, attrs as a

# Define the observation time for CR2208 (2018-09-15 22:00:00 UT)
start_time = '2018-09-15T22:00:00'
end_time   = '2018-09-15T22:05:00'  # a short time interval around the target time; adjust as needed

# Construct query for SDO/AIA with chosen wavelengths.
# In the VSO interface, SDO/AIA lists the available wavelengths which include:
# 94.0, (191.0-195.0 which covers our 193 Å) and 211.0 Angstrom.
# We will query these three channels.
query_94  = Fido.search(a.Time(start_time, end_time),
                         a.Instrument('AIA'),
                         a.Source('SDO'),
                         a.Wavelength(93.5, 94.5))  # 94 Å channel

query_193 = Fido.search(a.Time(start_time, end_time),
                         a.Instrument('AIA'),
                         a.Source('SDO'),
                         a.Wavelength(191, 195))  # covers 193 Å

query_211 = Fido.search(a.Time(start_time, end_time),
                         a.Instrument('AIA'),
                         a.Source('SDO'),
                         a.Wavelength(210.5, 211.5))  # 211 Å channel

# Print the search results for each wavelength channel
print("SDO/AIA 94 Å channel query result:")
print(query_94)
print("\nSDO/AIA 193 Å channel query result:")
print(query_193)
print("\nSDO/AIA 211 Å channel query result:")
print(query_211)

# Uncomment the following lines to fetch the data after confirming the query results.
# fetched_files_94 = Fido.fetch(query_94)
# fetched_files_193 = Fido.fetch(query_193)
# fetched_files_211 = Fido.fetch(query_211)

if __name__ == '__main__':
    sys.exit(0)
