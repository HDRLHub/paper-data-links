# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define time ranges around the SOL20120510T04:18 UT flare event.

# 1. HMI vector magnetic field before flare onset
hmi_start = '2012-05-10T04:06:00'
hmi_end   = '2012-05-10T04:18:00'

# 2. AIA 1600 Å imaging around flare peak
aia_start = '2012-05-10T04:07:00'
aia_end   = '2012-05-10T04:21:00'

# 3. LASCO-C2 coronagraph for CME association
lasco_start = '2012-05-10T04:00:00'
lasco_end   = '2012-05-10T05:00:00'

# 4. STEREO-B COR1 coronagraph to fill LASCO coverage gap
secchi_start = '2012-05-10T04:00:00'
secchi_end   = '2012-05-10T05:00:00'


# -----------------------------------------------------------------------
# Query 1: HMI vector magnetic field (hmi.B_720s) at 6173 Å
# -----------------------------------------------------------------------
hmi_query = Fido.search(
    a.Time(hmi_start, hmi_end),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('vector_magnetic_field'),
    a.Wavelength(6173.0 * u.Angstrom)
)
print('HMI vector magnetic field search results:')
print(hmi_query)


# -----------------------------------------------------------------------
# Query 2: AIA 1600 Å images for flare ribbons and UV emission
# -----------------------------------------------------------------------
aia_query = Fido.search(
    a.Time(aia_start, aia_end),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(1600.0 * u.Angstrom),
    a.Physobs('intensity')
)
print('AIA 1600 Å search results:')
print(aia_query)


# -----------------------------------------------------------------------
# Query 3: LASCO-C2 white-light coronagraph images for CME association
# -----------------------------------------------------------------------
lasco_query = Fido.search(
    a.Time(lasco_start, lasco_end),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Physobs('intensity')
)
print('LASCO-C2 search results:')
print(lasco_query)


# -----------------------------------------------------------------------
# Query 4: STEREO-B SECCHI COR1 white-light coronagraph images
# -----------------------------------------------------------------------
secchi_query = Fido.search(
    a.Time(secchi_start, secchi_end),
    a.Source('STEREO_B'),
    a.Instrument('SECCHI'),
    a.Detector('COR1'),
    a.Physobs('intensity')
)
print('STEREO-B COR1 search results:')
print(secchi_query)


# -----------------------------------------------------------------------
# Uncomment the following lines to fetch the data to local directories
# -----------------------------------------------------------------------
# Fido.fetch(hmi_query, path='data/hmi/')
# Fido.fetch(aia_query, path='data/aia_1600/')
# Fido.fetch(lasco_query, path='data/lasco_c2/')
# Fido.fetch(secchi_query, path='data/secchi_cor1/')
