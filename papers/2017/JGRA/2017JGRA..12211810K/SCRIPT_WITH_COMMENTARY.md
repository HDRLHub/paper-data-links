# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Query SOHO/EIT 195 Å data for source region identification (2007-11-01 to 2014-06-30)
time_eit = a.Time('2007-11-01', '2014-06-30')
query_eit = Fido.search(
    time_eit,
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(195 * u.angstrom)
)
print("SOHO/EIT 195 Å search results:")
print(query_eit)
# Fido.fetch(query_eit)

# Query SDO/AIA 171 Å data for EUV source region context (2010-05-12 to 2014-06-30)
time_aia = a.Time('2010-05-12', '2014-06-30')
query_aia_171 = Fido.search(
    time_aia,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(171 * u.angstrom)
)
print("\nSDO/AIA 171 Å search results:")
print(query_aia_171)
# Fido.fetch(query_aia_171)

# Query SDO/AIA 193 Å data for EUV source region context (2010-05-12 to 2014-06-30)
query_aia_193 = Fido.search(
    time_aia,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(193 * u.angstrom)
)
print("\nSDO/AIA 193 Å search results:")
print(query_aia_193)
# Fido.fetch(query_aia_193)

# Query SDO/HMI line-of-sight magnetic field (post-May 2010) for polarity inversion lines
time_hmi = a.Time('2010-05-01', '2014-06-30')
query_hmi = Fido.search(
    time_hmi,
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print("\nSDO/HMI LOS magnetic field search results:")
print(query_hmi)
# Fido.fetch(query_hmi)

# Query SOHO/MDI line-of-sight magnetic field (pre-May 2010) for polarity inversion lines
time_mdi = a.Time('2007-11-01', '2010-05-01')
query_mdi = Fido.search(
    time_mdi,
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field')
)
print("\nSOHO/MDI LOS magnetic field search results:")
print(query_mdi)
# Fido.fetch(query_mdi)

# Query SOHO/LASCO C2 white-light coronagraph images for CME identification and velocity/mass (2007-11-01 to 2014-06-30)
time_lasco = a.Time('2007-11-01', '2014-06-30')
query_lasco_c2 = Fido.search(
    time_lasco,
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("\nSOHO/LASCO C2 coronagraph search results:")
print(query_lasco_c2)
# Fido.fetch(query_lasco_c2)
