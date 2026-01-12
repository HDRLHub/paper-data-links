# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ------------------------------------------------------------------------------
# 1. SDO/AIA Data for Filament Activation and Partial Eruption Phase
#    Time Range: 2015-03-14 11:00 – 2015-03-14 13:00 UT
#    Wavelengths: 193 Å and 304 Å
# ------------------------------------------------------------------------------
# AIA 193 Å
query_aia_193_step1 = Fido.search(
    a.Time('2015-03-14 11:00', '2015-03-14 13:00'),
    a.Instrument('AIA'),
    a.Wavelength(193 * u.angstrom)
)
print("AIA 193 Å (2015-03-14 11:00–13:00) results:", query_aia_193_step1)
# Fido.fetch(query_aia_193_step1)

# AIA 304 Å
query_aia_304_step1 = Fido.search(
    a.Time('2015-03-14 11:00', '2015-03-14 13:00'),
    a.Instrument('AIA'),
    a.Wavelength(304 * u.angstrom)
)
print("AIA 304 Å (2015-03-14 11:00–13:00) results:", query_aia_304_step1)
# Fido.fetch(query_aia_304_step1)

# ------------------------------------------------------------------------------
# 2. SDO/AIA Data for Quasi-Equilibrium Phase and Full Eruption
#    Time Range: 2015-03-14 13:00 – 2015-03-15 00:45 UT
#    Wavelengths: 193 Å and 304 Å
# ------------------------------------------------------------------------------
# AIA 193 Å
query_aia_193_step2 = Fido.search(
    a.Time('2015-03-14 13:00', '2015-03-15 00:45'),
    a.Instrument('AIA'),
    a.Wavelength(193 * u.angstrom)
)
print("AIA 193 Å (2015-03-14 13:00–03-15 00:45) results:", query_aia_193_step2)
# Fido.fetch(query_aia_193_step2)

# AIA 304 Å
query_aia_304_step2 = Fido.search(
    a.Time('2015-03-14 13:00', '2015-03-15 00:45'),
    a.Instrument('AIA'),
    a.Wavelength(304 * u.angstrom)
)
print("AIA 304 Å (2015-03-14 13:00–03-15 00:45) results:", query_aia_304_step2)
# Fido.fetch(query_aia_304_step2)

# ------------------------------------------------------------------------------
# 3. SDO/AIA Data for Time–Distance Analysis of Filament Dynamics
#    Time Range: 2015-03-14 12:00 – 2015-03-15 02:00 UT
#    Wavelength: 193 Å
# ------------------------------------------------------------------------------
query_aia_193_timedist = Fido.search(
    a.Time('2015-03-14 12:00', '2015-03-15 02:00'),
    a.Instrument('AIA'),
    a.Wavelength(193 * u.angstrom)
)
print("AIA 193 Å (2015-03-14 12:00–03-15 02:00) results:", query_aia_193_timedist)
# Fido.fetch(query_aia_193_timedist)

# ------------------------------------------------------------------------------
# 4. SDO/HMI Magnetic Field Data for Decay Index Calculation
#    Time Snapshot: 2015-03-14 15:00 UT
#    Observable: Line-of-sight Magnetic Field
# ------------------------------------------------------------------------------
query_hmi_los = Fido.search(
    a.Time('2015-03-14 15:00', '2015-03-14 15:00'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print("HMI LOS Magnetic Field (2015-03-14 15:00) results:", query_hmi_los)
# Fido.fetch(query_hmi_los)

# ------------------------------------------------------------------------------
# 5. SOHO/LASCO Coronagraph Data for CME Detection and Evolution
#    a) Partial CME on 14 March 2015 at ≈13:30 UT in C2
#    b) Main CME on 15 March 2015 at 01:48 UT in C2 and C3
# ------------------------------------------------------------------------------
# LASCO C2 – Partial CME on 2015-03-14
query_lasco_c2_pre = Fido.search(
    a.Time('2015-03-14 13:30', '2015-03-14 14:00'),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Physobs('intensity')
)
print("LASCO C2 Partial CME (2015-03-14 13:30–14:00) results:", query_lasco_c2_pre)
# Fido.fetch(query_lasco_c2_pre)

# LASCO C2 – Main CME on 2015-03-15
query_lasco_c2_main = Fido.search(
    a.Time('2015-03-15 01:48', '2015-03-15 03:00'),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Physobs('intensity')
)
print("LASCO C2 Main CME (2015-03-15 01:48–03:00) results:", query_lasco_c2_main)
# Fido.fetch(query_lasco_c2_main)

# LASCO C3 – Main CME on 2015-03-15
query_lasco_c3_main = Fido.search(
    a.Time('2015-03-15 01:48', '2015-03-15 06:00'),
    a.Instrument('LASCO'),
    a.Detector('C3'),
    a.Physobs('intensity')
)
print("LASCO C3 Main CME (2015-03-15 01:48–06:00) results:", query_lasco_c3_main)
# Fido.fetch(query_lasco_c3_main)

print("All queries complete. Uncomment the fetch commands to download the data.")
