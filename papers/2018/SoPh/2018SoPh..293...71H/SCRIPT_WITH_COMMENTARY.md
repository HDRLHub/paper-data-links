# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs a series of SunPy VSO queries which mirror the data used
in the study on automated identification of coronal holes (CHs) using EUV synoptic maps
and magnetic field measurements. The queries target:

1. SOHO/EIT EUV intensity maps at wavelengths 195 Å, 171 Å, and 304 Å during
   the first EIT period (CR 1911 to CR 2055).
2. SDO/AIA EUV intensity maps at wavelengths 193 Å, 171 Å, and 304 Å covering
   the period from CR 2097 to CR 2186.
3. SOHO/MDI magnetic field (LOS_magnetic_field) observations for the period
   covering the EIT era.
4. SDO/HMI magnetic field (LOS_magnetic_field) measurements contemporaneous
   with the AIA observations.

Note:
- The Fido.fetch commands are commented out.
- Each query is constructed explicitly with its own parameters.
- The only required values used are the time range and instrument as specified.
"""

# Import required modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ---------------------------
# 1. SOHO/EIT EUV Intensity Data Query (EIT-1 Period)
# ---------------------------
# Define time range corresponding to CR 1911 (June 28, 1996) to CR 2055 (March 31, 2007)
eit_start_time = '1996-06-28'
eit_end_time   = '2007-03-31'
# SOHO/EIT observes at several wavelengths, we choose three key ones used in the study:
eit_wavelengths = [195*u.Angstrom, 171*u.Angstrom, 304*u.Angstrom]

# Query for each wavelength separately for clarity in our script.
print("Querying SOHO/EIT EUV intensity data:")
print("------------------------------------------------")

# Query for 195 Å data
eit_195_query = Fido.search(
    a.Time(eit_start_time, eit_end_time),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(195*u.Angstrom, 195*u.Angstrom),
    a.Physobs('intensity')
)
print("SOHO/EIT 195 Å query results:")
print(eit_195_query)
# Uncomment the following line to fetch the data:
# files_eit_195 = Fido.fetch(eit_195_query)

# Query for 171 Å data
eit_171_query = Fido.search(
    a.Time(eit_start_time, eit_end_time),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(171*u.Angstrom, 171*u.Angstrom),
    a.Physobs('intensity')
)
print("SOHO/EIT 171 Å query results:")
print(eit_171_query)
# Uncomment the following line to fetch the data:
# files_eit_171 = Fido.fetch(eit_171_query)

# Query for 304 Å data
eit_304_query = Fido.search(
    a.Time(eit_start_time, eit_end_time),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(304*u.Angstrom, 304*u.Angstrom),
    a.Physobs('intensity')
)
print("SOHO/EIT 304 Å query results:")
print(eit_304_query)
# Uncomment the following line to fetch the data:
# files_eit_304 = Fido.fetch(eit_304_query)

# ---------------------------
# 2. SDO/AIA EUV Intensity Data Query (CR 2097 to CR 2186)
# ---------------------------
# Define the time range corresponding to May 20, 2010 to January 10, 2017.
aia_start_time = '2010-05-20'
aia_end_time   = '2017-01-10'
# Select wavelengths used in the study: 193 Å (within the range 191-195 Å), 171 Å, and 304 Å.
aia_wavelengths = [193*u.Angstrom, 171*u.Angstrom, 304*u.Angstrom]

print("\nQuerying SDO/AIA EUV intensity data:")
print("------------------------------------------------")

# Query for 193 Å data
aia_193_query = Fido.search(
    a.Time(aia_start_time, aia_end_time),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(193*u.Angstrom, 193*u.Angstrom),
    a.Physobs('intensity')
)
print("SDO/AIA 193 Å query results:")
print(aia_193_query)
# Uncomment the following line to fetch the data:
# files_aia_193 = Fido.fetch(aia_193_query)

# Query for 171 Å data
aia_171_query = Fido.search(
    a.Time(aia_start_time, aia_end_time),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(171*u.Angstrom, 171*u.Angstrom),
    a.Physobs('intensity')
)
print("SDO/AIA 171 Å query results:")
print(aia_171_query)
# Uncomment the following line to fetch the data:
# files_aia_171 = Fido.fetch(aia_171_query)

# Query for 304 Å data
aia_304_query = Fido.search(
    a.Time(aia_start_time, aia_end_time),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(304*u.Angstrom, 304*u.Angstrom),
    a.Physobs('intensity')
)
print("SDO/AIA 304 Å query results:")
print(aia_304_query)
# Uncomment the following line to fetch the data:
# files_aia_304 = Fido.fetch(aia_304_query)

# ---------------------------
# 3. SOHO/MDI Magnetic Field Data Query
# ---------------------------
# The study uses synoptic magnetic field maps to distinguish coronal holes from filament channels.
# Query the LOS magnetic field observed by SOHO/MDI during the period covering the EUV observation era.
mdi_start_time = '1996-06-28'
mdi_end_time   = '2010-10-03'

print("\nQuerying SOHO/MDI magnetic field data:")
print("------------------------------------------------")

mdi_query = Fido.search(
    a.Time(mdi_start_time, mdi_end_time),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Detector('MDI'),
    a.Wavelength(6768*u.Angstrom, 6768*u.Angstrom),  # Provided wavelength for MDI observations
    a.Physobs('LOS_magnetic_field')
)
print("SOHO/MDI LOS magnetic field query results:")
print(mdi_query)
# Uncomment the following line to fetch the data:
# files_mdi = Fido.fetch(mdi_query)

# ---------------------------
# 4. SDO/HMI Magnetic Field Data Query
# ---------------------------
# For the later period, SDO/HMI provides the photospheric magnetic field measurements.
hmi_start_time = '2010-05-20'
hmi_end_time   = '2017-01-10'

print("\nQuerying SDO/HMI magnetic field data:")
print("------------------------------------------------")

hmi_query = Fido.search(
    a.Time(hmi_start_time, hmi_end_time),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print("SDO/HMI LOS magnetic field query results:")
print(hmi_query)
# Uncomment the following line to fetch the data:
# files_hmi = Fido.fetch(hmi_query)

print("\nAll queries completed. Review the printed query results above.")
    
if __name__ == '__main__':
    pass
