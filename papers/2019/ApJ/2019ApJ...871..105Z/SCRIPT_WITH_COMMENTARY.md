# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs Sunpy VSO queries for datasets used in the study of active region NOAA 12268.
The observations span 36 hours from 00:00 UT on January 29, 2015 to 12:00 UT on January 30, 2015.
We query data from:
  • SDO/AIA for multi‐wavelength EUV/UV imaging (1600 Å, 171 Å, and 94 Å),
  • SDO/HMI for photospheric magnetograms (observing the Fe I 6173 Å line), and
  • SOHO/LASCO (C2 detector) for white light coronagraph images (to check for any CME signatures).

Note: ONSET, GONG, and GOES data are not available via the VSO interface provided.
The Fido.fetch commands are commented out so as not to trigger any downloads.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the observation
time_start = "2015-01-29T00:00:00"
time_end = "2015-01-30T12:00:00"

##############################################
# Query 1: SDO/AIA
# We query SDO/AIA data in three channels: 1600 Å, 171 Å, and 94 Å.
# These wavelengths correspond to ultraviolet and extreme-ultraviolet observations of the solar atmosphere.
##############################################

# Build individual wavelength attributes
wavelength_1600 = a.Wavelength(1600*u.Angstrom, 1600*u.Angstrom)
wavelength_171 = a.Wavelength(171*u.Angstrom, 171*u.Angstrom)
wavelength_94  = a.Wavelength(94*u.Angstrom, 94*u.Angstrom)

# Construct the query for SDO/AIA data
aia_query = Fido.search(
    a.Time(time_start, time_end),
    a.Instrument("AIA"),
    # Combine wavelength filters using the OR operator.
    wavelength_1600 | wavelength_171 | wavelength_94
)

# Print the query results for AIA; this shows the search summary.
print("SDO/AIA query results:")
print(aia_query)

# To fetch the data, uncomment the following lines:
# downloaded_aia_files = Fido.fetch(aia_query)
# print("Downloaded AIA files:", downloaded_aia_files)

##############################################
# Query 2: SDO/HMI
# We query SDO/HMI data which observes the Fe I 6173 Å line, important for magnetic field analysis.
##############################################

# Define the wavelength range for the Fe I 6173 Å line observation.
hmi_wavelength = a.Wavelength(6173*u.Angstrom, 6174*u.Angstrom)

# Construct the query for SDO/HMI data.
hmi_query = Fido.search(
    a.Time(time_start, time_end),
    a.Instrument("HMI"),
    hmi_wavelength
)

# Print the query results for HMI.
print("\nSDO/HMI query results:")
print(hmi_query)

# To fetch the data, uncomment the following lines:
# downloaded_hmi_files = Fido.fetch(hmi_query)
# print("Downloaded HMI files:", downloaded_hmi_files)

##############################################
# Query 3: SOHO/LASCO (C2 detector)
# We query SOHO LASCO data with the C2 coronagraph to investigate the presence or absence of CMEs.
##############################################

# Construct the query for SOHO LASCO data using the C2 detector.
lasco_query = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print the query results for LASCO C2.
print("\nSOHO/LASCO (C2) query results:")
print(lasco_query)

# To fetch the data, uncomment the following lines:
# downloaded_lasco_files = Fido.fetch(lasco_query)
# print("Downloaded LASCO C2 files:", downloaded_lasco_files)

if __name__ == '__main__':
    # This ensures that the script can be run as a standalone executable.
    print("\nSunpy VSO Queries constructed successfully.")
