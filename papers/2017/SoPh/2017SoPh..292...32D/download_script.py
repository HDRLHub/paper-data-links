# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net as net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# -------------------------------------------------------------------
# Query 1: SOHO/EIT Full-Disk He II 30.4 nm Images
# Time Range: 1996-04-27 to 2015-05-28 (quiet Sun, no flares, processed)
# Wavelength: 304 Å (He II 30.4 nm)
# -------------------------------------------------------------------
eit_time_start = '1996-04-27'
eit_time_end   = '2015-05-28'
eit_query = Fido.search(
    a.Time(eit_time_start, eit_time_end),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(304 * u.angstrom)
)

# Print the EIT search results
print("SOHO/EIT search results for He II 30.4 nm:")
print(eit_query)

# To download, uncomment the following line:
# files_eit = Fido.fetch(eit_query)

# -------------------------------------------------------------------
# Query 2: SDO/AIA Full-Disk He II 30.4 nm Images
# Time Range: 2010-08-26 to 2015-05-28 (overlaps with EIT interval)
# Wavelength: 304 Å (He II 30.4 nm)
# -------------------------------------------------------------------
aia_time_start = '2010-08-26'
aia_time_end   = '2015-05-28'
aia_query = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(304 * u.angstrom)
)

# Print the AIA search results
print("SDO/AIA search results for He II 30.4 nm:")
print(aia_query)

# To download, uncomment the following line:
# files_aia = Fido.fetch(aia_query)
