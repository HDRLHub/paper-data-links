# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query data corresponding to instruments discussed in the paper.
The observations focus on the active region NOAA 11875 on 2013 October 28 between 00:30 UT and 04:30 UT.
We query SDO instruments (AIA and HMI), RHESSI, and SOHO LASCO (C2 and C3). Note that all Fido.fetch
commands are commented out to avoid downloading data automatically.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs as a

# Define the start and end times for the observation period
start_time = '2013-10-28T00:30:00'
end_time   = '2013-10-28T04:30:00'

#-------------------------------------------
# Query for SDO AIA Data
#-------------------------------------------
# AIA observes the Sun in multiple (E)UV channels and white light, as discussed in the paper.
query_aia = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SDO'),
    a.Instrument('AIA')
)
print("SDO AIA Search Result:")
print(query_aia)

# Uncomment the following lines to download AIA data
# downloaded_files_aia = Fido.fetch(query_aia)
# print("Downloaded SDO AIA Data:")
# print(downloaded_files_aia)

#-------------------------------------------
# Query for SDO HMI Data
#-------------------------------------------
# HMI provides photospheric LOS magnetograms and intensity images.
query_hmi = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SDO'),
    a.Instrument('HMI')
)
print("\nSDO HMI Search Result:")
print(query_hmi)

# Uncomment the following lines to download HMI data
# downloaded_files_hmi = Fido.fetch(query_hmi)
# print("Downloaded SDO HMI Data:")
# print(downloaded_files_hmi)

#-------------------------------------------
# Query for RHESSI Data
#-------------------------------------------
# RHESSI data is used for hard X-ray imaging spectroscopy during the flare.
query_rhessi = Fido.search(
    a.Time(start_time, end_time),
    a.Source('RHESSI'),
    a.Instrument('RHESSI')
)
print("\nRHESSI Search Result:")
print(query_rhessi)

# Uncomment the following lines to download RHESSI data
# downloaded_files_rhessi = Fido.fetch(query_rhessi)
# print("Downloaded RHESSI Data:")
# print(downloaded_files_rhessi)

#-------------------------------------------
# Query for SOHO LASCO C2 Data
#-------------------------------------------
# LASCO C2 observes the corona in white light and is effective for CME studies.
query_lasco_c2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("\nSOHO LASCO C2 Search Result:")
print(query_lasco_c2)

# Uncomment the following lines to download LASCO C2 data
# downloaded_files_lasco_c2 = Fido.fetch(query_lasco_c2)
# print("Downloaded SOHO LASCO C2 Data:")
# print(downloaded_files_lasco_c2)

#-------------------------------------------
# Query for SOHO LASCO C3 Data
#-------------------------------------------
# LASCO C3 provides observations at larger scales for tracking the CME.
query_lasco_c3 = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C3')
)
print("\nSOHO LASCO C3 Search Result:")
print(query_lasco_c3)

# Uncomment the following lines to download LASCO C3 data
# downloaded_files_lasco_c3 = Fido.fetch(query_lasco_c3)
# print("Downloaded SOHO LASCO C3 Data:")
# print(downloaded_files_lasco_c3)

if __name__ == '__main__':
    print("\nVSO data query script completed successfully.")
