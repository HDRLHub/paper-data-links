# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query 1: SOHO/MDI LOS magnetic field for AR 10486 during Carrington Rotation 2009
time_cr2009_start = '2003-10-24T15:58:00'
time_cr2009_end   = '2003-11-02T18:45:00'

query_cr2009 = Fido.search(
    a.Time(time_cr2009_start, time_cr2009_end),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6768.0 * u.Angstrom)
)

print("Search results for CR2009 (2003-10-24 15:58 to 2003-11-02 18:45):")
print(query_cr2009)

# Query 2: SOHO/MDI LOS magnetic field for AR 10486 during Carrington Rotation 2010
time_cr2010_start = '2003-11-20T23:22:00'
time_cr2010_end   = '2003-11-30T02:11:00'

query_cr2010 = Fido.search(
    a.Time(time_cr2010_start, time_cr2010_end),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6768.0 * u.Angstrom)
)

print("Search results for CR2010 (2003-11-20 23:22 to 2003-11-30 02:11):")
print(query_cr2010)

# To download the files, uncomment the lines below:
# files_cr2009 = Fido.fetch(query_cr2009)
# files_cr2010 = Fido.fetch(query_cr2010)
