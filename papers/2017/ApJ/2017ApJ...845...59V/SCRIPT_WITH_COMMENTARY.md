# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a
from sunpy.time import parse_time

# Define the overall time range for AR NOAA 12371 disk passage and CME events
tstart = parse_time('2015-06-18T00:00:00')
tend   = parse_time('2015-06-25T23:59:59')

# -------------------------------------------------------------------
# 1. Query SDO/HMI vector magnetic field data (Fe I 6173 Å)
# -------------------------------------------------------------------
query_hmi_vector = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('vector_magnetic_field'),
    a.Wavelength(6173.0 * u.Angstrom)
)
print("HMI Vector Magnetic Field Query Results:")
print(query_hmi_vector)
# To download the data, uncomment the next line:
# Fido.fetch(query_hmi_vector)

# -------------------------------------------------------------------
# 2. Query SDO/HMI line-of-sight magnetic field data (Fe I 6173 Å)
# -------------------------------------------------------------------
query_hmi_los = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6173.0 * u.Angstrom)
)
print("HMI LOS Magnetic Field Query Results:")
print(query_hmi_los)
# To download the data, uncomment the next line:
# Fido.fetch(query_hmi_los)

# -------------------------------------------------------------------
# 3. Query SDO/AIA EUV and UV imaging data for key wavelengths
#    (94, 131, 193, 335, 304, 1600, 171 Å)
# -------------------------------------------------------------------
query_aia_94 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(94.0 * u.Angstrom)
)
print("AIA 94 Å Query Results:")
print(query_aia_94)
# Fido.fetch(query_aia_94)

query_aia_131 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(131.0 * u.Angstrom)
)
print("AIA 131 Å Query Results:")
print(query_aia_131)
# Fido.fetch(query_aia_131)

query_aia_193 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(193.0 * u.Angstrom)
)
print("AIA 193 Å Query Results:")
print(query_aia_193)
# Fido.fetch(query_aia_193)

query_aia_335 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(335.0 * u.Angstrom)
)
print("AIA 335 Å Query Results:")
print(query_aia_335)
# Fido.fetch(query_aia_335)

query_aia_304 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(304.0 * u.Angstrom)
)
print("AIA 304 Å Query Results:")
print(query_aia_304)
# Fido.fetch(query_aia_304)

query_aia_1600 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(1600.0 * u.Angstrom)
)
print("AIA 1600 Å Query Results:")
print(query_aia_1600)
# Fido.fetch(query_aia_1600)

query_aia_171 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(171.0 * u.Angstrom)
)
print("AIA 171 Å Query Results:")
print(query_aia_171)
# Fido.fetch(query_aia_171)

# -------------------------------------------------------------------
# 4. Query SOHO/LASCO white-light coronagraph data for C2 and C3
# -------------------------------------------------------------------
query_lasco_c2 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("LASCO C2 Query Results:")
print(query_lasco_c2)
# Fido.fetch(query_lasco_c2)

query_lasco_c3 = Fido.search(
    a.Time(tstart, tend),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C3')
)
print("LASCO C3 Query Results:")
print(query_lasco_c3)
# Fido.fetch(query_lasco_c3)

print("All queries completed.")
