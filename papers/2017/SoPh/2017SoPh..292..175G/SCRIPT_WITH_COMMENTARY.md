# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Script to query SoHO/EIT and SDO/AIA synoptic EUV data for coronal hole mapping
using Fe XII lines (195 Å for EIT, 193 Å for AIA).
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ------------------------------------------------------------------------
# Query 1: SoHO/EIT Fe XII 195 Å
# Time range covers CRs 1909–2123 (1996 – 2012) as used in the study
time_eit = a.Time('1996-01-01', '2012-12-31')
instrument_eit = a.Instrument('EIT')
wavelength_eit = a.Wavelength(195 * u.Angstrom)

# Perform the search
results_eit = Fido.search(time_eit, instrument_eit, wavelength_eit)
print("SoHO/EIT 195 Å search results:")
print(results_eit)

# Uncomment the following line to download the data:
# files_eit = Fido.fetch(results_eit)

# ------------------------------------------------------------------------
# Query 2: SDO/AIA Fe XII 193 Å
# Time range covers CRs 2124–2190 (2012.42 – 2017.40) as used in the study
time_aia = a.Time('2012-05-11', '2017-04-30')
instrument_aia = a.Instrument('AIA')
wavelength_aia = a.Wavelength(193 * u.Angstrom)

# Perform the search
results_aia = Fido.search(time_aia, instrument_aia, wavelength_aia)
print("SDO/AIA 193 Å search results:")
print(results_aia)

# Uncomment the following line to download the data:
# files_aia = Fido.fetch(results_aia)
