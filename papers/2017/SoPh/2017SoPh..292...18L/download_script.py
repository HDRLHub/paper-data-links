# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
SunPy VSO Queries for Coronal Hole Study (1996–2014)

This script searches for:
 1. SOHO/EIT 195 Å EUV images (1996-05-31 to 2010-12-31)
 2. SOHO/MDI LOS magnetic field maps (1996-06-28 to 2010-11-26)
 3. SDO/AIA 193 Å EUV images (2010-05-13 to 2014-08-19)
 4. SDO/HMI LOS magnetic field maps (2010-04-22 to 2014-10-14)

STEREO/EUVI A/B is not available in the provided VSO interface.
"""

import astropy.units as u
from sunpy.net import Fido
import sunpy.net.attrs as a

# ------------------------------------------------------------------------
# 1. Query SOHO/EIT 195 Å data (EUV coronal hole detection, Cycle 23)
# ------------------------------------------------------------------------
time_eit_start = '1996-05-31 00:00'
time_eit_end   = '2010-12-31 23:59'
query_eit = Fido.search(
    a.Time(time_eit_start, time_eit_end),
    a.vso.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(195.0 * u.Angstrom)
)
print("SOHO/EIT 195Å query results:")
print(query_eit)
# fetched_eit = Fido.fetch(query_eit)  # Uncomment to download SOHO/EIT data

# ------------------------------------------------------------------------
# 2. Query SOHO/MDI LOS magnetic field (photospheric flux, Cycle 23)
# ------------------------------------------------------------------------
time_mdi_start = '1996-06-28 00:00'
time_mdi_end   = '2010-11-26 23:59'
query_mdi = Fido.search(
    a.Time(time_mdi_start, time_mdi_end),
    a.vso.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6768.0 * u.Angstrom)
)
print("\nSOHO/MDI LOS magnetic field query results:")
print(query_mdi)
# fetched_mdi = Fido.fetch(query_mdi)  # Uncomment to download SOHO/MDI data

# ------------------------------------------------------------------------
# 3. Query SDO/AIA 193 Å data (EUV coronal hole detection, Cycle 24)
# ------------------------------------------------------------------------
time_aia_start = '2010-05-13 00:00'
time_aia_end   = '2014-08-19 23:59'
query_aia = Fido.search(
    a.Time(time_aia_start, time_aia_end),
    a.vso.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(193.0 * u.Angstrom)
)
print("\nSDO/AIA 193Å query results:")
print(query_aia)
# fetched_aia = Fido.fetch(query_aia)  # Uncomment to download SDO/AIA data

# ------------------------------------------------------------------------
# 4. Query SDO/HMI LOS magnetic field (photospheric flux, Cycle 24)
# ------------------------------------------------------------------------
time_hmi_start = '2010-04-22 00:00'
time_hmi_end   = '2014-10-14 23:59'
query_hmi = Fido.search(
    a.Time(time_hmi_start, time_hmi_end),
    a.vso.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6173.0 * u.Angstrom)
)
print("\nSDO/HMI LOS magnetic field query results:")
print(query_hmi)
# fetched_hmi = Fido.fetch(query_hmi)  # Uncomment to download SDO/HMI data

# ------------------------------------------------------------------------
# Note on STEREO/EUVI A/B
# ------------------------------------------------------------------------
print("\nNote: STEREO/EUVI A/B is not available in the provided VSO interface.")
