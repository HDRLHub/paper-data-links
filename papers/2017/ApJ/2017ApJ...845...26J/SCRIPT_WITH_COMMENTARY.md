# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Script to query VSO for SDO/AIA, SDO/HMI, RHESSI, and SOHO/LASCO data
for the 2014-12-18 eruptive event from AR NOAA 12241.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# -----------------------------------------------------------------------------
# 1. SDO/AIA data for 2014-12-18 21:30 – 2014-12-19 02:00 UT
#    EUV channels: 304, 131, 171, 193, 211, 335, 94 Å
#    UV channels: 1600, 1700 Å
#    Visible: 4500 Å
# -----------------------------------------------------------------------------
time_aia = a.Time('2014-12-18 21:30', '2014-12-19 02:00')

# AIA 304 Å
query_aia_304 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(304 * u.Angstrom))
print(query_aia_304)
# Fido.fetch(query_aia_304)

# AIA 131 Å
query_aia_131 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(131 * u.Angstrom))
print(query_aia_131)
# Fido.fetch(query_aia_131)

# AIA 171 Å
query_aia_171 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(171 * u.Angstrom))
print(query_aia_171)
# Fido.fetch(query_aia_171)

# AIA 193 Å
query_aia_193 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(193 * u.Angstrom))
print(query_aia_193)
# Fido.fetch(query_aia_193)

# AIA 211 Å
query_aia_211 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(211 * u.Angstrom))
print(query_aia_211)
# Fido.fetch(query_aia_211)

# AIA 335 Å
query_aia_335 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(335 * u.Angstrom))
print(query_aia_335)
# Fido.fetch(query_aia_335)

# AIA 94 Å
query_aia_94 = Fido.search(time_aia,
                           a.Instrument('AIA'),
                           a.Wavelength(94 * u.Angstrom))
print(query_aia_94)
# Fido.fetch(query_aia_94)

# AIA 1600 Å
query_aia_1600 = Fido.search(time_aia,
                             a.Instrument('AIA'),
                             a.Wavelength(1600 * u.Angstrom))
print(query_aia_1600)
# Fido.fetch(query_aia_1600)

# AIA 1700 Å
query_aia_1700 = Fido.search(time_aia,
                             a.Instrument('AIA'),
                             a.Wavelength(1700 * u.Angstrom))
print(query_aia_1700)
# Fido.fetch(query_aia_1700)

# AIA 4500 Å (visible)
query_aia_4500 = Fido.search(time_aia,
                             a.Instrument('AIA'),
                             a.Wavelength(4500 * u.Angstrom))
print(query_aia_4500)
# Fido.fetch(query_aia_4500)

# -----------------------------------------------------------------------------
# 2. SDO/HMI LOS magnetograms for 2014-12-18 20:15 – 2014-12-18 22:00 UT
#    Fe I 6173 Å line-of-sight magnetic field
# -----------------------------------------------------------------------------
time_hmi = a.Time('2014-12-18 20:15', '2014-12-18 22:00')
query_hmi_los = Fido.search(time_hmi,
                            a.Instrument('HMI'),
                            a.Wavelength(6173 * u.Angstrom),
                            a.Physobs('LOS_magnetic_field'))
print(query_hmi_los)
# Fido.fetch(query_hmi_los)

# -----------------------------------------------------------------------------
# 3. RHESSI hard X-ray imaging for 2014-12-18 21:41 – 2014-12-18 22:10 UT
#    Energy range 25–50 keV
# -----------------------------------------------------------------------------
time_rhessi = a.Time('2014-12-18 21:41', '2014-12-18 22:10')
query_rhessi = Fido.search(time_rhessi,
                           a.Instrument('RHESSI'),
                           a.Wavelength(25 * u.keV, 50 * u.keV))
print(query_rhessi)
# Fido.fetch(query_rhessi)

# -----------------------------------------------------------------------------
# 4. SOHO/LASCO C2 white-light coronagraph at 2014-12-19 01:04:42 UT
# -----------------------------------------------------------------------------
time_lasco = a.Time('2014-12-19 01:04:42', '2014-12-19 01:04:42')
query_lasco_c2 = Fido.search(time_lasco,
                             a.Instrument('LASCO'),
                             a.Detector('C2'))
print(query_lasco_c2)
# Fido.fetch(query_lasco_c2)

# -----------------------------------------------------------------------------
# Note: GOES X-ray time profiles (1–8 Å, 0.5–4 Å) are not available via the
#       provided VSO interface. Use SunPy TimeSeries:
#       from sunpy.timeseries import TimeSeries
#       ts = TimeSeries('goes://')
# -----------------------------------------------------------------------------
