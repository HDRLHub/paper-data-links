# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query solar data corresponding to the observational campaign
described in the paper. The observations cover 2012 August 4 at 23:00 UT to 2012 August 6 at 08:00 UT.
We query data from:
  1. SDO/AIA – to monitor filament plasma evolution in discrete EUV wavebands (171, 193, 211, and 304 Å)
  2. SDO/HMI – to study photospheric magnetic field evolution (magnetograms)
  3. STEREO-B SECCHI/EUVI – to measure the filament height at 2012 August 4 at 23:00 UT

Note: The Fido.fetch calls are provided as comments. This script prints the query results.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the common time range for the observations
start_time = '2012-08-04T23:00:00'
end_time = '2012-08-06T08:00:00'
time_range = a.Time(start_time, end_time)

# -------------------------------
# 1. Query for SDO/AIA Data
#
# For AIA, we focus on the four wavebands: 171 Å, 193 Å, 211 Å, and 304 Å.
# The available wavelength information in the VSO shows ranges that include these wavelengths.
# We define a narrow wavelength range (±0.5 Å) around each target wavelength.
# -------------------------------

# Query for the 171 Å channel
aia_wave_171 = a.Wave((171 - 0.5) * u.AA, (171 + 0.5) * u.AA)
query_aia_171 = Fido.search(
    time_range,
    a.Instrument('AIA'),
    aia_wave_171,
    a.Source('SDO')
)
print("SDO/AIA 171 Å Query Result:")
print(query_aia_171)
# To fetch the data for 171 Å:
# files_aia_171 = Fido.fetch(query_aia_171)

# Query for the 193 Å channel
aia_wave_193 = a.Wave((193 - 0.5) * u.AA, (193 + 0.5) * u.AA)
query_aia_193 = Fido.search(
    time_range,
    a.Instrument('AIA'),
    aia_wave_193,
    a.Source('SDO')
)
print("\nSDO/AIA 193 Å Query Result:")
print(query_aia_193)
# To fetch the data for 193 Å:
# files_aia_193 = Fido.fetch(query_aia_193)

# Query for the 211 Å channel
aia_wave_211 = a.Wave((211 - 0.5) * u.AA, (211 + 0.5) * u.AA)
query_aia_211 = Fido.search(
    time_range,
    a.Instrument('AIA'),
    aia_wave_211,
    a.Source('SDO')
)
print("\nSDO/AIA 211 Å Query Result:")
print(query_aia_211)
# To fetch the data for 211 Å:
# files_aia_211 = Fido.fetch(query_aia_211)

# Query for the 304 Å channel
aia_wave_304 = a.Wave((304 - 0.5) * u.AA, (304 + 0.5) * u.AA)
query_aia_304 = Fido.search(
    time_range,
    a.Instrument('AIA'),
    aia_wave_304,
    a.Source('SDO')
)
print("\nSDO/AIA 304 Å Query Result:")
print(query_aia_304)
# To fetch the data for 304 Å:
# files_aia_304 = Fido.fetch(query_aia_304)

# -------------------------------
# 2. Query for SDO/HMI Data (Magnetograms)
#
# HMI data provides line-of-sight magnetograms used for studying the photospheric magnetic field evolution.
# We use the same time range for consistency.
# -------------------------------
query_hmi = Fido.search(
    time_range,
    a.Instrument('HMI'),
    a.Source('SDO')
)
print("\nSDO/HMI Query Result:")
print(query_hmi)
# To fetch the HMI data:
# files_hmi = Fido.fetch(query_hmi)

# -------------------------------
# 3. Query for STEREO-B SECCHI/EUVI Data
#
# To measure the filament height, we use SECCHI's EUVI detector on STEREO-B.
# The measurement is taken at the time of the first NLFFF model:
# 2012 August 4 at 23:00 UT. We use a short time window to capture the relevant data.
# -------------------------------
euvi_time_range = a.Time('2012-08-04T23:00:00', '2012-08-04T23:10:00')
query_euvi = Fido.search(
    euvi_time_range,
    a.Source('STEREO_B'),
    a.Instrument('SECCHI'),
    a.Detector('EUVI')
)
print("\nSTEREO-B SECCHI/EUVI Query Result:")
print(query_euvi)
# To fetch the EUVI data:
# files_euvi = Fido.fetch(query_euvi)

if __name__ == '__main__':
    print("\nCompleted all VSO queries for the specified instruments and time ranges.")
