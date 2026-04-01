# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs explicit SunPy VSO queries for downloading multiwavelength solar observations
related to the study of a filament eruption and reformation in NOAA AR 11791 on 2013 July 15.
We query data from the following instruments (as available via the VSO):
  1. SDO/AIA – to capture EUV images at wavelengths 304 Å, 94 Å, and 193 Å during the eruption phase.
  2. SDO/HMI – to capture photospheric magnetic field measurements (Fe I 6173 Å) covering the flux emergence and magnetic evolution.
  3. RHESSI – to capture hard X-ray data (6–12 keV) during the impulsive phase.
  
Note: Other instruments (e.g., NVST, GOES, LASCO) mentioned in the paper are not available in the provided VSO interface.
The Fido.fetch commands have been provided as comments and are not executed.
"""

# Import necessary modules from SunPy and astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# -------------------------------
# 1. Query SDO/AIA data
# -------------------------------
# Time range for the filament eruption phase as described in the paper:
# 2013 July 15, from about 00:30 UT to 04:30 UT.
aia_time_start = "2013-07-15T00:30:00"
aia_time_end   = "2013-07-15T04:30:00"

# We query three wavelengths available: 304 Å, 94 Å, and 193 Å.
# The AIA instrument is part of SDO.
# The wavelength attribute accepts units in Angstrom.
query_aia_304 = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Instrument("AIA"),
    a.Wavelength(304*u.AA, 304*u.AA)
)
print("SDO/AIA 304 Å query results:")
print(query_aia_304)

query_aia_94 = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Instrument("AIA"),
    a.Wavelength(94*u.AA, 94*u.AA)
)
print("\nSDO/AIA 94 Å query results:")
print(query_aia_94)

query_aia_193 = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Instrument("AIA"),
    a.Wavelength(193*u.AA, 193*u.AA)
)
print("\nSDO/AIA 193 Å query results:")
print(query_aia_193)

# Uncomment the following lines to fetch the data once you have verified the query results.
# files_aia_304 = Fido.fetch(query_aia_304)
# files_aia_94  = Fido.fetch(query_aia_94)
# files_aia_193 = Fido.fetch(query_aia_193)

# -------------------------------
# 2. Query SDO/HMI data
# -------------------------------
# Time range covering the flux emergence and the magnetic field evolution:
# From 2013-07-14T20:00:00 to 2013-07-15T03:00:00.
hmi_time_start = "2013-07-14T20:00:00"
hmi_time_end   = "2013-07-15T03:00:00"

# HMI observes the Fe I absorption line near 6173 Å.
# The wavelength range available is 6173 - 6174 Å.
query_hmi = Fido.search(
    a.Time(hmi_time_start, hmi_time_end),
    a.Instrument("HMI"),
    a.Wavelength(6173*u.AA, 6174*u.AA)
)
print("\nSDO/HMI query results (Fe I 6173 Å):")
print(query_hmi)

# Uncomment the following line to fetch HMI data.
# files_hmi = Fido.fetch(query_hmi)

# -------------------------------
# 3. Query RHESSI data
# -------------------------------
# RHESSI is utilized to capture hard X-ray emissions.
# We focus on the first data collection period: 2013-07-15 from 01:54 UT to 01:56 UT.
rhessi_time_start = "2013-07-15T01:54:00"
rhessi_time_end   = "2013-07-15T01:56:00"

# The RHESSI available wavelength range in the VSO is specified in keV.
# Here we query for the 6–12 keV energy band.
query_rhessi = Fido.search(
    a.Time(rhessi_time_start, rhessi_time_end),
    a.Source("RHESSI"),
    a.Instrument("RHESSI"),
    a.Wavelength(6*u.keV, 12*u.keV)
)
print("\nRHESSI query results (6–12 keV):")
print(query_rhessi)

# Uncomment the following line to fetch RHESSI data.
# files_rhessi = Fido.fetch(query_rhessi)

# End of script

if __name__ == '__main__':
    print("\nQueries completed. Inspect the printed search results above.")
