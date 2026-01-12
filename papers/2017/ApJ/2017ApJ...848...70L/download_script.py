# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query 1: SDO HMI line-of-sight (LOS) magnetograms for Carrington Rotation 2098 (2010-06-16 to 2010-07-13)
hmi_los_query = Fido.search(
    a.Time('2010-06-16', '2010-07-13'),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6173 * u.Angstrom)
)
print("HMI LOS Query Results:")
print(hmi_los_query)
# To download the data, uncomment the line below:
# Fido.fetch(hmi_los_query)

# Query 2: SDO HMI vector magnetograms for Carrington Rotation 2098 (2010-06-16 to 2010-07-13)
hmi_vector_query = Fido.search(
    a.Time('2010-06-16', '2010-07-13'),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('vector_magnetic_field'),
    a.Wavelength(6173 * u.Angstrom)
)
print("\nHMI Vector Query Results:")
print(hmi_vector_query)
# To download the data, uncomment the line below:
# Fido.fetch(hmi_vector_query)

# Query 3: SDO AIA 193 Å EUV image for coronal hole detection on 2010-07-08
aia_193_query = Fido.search(
    a.Time('2010-07-08', '2010-07-08'),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Physobs('intensity'),
    a.Wavelength(193 * u.Angstrom)
)
print("\nAIA 193 Å Query Results:")
print(aia_193_query)
# To download the data, uncomment the line below:
# Fido.fetch(aia_193_query)

# Query 4: SOHO MDI line-of-sight (LOS) magnetograms for Carrington Rotation 2098 (2010-06-16 to 2010-07-13)
mdi_los_query = Fido.search(
    a.Time('2010-06-16', '2010-07-13'),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6768 * u.Angstrom)
)
print("\nMDI LOS Query Results:")
print(mdi_los_query)
# To download the data, uncomment the line below:
# Fido.fetch(mdi_los_query)
