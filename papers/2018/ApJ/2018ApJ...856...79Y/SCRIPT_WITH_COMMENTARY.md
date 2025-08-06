# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.map
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define time ranges for queries
# AIA eruption observations on 2017-09-06 from 00:00 to 23:59:59 UT
time_aia = a.Time('2017-09-06 00:00', '2017-09-06 23:59:59')

# HMI observations from 2017-09-05 00:00 to 2017-09-06 23:59:59 UT
time_hmi = a.Time('2017-09-05 00:00', '2017-09-06 23:59:59')

# LASCO C2 observations on 2017-09-06 from 00:00 to 23:59:59 UT
time_lasco = a.Time('2017-09-06 00:00', '2017-09-06 23:59:59')

# -----------------------------------------------------------------------------
# 1. Query SDO/AIA in 304 Å, 171 Å, and 131 Å for flare eruption imaging
# -----------------------------------------------------------------------------
# AIA 304 Å
search_aia_304 = Fido.search(
    time_aia,
    a.Instrument('AIA'),
    a.Wavelength(304 * u.angstrom)
)
print('AIA 304 Å search results:')
print(search_aia_304)
# Fido.fetch(search_aia_304)

# AIA 171 Å
search_aia_171 = Fido.search(
    time_aia,
    a.Instrument('AIA'),
    a.Wavelength(171 * u.angstrom)
)
print('AIA 171 Å search results:')
print(search_aia_171)
# Fido.fetch(search_aia_171)

# AIA 131 Å
search_aia_131 = Fido.search(
    time_aia,
    a.Instrument('AIA'),
    a.Wavelength(131 * u.angstrom)
)
print('AIA 131 Å search results:')
print(search_aia_131)
# Fido.fetch(search_aia_131)

# -----------------------------------------------------------------------------
# 2. Query SDO/HMI for sunspot and magnetic evolution
# -----------------------------------------------------------------------------
# HMI continuum intensity images
search_hmi_cont = Fido.search(
    time_hmi,
    a.Instrument('HMI'),
    a.Physobs('intensity')
)
print('HMI continuum intensity search results:')
print(search_hmi_cont)
# Fido.fetch(search_hmi_cont)

# HMI line-of-sight magnetograms
search_hmi_los = Fido.search(
    time_hmi,
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print('HMI LOS magnetogram search results:')
print(search_hmi_los)
# Fido.fetch(search_hmi_los)

# HMI vector magnetograms
search_hmi_vector = Fido.search(
    time_hmi,
    a.Instrument('HMI'),
    a.Physobs('vector_magnetic_field')
)
print('HMI vector magnetogram search results:')
print(search_hmi_vector)
# Fido.fetch(search_hmi_vector)

# -----------------------------------------------------------------------------
# 3. Query SOHO/LASCO C2 for CME observations
# -----------------------------------------------------------------------------
search_lasco_c2 = Fido.search(
    time_lasco,
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print('LASCO C2 search results:')
print(search_lasco_c2)
# Fido.fetch(search_lasco_c2)
