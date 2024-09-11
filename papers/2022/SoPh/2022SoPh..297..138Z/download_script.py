# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query for SDO/AIA
print("Querying SDO/AIA for the prominence eruption...")
aia_query = Fido.search(
    a.Time('2011-06-13T00:50:00', '2011-06-13T01:32:00'),
    a.Instrument('AIA'),
    a.Wavelength(304 * u.Angstrom) | a.Wavelength(131 * u.Angstrom) | 
    a.Wavelength(193 * u.Angstrom) | a.Wavelength(211 * u.Angstrom) | 
    a.Wavelength(171 * u.Angstrom)
)
print(aia_query)
# aia_files = Fido.fetch(aia_query)

# Query for STEREO-B/EUVI
print("Querying STEREO-B/EUVI for the filament eruption...")
euvi_query = Fido.search(
    a.Time('2011-06-13T00:50:00', '2011-06-13T01:32:00'),
    a.Instrument('EUVI'),
    a.Wavelength(304 * u.Angstrom) | a.Wavelength(195 * u.Angstrom),
    a.Source('STEREO_B')
)
print(euvi_query)
# euvi_files = Fido.fetch(euvi_query)

# Query for SOHO/LASCO
print("Querying SOHO/LASCO for the jet-like CME...")
lasco_query = Fido.search(
    a.Time('2011-06-13T01:36:00', '2011-06-13T02:24:00'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print(lasco_query)
# lasco_files = Fido.fetch(lasco_query)

# Query for Fermi/GBM
print("Querying Fermi/GBM for the C1.2 class flare...")
# Note: Fermi/GBM data is not available in VSO, so we skip this query.

# Query for STEREO-B/SWAVES
print("Querying STEREO-B/SWAVES for the type III radio burst...")
swaves_query = Fido.search(
    a.Time('2011-06-13T00:56:00', '2011-06-13T01:14:00'),
    a.Instrument('SWAVES'),
    a.Wavelength(10 * u.MHz, 1 * u.MHz),
    a.Source('STEREO_B')
)
print(swaves_query)
# swaves_files = Fido.fetch(swaves_query)
