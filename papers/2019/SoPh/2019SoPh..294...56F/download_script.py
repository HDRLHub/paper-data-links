# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs SunPy VSO queries to download observational data used in the study of the 11 April 2013 EUV wave event.
The observations include:
    1. SDO/AIA 193 Å imaging during the fast-component EUV wave (07:04 UT – 07:11 UT on 11 April 2013)
    2. SDO/AIA 171 Å imaging for coronal loop oscillations (around 07:20 UT on 11 April 2013)
    3. SDO/HMI magnetogram (Fe I 6173 Å) taken at 06:04 UT on 11 April 2013
    4. SOHO/LASCO C2 white-light coronagraph imagery (first appearance of the CME near 07:36 UT on 11 April 2013)
    5. SOHO/LASCO C3 white-light coronagraph imagery (CME in the C3 field-of-view near 09:06 UT on 11 April 2013)

Note:
 - The VSO interface provided confirms that these instruments are available.
 - Fido.fetch commands are included but commented out so that only the query results are printed.
"""

from sunpy.net import Fido, attrs as a
from astropy import units as u

# ------------------------------
# 1. Query SDO/AIA 193 Å for EUV Wave Imaging
# ------------------------------
# Define the time range for the fast-component EUV wave
start_time_aia193 = "2013-04-11T07:04:00"
end_time_aia193   = "2013-04-11T07:11:00"

# Construct the query for SDO/AIA in the 193 Å channel.
# Note: The available wavelengths for AIA are specified as "191.0 - 195.0 Å" in the interface.
result_aia193 = Fido.search(
    a.Time(start_time_aia193, end_time_aia193),
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Wavelength(193*u.AA)
)

print("Query Result for SDO/AIA 193 Å (EUV Wave Imaging):")
print(result_aia193)
# Uncomment the following line to download the data
# files_aia193 = Fido.fetch(result_aia193)

# ------------------------------
# 2. Query SDO/AIA 171 Å for Coronal Loop Oscillations
# ------------------------------
# Define a narrow time range around the observed oscillation (07:20 UT).
start_time_aia171 = "2013-04-11T07:19:00"
end_time_aia171   = "2013-04-11T07:21:00"

# Construct the query for SDO/AIA in the 171 Å channel.
# The available wavelengths include the range "171.0 - 175.0 Å".
result_aia171 = Fido.search(
    a.Time(start_time_aia171, end_time_aia171),
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Wavelength(171*u.AA)
)

print("\nQuery Result for SDO/AIA 171 Å (Coronal Loop Oscillations):")
print(result_aia171)
# Uncomment the following line to download the data
# files_aia171 = Fido.fetch(result_aia171)

# ------------------------------
# 3. Query SDO/HMI Magnetogram (Fe I 6173 Å)
# ------------------------------
# Define the time for the representative magnetogram.
start_time_hmi = "2013-04-11T06:04:00"
end_time_hmi   = "2013-04-11T06:04:10"  # A short interval around the specified time

# Construct the query for SDO/HMI magnetogram.
# The interface states the available wavelength for HMI is "6173.0 - 6174.0 Å".
result_hmi = Fido.search(
    a.Time(start_time_hmi, end_time_hmi),
    a.Instrument("HMI"),
    a.Source("SDO"),
    a.Wavelength(6173*u.AA)
)

print("\nQuery Result for SDO/HMI Magnetogram (6173 Å):")
print(result_hmi)
# Uncomment the following line to download the data
# files_hmi = Fido.fetch(result_hmi)

# ------------------------------
# 4. Query SOHO/LASCO C2 for CME Observation
# ------------------------------
# Define the time range for the first appearance of the CME in the C2 field-of-view.
start_time_lasco_c2 = "2013-04-11T07:36:00"
end_time_lasco_c2   = "2013-04-11T07:40:00"

# Construct the query for LASCO C2 data.
result_lasco_c2 = Fido.search(
    a.Time(start_time_lasco_c2, end_time_lasco_c2),
    a.Instrument("LASCO"),
    a.Source("SOHO"),
    a.Detector("C2")
)

print("\nQuery Result for SOHO/LASCO C2 (CME first appearance):")
print(result_lasco_c2)
# Uncomment the following line to download the data
# files_lasco_c2 = Fido.fetch(result_lasco_c2)

# ------------------------------
# 5. Query SOHO/LASCO C3 for CME Propagation Observation
# ------------------------------
# Define the time range for when the CME enters the C3 field-of-view.
start_time_lasco_c3 = "2013-04-11T09:06:00"
end_time_lasco_c3   = "2013-04-11T09:10:00"

# Construct the query for LASCO C3 data.
result_lasco_c3 = Fido.search(
    a.Time(start_time_lasco_c3, end_time_lasco_c3),
    a.Instrument("LASCO"),
    a.Source("SOHO"),
    a.Detector("C3")
)

print("\nQuery Result for SOHO/LASCO C3 (CME propagation):")
print(result_lasco_c3)
# Uncomment the following line to download the data
# files_lasco_c3 = Fido.fetch(result_lasco_c3)

if __name__ == '__main__':
    # This main block ensures the script can be executed directly.
    print("\nAll queries have been executed. Please review the output above for query details.")
