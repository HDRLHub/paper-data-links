# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script demonstrates how to query solar data using SunPy's VSO interface for a compound eruption event observed in NOAA AR 11429.
We construct separate queries for:
  1. SDO/AIA data (EUV imaging) from 2012-03-09 04:00 UT to 2012-03-10 19:00 UT.
  2. SDO/HMI data (magnetic field observations) from 2012-03-09 04:00 UT to 2012-03-10 19:00 UT.
  3. STEREO-A SECCHI/EUVI observations from 2012-03-10 16:31:32 to 2012-03-10 18:08:32.
  
The Fido.fetch calls are provided as commented-out examples. We simply print the query results.
"""

from sunpy.net import Fido, attrs as a
import datetime

#----------------------------
# 1. Query SDO/AIA Data
#----------------------------
# Define the time range for the AIA observations as per the paper:
start_time_aia = '2012-03-09T04:00:00'
end_time_aia = '2012-03-10T19:00:00'

# Construct the query:
# Instrument is AIA onboard SDO and we rely on available wavelengths (e.g., 94, 131, 1600, 304 are mentioned in the paper)
aia_query = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Instrument('AIA'),
    a.Source('SDO')
)

print("SDO/AIA Query Result:")
print(aia_query)
# To actually download the data, uncomment the line below:
# files_aia = Fido.fetch(aia_query)

#----------------------------
# 2. Query SDO/HMI Data
#----------------------------
# Define the time range for the HMI observations (matching the AIA observation period):
start_time_hmi = '2012-03-09T04:00:00'
end_time_hmi = '2012-03-10T19:00:00'

# Construct the query:
# Instrument is HMI, obtaining magnetic field data.
hmi_query = Fido.search(
    a.Time(start_time_hmi, end_time_hmi),
    a.Instrument('HMI'),
    a.Source('SDO')
)

print("\nSDO/HMI Query Result:")
print(hmi_query)
# To actually download the data, uncomment the line below:
# files_hmi = Fido.fetch(hmi_query)

#----------------------------
# 3. Query STEREO-A SECCHI/EUVI Data
#----------------------------
# Define the time range for STEREO-A EUVI observations as per the paper:
start_time_euvi = '2012-03-10T16:31:32'
end_time_euvi = '2012-03-10T18:08:32'

# Construct the query:
# Instrument: SECCHI, Detector: EUVI, Source: STEREO_A.
euvi_query = Fido.search(
    a.Time(start_time_euvi, end_time_euvi),
    a.Instrument('SECCHI'),
    a.Detector('EUVI'),
    a.Source('STEREO_A')
)

print("\nSTEREO-A SECCHI/EUVI Query Result:")
print(euvi_query)
# To actually download the data, uncomment the line below:
# files_euvi = Fido.fetch(euvi_query)

if __name__ == "__main__":
    # The script prints the query results. Uncomment Fido.fetch calls for actual downloads.
    pass
