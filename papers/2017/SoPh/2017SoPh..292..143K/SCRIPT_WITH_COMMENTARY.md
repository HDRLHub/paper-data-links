# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# --------------------------------------------------------------------------------
# 1. Query SDO/AIA 304 Å data for the prominence eruption on 16–17 August 2013
# Time range: 2013-08-16 22:50 UT to 2013-08-17 03:00 UT
# Instrument: AIA
# Wavelength: 304 Å
# --------------------------------------------------------------------------------
time_start_aia = "2013-08-16 22:50"
time_end_aia   = "2013-08-17 03:00"
wvl_aia        = 304 * u.angstrom

query_aia = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument('AIA'),
    a.Wavelength(wvl_aia)
)
print("SDO/AIA 304 Å Query Results:")
print(query_aia)
# To download the files, uncomment the following line:
# aia_files = Fido.fetch(query_aia)

# --------------------------------------------------------------------------------
# 2. Query STEREO-B/EUVI 304 Å data for off-limb prominence tracking
# Time range: 2013-08-16 22:50 UT to 2013-08-17 03:00 UT
# Instrument: EUVI
# Source: STEREO_B
# Wavelength: 304 Å
# --------------------------------------------------------------------------------
time_start_euvi = "2013-08-16 22:50"
time_end_euvi   = "2013-08-17 03:00"
wvl_euvi        = 304 * u.angstrom

query_euvi = Fido.search(
    a.Time(time_start_euvi, time_end_euvi),
    a.Source('STEREO_B'),
    a.Instrument('EUVI'),
    a.Wavelength(wvl_euvi)
)
print("\nSTEREO-B/EUVI 304 Å Query Results:")
print(query_euvi)
# To download the files, uncomment the following line:
# euvi_files = Fido.fetch(query_euvi)

# --------------------------------------------------------------------------------
# 3. Query SOHO/LASCO C2 white-light coronagraph data for CME tracking
# Time range: 2013-08-17 01:26 UT to 2013-08-17 15:00 UT
# Instrument: LASCO
# Detector: C2
# --------------------------------------------------------------------------------
time_start_lascoc2 = "2013-08-17 01:26"
time_end_lascoc2   = "2013-08-17 15:00"

query_lascoc2 = Fido.search(
    a.Time(time_start_lascoc2, time_end_lascoc2),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("\nSOHO/LASCO C2 Query Results:")
print(query_lascoc2)
# To download the files, uncomment the following line:
# lascoc2_files = Fido.fetch(query_lascoc2)

# --------------------------------------------------------------------------------
# 4. Query SOHO/LASCO C3 white-light coronagraph data for extended CME propagation
# Time range: 2013-08-17 01:26 UT to 2013-08-17 15:00 UT
# Instrument: LASCO
# Detector: C3
# --------------------------------------------------------------------------------
time_start_lascoc3 = "2013-08-17 01:26"
time_end_lascoc3   = "2013-08-17 15:00"

query_lascoc3 = Fido.search(
    a.Time(time_start_lascoc3, time_end_lascoc3),
    a.Instrument('LASCO'),
    a.Detector('C3')
)
print("\nSOHO/LASCO C3 Query Results:")
print(query_lascoc3)
# To download the files, uncomment the following line:
# lascoc3_files = Fido.fetch(query_lascoc3)

# --------------------------------------------------------------------------------
# 5. Query STEREO-B/SECCHI COR1 polarized-brightness data for early CME structure
# Time range: 2013-08-17 01:30 UT to 2013-08-17 11:00 UT
# Instrument: SECCHI
# Detector: COR1
# Source: STEREO_B
# --------------------------------------------------------------------------------
time_start_cor1 = "2013-08-17 01:30"
time_end_cor1   = "2013-08-17 11:00"

query_cor1 = Fido.search(
    a.Time(time_start_cor1, time_end_cor1),
    a.Source('STEREO_B'),
    a.Instrument('SECCHI'),
    a.Detector('COR1')
)
print("\nSTEREO-B/SECCHI COR1 Query Results:")
print(query_cor1)
# To download the files, uncomment the following line:
# cor1_files = Fido.fetch(query_cor1)

# --------------------------------------------------------------------------------
# 6. Query STEREO-B/SECCHI COR2 polarized-brightness data for later CME evolution
# Time range: 2013-08-17 01:30 UT to 2013-08-17 11:00 UT
# Instrument: SECCHI
# Detector: COR2
# Source: STEREO_B
# --------------------------------------------------------------------------------
time_start_cor2 = "2013-08-17 01:30"
time_end_cor2   = "2013-08-17 11:00"

query_cor2 = Fido.search(
    a.Time(time_start_cor2, time_end_cor2),
    a.Source('STEREO_B'),
    a.Instrument('SECCHI'),
    a.Detector('COR2')
)
print("\nSTEREO-B/SECCHI COR2 Query Results:")
print(query_cor2)
# To download the files, uncomment the following line:
# cor2_files = Fido.fetch(query_cor2)
