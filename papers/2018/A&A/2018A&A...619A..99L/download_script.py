# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
import astropy.units as u
from sunpy.net import Fido, attrs as a

# -------------------------------------------------------------------
# Query 1: SOHO/MDI Medium-ℓ Dopplergrams (LoS Velocity)
# Time range: 1996-05-01 to 2010-04-30
# Physobs: LOS_velocity, Wavelength: Ni I 6768 Å
# -------------------------------------------------------------------
mdi_time_start = '1996-05-01'
mdi_time_end   = '2010-04-30'

mdi_search = Fido.search(
    a.Time(mdi_time_start, mdi_time_end),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_velocity'),
    a.Wavelength(6768 * u.Angstrom)
)

print("SOHO/MDI LOS Velocity Search Results:")
print(mdi_search)

# To download the MDI data, uncomment the following line:
# fetched_mdi = Fido.fetch(mdi_search)


# -------------------------------------------------------------------
# Query 2: SDO/HMI Medium-ℓ Dopplergrams (LoS Velocity)
# Time range: 2010-05-01 to 2017-04-30
# Physobs: LOS_velocity, Wavelength: Fe I 6173 Å
# -------------------------------------------------------------------
hmi_time_start = '2010-05-01'
hmi_time_end   = '2017-04-30'

hmi_search = Fido.search(
    a.Time(hmi_time_start, hmi_time_end),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_velocity'),
    a.Wavelength(6173 * u.Angstrom)
)

print("SDO/HMI LOS Velocity Search Results:")
print(hmi_search)

# To download the HMI data, uncomment the following line:
# fetched_hmi = Fido.fetch(hmi_search)
