# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Query Script
This script searches for data from SDO/AIA, SDO/HMI, and SOHO/LASCO instruments
for the time periods and physical observables used in the study of the 2–4 August 2011 CMEs
and the 4–7 August 2011 ICME events.
"""

import astropy.units as u
from sunpy.net import Fido
import sunpy.net.attrs as a

# ------------------------------------------------------------------------------
# 1. Query SDO/AIA EUV Images for CME1 Formation and DEM Diagnostics
# Time Range: 2011-08-02T05:30 – 2011-08-02T06:10 UT
# Wavelengths: 94, 131, 171, 193, 211, 335 Angstrom
# ------------------------------------------------------------------------------
time_aia = a.Time('2011-08-02 05:30', '2011-08-02 06:10')

# AIA 94 Å
query_aia_94 = Fido.search(
    time_aia,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(94 * u.angstrom)
)
print("AIA 94 Å query results:")
print(query_aia_94)
# Fido.fetch(query_aia_94)

# AIA 131 Å
query_aia_131 = Fido.search(
    time_aia,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(131 * u.angstrom)
)
print("AIA 131 Å query results:")
print(query_aia_131)
# Fido.fetch(query_aia_131)

# AIA 171 Å
query_aia_171 = Fido.search(
    time_aia,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(171 * u.angstrom)
)
print("AIA 171 Å query results:")
print(query_aia_171)
# Fido.fetch(query_aia_171)

# AIA 193 Å
query_aia_193 = Fido.search(
    time_aia,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(193 * u.angstrom)
)
print("AIA 193 Å query results:")
print(query_aia_193)
# Fido.fetch(query_aia_193)

# AIA 211 Å
query_aia_211 = Fido.search(
    time_aia,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(211 * u.angstrom)
)
print("AIA 211 Å query results:")
print(query_aia_211)
# Fido.fetch(query_aia_211)

# AIA 335 Å
query_aia_335 = Fido.search(
    time_aia,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(335 * u.angstrom)
)
print("AIA 335 Å query results:")
print(query_aia_335)
# Fido.fetch(query_aia_335)


# ------------------------------------------------------------------------------
# 2. Query SDO/HMI Vector Magnetograms for MHD Model Boundary Conditions
# Time Range: 2011-07-31T05:00:41 – 2011-08-02T06:00:41 UT
# Observable: Vector magnetic field maps
# ------------------------------------------------------------------------------
time_hmi = a.Time('2011-07-31 05:00:41', '2011-08-02 06:00:41')

query_hmi_vector = Fido.search(
    time_hmi,
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('vector_magnetic_field')
)
print("HMI vector magnetic field query results:")
print(query_hmi_vector)
# Fido.fetch(query_hmi_vector)


# ------------------------------------------------------------------------------
# 3. Query SOHO/LASCO C2 Coronagraph for CME Expansion Observations
# Time Range: 2011-08-02T06:36 – 2011-08-02T07:00 UT
# Detector: C2, Visible/white-light intensity
# ------------------------------------------------------------------------------
time_lasco = a.Time('2011-08-02 06:36', '2011-08-02 07:00')

query_lasco_c2 = Fido.search(
    time_lasco,
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("LASCO C2 query results:")
print(query_lasco_c2)
# Fido.fetch(query_lasco_c2)

# End of script
