# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Query Script for Solar Chromospheric and UV Data

This script performs two separate VSO searches:
1) SOLIS/ISS Ca II K 1-Å index between 2015-10-01 and 2016-12-31.
2) SORCE/SOLSTICE far-UV irradiance (200–280 nm) between 2003-01-01 and 2016-12-31.

Note:
- TIGRE/HEROS data from the TIGRE 1.2 m telescope are not available via VSO.
"""

import astropy.units as u
from sunpy.net import attrs as a
from sunpy.net.vso import VSOClient

# Instantiate the VSO client
client = VSOClient()

# --------------------------------------------------------------------
# Query 1: ISS on SOLIS (Ca II K 1-Å Index)
# Time Range : 2015-10-01 to 2016-12-31
# Instrument : ISS
# --------------------------------------------------------------------
time_iss = a.Time('2015-10-01', '2016-12-31')
inst_iss = a.Instrument('ISS')

print("Performing VSO search for SOLIS/ISS Ca II K 1-Å index...")
result_iss = client.search(time_iss, inst_iss)
print(result_iss)

# To download the data, uncomment the following line:
# client.fetch(result_iss)

# --------------------------------------------------------------------
# Query 2: SOLSTICE on SORCE (Far-UV Irradiance)
# Time Range : 2003-01-01 to 2016-12-31
# Instrument : SOLSTICE
# Wavelength  : 200 nm to 280 nm
# --------------------------------------------------------------------
time_solstice = a.Time('2003-01-01', '2016-12-31')
inst_solstice = a.Instrument('SOLSTICE')
wave_solstice = a.Wave(200 * u.nm, 280 * u.nm)

print("Performing VSO search for SORCE/SOLSTICE far-UV irradiance (200–280 nm)...")
result_solstice = client.search(time_solstice, inst_solstice, wave_solstice)
print(result_solstice)

# To download the data, uncomment the following line:
# client.fetch(result_solstice)
