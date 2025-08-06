# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for all queries: June 1, 2010 to November 30, 2016
start_time = '2010-06-01 00:00'
end_time   = '2016-11-30 23:59'

# -----------------------------------------------------------------------------
# Part 1: Query SDO/AIA EUV data for six coronal wavelengths (94, 131, 171, 193, 211, 335 Å)
# -----------------------------------------------------------------------------

# 1) AIA 94 Å channel
print("Searching for SDO/AIA 94 Å data...")
aia_94 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(94.0 * u.Angstrom)
)
print(aia_94)
# Uncomment the next line to download the data:
# Fido.fetch(aia_94)

# 2) AIA 131 Å channel
print("Searching for SDO/AIA 131 Å data...")
aia_131 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(131.0 * u.Angstrom)
)
print(aia_131)
# Fido.fetch(aia_131)

# 3) AIA 171 Å channel
print("Searching for SDO/AIA 171 Å data...")
aia_171 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(171.0 * u.Angstrom)
)
print(aia_171)
# Fido.fetch(aia_171)

# 4) AIA 193 Å channel
print("Searching for SDO/AIA 193 Å data...")
aia_193 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(193.0 * u.Angstrom)
)
print(aia_193)
# Fido.fetch(aia_193)

# 5) AIA 211 Å channel
print("Searching for SDO/AIA 211 Å data...")
aia_211 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(211.0 * u.Angstrom)
)
print(aia_211)
# Fido.fetch(aia_211)

# 6) AIA 335 Å channel
print("Searching for SDO/AIA 335 Å data...")
aia_335 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(335.0 * u.Angstrom)
)
print(aia_335)
# Fido.fetch(aia_335)

# -----------------------------------------------------------------------------
# Part 2: Query SOHO/LASCO white-light coronagraph data (C2 detector)
# -----------------------------------------------------------------------------

print("Searching for SOHO/LASCO C2 white-light data...")
lasco_c2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print(lasco_c2)
# Fido.fetch(lasco_c2)

print("All queries complete.")
