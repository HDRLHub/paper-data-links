# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates building Sunpy VSO queries for CME-related observations
as inspired by the provided context. The observations include data from the
SDO mission (AIA and HMI), STEREO missions (STEREO-A and STEREO-B SECCHI EUVI), and
SOHO (LASCO C2 and C3). Each query explicitly sets up the time range and the instrument,
matching instruments available in the provided VSO interface.
Note:
  - The script prints out query results.
  - Actual data downloading (using Fido.fetch) is commented out.
"""

import datetime
from sunpy.net import Fido, attrs as a

# Define the time range for the query.
# Here we choose a sample time window that lies within the available full time ranges provided.
# For these examples, we use a 12-hour window on 2020-06-01.
start_time = "2020-06-01T00:00:00"
end_time = "2020-06-01T12:00:00"

# Query for SDO AIA data.
# SDO/AIA provides multi-wavelength EUV images for tracking low-coronal signatures.
query_aia = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Source('SDO')
)
print("SDO AIA query results:")
print(query_aia)
# Uncomment the following line to fetch the data
# aia_files = Fido.fetch(query_aia)

# Query for SDO HMI data.
# SDO/HMI supplies high resolution photospheric magnetic field measurements.
query_hmi = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('HMI'),
    a.Source('SDO')
)
print("\nSDO HMI query results:")
print(query_hmi)
# Uncomment the following line to fetch the data
# hmi_files = Fido.fetch(query_hmi)

# Query for STEREO-A SECCHI EUVI data.
# The EUVI channel of the SECCHI instrument on STEREO-A is used for imaging the lower corona.
query_stereo_a_euvi = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('SECCHI'),
    a.Source('STEREO_A'),
    a.Detector('EUVI')
)
print("\nSTEREO-A SECCHI EUVI query results:")
print(query_stereo_a_euvi)
# Uncomment the following line to fetch the data
# stereo_a_euvi_files = Fido.fetch(query_stereo_a_euvi)

# Query for STEREO-B SECCHI EUVI data.
# Similar to STEREO-A, STEREO-B’s EUVI observations help in multi-point CME imaging.
query_stereo_b_euvi = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('SECCHI'),
    a.Source('STEREO_B'),
    a.Detector('EUVI')
)
print("\nSTEREO-B SECCHI EUVI query results:")
print(query_stereo_b_euvi)
# Uncomment the following line to fetch the data
# stereo_b_euvi_files = Fido.fetch(query_stereo_b_euvi)

# Query for SOHO LASCO C2 data.
# LASCO C2 provides white-light imaging of CMEs.
query_lasco_c2 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('LASCO'),
    a.Source('SOHO'),
    a.Detector('C2')
)
print("\nSOHO LASCO C2 query results:")
print(query_lasco_c2)
# Uncomment the following line to fetch the data
# lasco_c2_files = Fido.fetch(query_lasco_c2)

# Query for SOHO LASCO C3 data.
# LASCO C3 extends the field-of-view to further track CME propagation.
query_lasco_c3 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('LASCO'),
    a.Source('SOHO'),
    a.Detector('C3')
)
print("\nSOHO LASCO C3 query results:")
print(query_lasco_c3)
# Uncomment the following line to fetch the data
# lasco_c3_files = Fido.fetch(query_lasco_c3)

if __name__ == "__main__":
    print("\nAll queries executed. Please review the printed query results for details.")
