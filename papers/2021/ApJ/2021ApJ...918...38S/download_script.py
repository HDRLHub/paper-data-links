# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs SunPy VSO queries to obtain data for a solar filament eruption event.
It queries three datasets based on the available VSO interface:

1. SDO/AIA data: Full-disk solar images in multiple wavelengths (94 Å, 211 Å, 171 Å, 193 Å, and 304 Å)
   covering the time period from November 3, 2016 to November 5, 2016.
   
2. SDO/HMI data: Line-of-sight (LOS) magnetograms from SDO/HMI on November 5, 2016.
   
3. SOHO/LASCO C2 data: White-light coronagraph images from SOHO LASCO C2 capturing a CME snapshot
   around 04:36 UT on November 5, 2016 (a narrow time window is used here).

Note: The Fido.fetch commands are provided as comments and will not execute automatically.
"""

# Import necessary modules from sunpy.net and astropy.units.
from sunpy.net import Fido, attrs as a
import astropy.units as u

# -------------------------------
# 1. Query SDO/AIA data
# -------------------------------

# Time range for the filament event observations from SDO/AIA.
start_time_aia = '2016-11-03T00:00:00'
end_time_aia   = '2016-11-05T23:59:59'

# Query for SDO/AIA data at 94 Å
result_aia_94 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(94*u.AA, 94*u.AA)
)
print("SDO/AIA 94 Å Query Results:")
print(result_aia_94)
# To download, uncomment the following line:
# files_aia_94 = Fido.fetch(result_aia_94)

# Query for SDO/AIA data at 211 Å
result_aia_211 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(211*u.AA, 211*u.AA)
)
print("SDO/AIA 211 Å Query Results:")
print(result_aia_211)
# To download, uncomment the following line:
# files_aia_211 = Fido.fetch(result_aia_211)

# Query for SDO/AIA data at 171 Å
result_aia_171 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(171*u.AA, 171*u.AA)
)
print("SDO/AIA 171 Å Query Results:")
print(result_aia_171)
# To download, uncomment the following line:
# files_aia_171 = Fido.fetch(result_aia_171)

# Query for SDO/AIA data at 193 Å
result_aia_193 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(193*u.AA, 193*u.AA)
)
print("SDO/AIA 193 Å Query Results:")
print(result_aia_193)
# To download, uncomment the following line:
# files_aia_193 = Fido.fetch(result_aia_193)

# Query for SDO/AIA data at 304 Å
result_aia_304 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(304*u.AA, 304*u.AA)
)
print("SDO/AIA 304 Å Query Results:")
print(result_aia_304)
# To download, uncomment the following line:
# files_aia_304 = Fido.fetch(result_aia_304)

# -------------------------------
# 2. Query SDO/HMI data (LOS magnetograms)
# -------------------------------

# Time range for SDO/HMI observations on November 5, 2016.
start_time_hmi = '2016-11-05T00:00:00'
end_time_hmi   = '2016-11-05T23:59:59'

result_hmi = Fido.search(
    a.Time(start_time_hmi, end_time_hmi),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print("SDO/HMI LOS magnetic field Query Results:")
print(result_hmi)
# To download, uncomment the following line:
# files_hmi = Fido.fetch(result_hmi)

# -------------------------------
# 3. Query SOHO/LASCO C2 data
# -------------------------------

# LASCO C2 observed a CME around 04:36 UT on November 5, 2016.
# A short time interval is set to capture the event.
start_time_lasco = '2016-11-05T04:30:00'
end_time_lasco   = '2016-11-05T04:40:00'

result_lasco_c2 = Fido.search(
    a.Time(start_time_lasco, end_time_lasco),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("SOHO LASCO C2 Query Results:")
print(result_lasco_c2)
# To download, uncomment the following line:
# files_lasco_c2 = Fido.fetch(result_lasco_c2)

if __name__ == '__main__':
    # Main entry point for script execution.
    pass
