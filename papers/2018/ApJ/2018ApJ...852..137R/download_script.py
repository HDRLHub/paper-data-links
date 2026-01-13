# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query 1: SOHO/MDI full-disk line-of-sight magnetic field
# Time range: 1996-07-01 to 2011-04-12 (MDI data available until 2011-04-12)
mdi_query = Fido.search(
    a.Time('1996-07-01', '2011-04-12'),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field')
)
print("MDI Query Results:")
print(mdi_query)
# Uncomment to download: files_mdi = Fido.fetch(mdi_query)

# Query 2: SDO/HMI full-disk line-of-sight magnetic field
# Time range: 2010-05-01 to 2015-02-05 (HMI data from May 2010 onward)
hmi_query = Fido.search(
    a.Time('2010-05-01', '2015-02-05'),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print("\nHMI Query Results:")
print(hmi_query)
# Uncomment to download: files_hmi = Fido.fetch(hmi_query)

# Query 3: SDO/EVE solar spectral irradiance (intensity)
# Time range: 2010-07-01 to 2012-07-31 (short-term SSI comparison period)
eve_query = Fido.search(
    a.Time('2010-07-01', '2012-07-31'),
    a.Source('SDO'),
    a.Instrument('EVE'),
    a.Physobs('intensity')
)
print("\nEVE Query Results:")
print(eve_query)
# Uncomment to download: files_eve = Fido.fetch(eve_query)

# Query 4: SDO/AIA EUV full-disk intensity at 19.3 nm (193 Å)
# Time range: 2010-07-01 to 2012-07-31
aia_193_query = Fido.search(
    a.Time('2010-07-01', '2012-07-31'),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Physobs('intensity'),
    a.Wavelength(193 * u.Angstrom)
)
print("\nAIA 193 Å Query Results:")
print(aia_193_query)
# Uncomment to download: files_aia_193 = Fido.fetch(aia_193_query)

# Query 5: SDO/AIA EUV full-disk intensity at 21.1 nm (211 Å)
# Time range: 2010-07-01 to 2012-07-31
aia_211_query = Fido.search(
    a.Time('2010-07-01', '2012-07-31'),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Physobs('intensity'),
    a.Wavelength(211 * u.Angstrom)
)
print("\nAIA 211 Å Query Results:")
print(aia_211_query)
# Uncomment to download: files_aia_211 = Fido.fetch(aia_211_query)

# Query 6: SOHO/EIT EUV images at 19.5 nm (195 Å) for spatial validation
# Date: 2001-12-15
eit_dec2001_query = Fido.search(
    a.Time('2001-12-15', '2001-12-15'),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Physobs('intensity'),
    a.Wavelength(195 * u.Angstrom)
)
print("\nEIT 2001-12-15 Query Results:")
print(eit_dec2001_query)
# Uncomment to download: files_eit_dec2001 = Fido.fetch(eit_dec2001_query)

# Query 7: SOHO/EIT EUV images at 19.5 nm (195 Å) for spatial validation
# Date: 2003-11-15
eit_nov2003_query = Fido.search(
    a.Time('2003-11-15', '2003-11-15'),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Physobs('intensity'),
    a.Wavelength(195 * u.Angstrom)
)
print("\nEIT 2003-11-15 Query Results:")
print(eit_nov2003_query)
# Uncomment to download: files_eit_nov2003 = Fido.fetch(eit_nov2003_query)

# Note: TIMED/SEE Solar Spectral Irradiance data (19.3 nm, 21.1 nm) is not available via VSO.
