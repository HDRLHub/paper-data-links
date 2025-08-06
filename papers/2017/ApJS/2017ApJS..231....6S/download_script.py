# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
SunPy VSO Query Script for Multi-Instrument Solar Flare Data

This script performs four separate VSO searches corresponding to the instruments
used in the IMIDSF database paper:
    • RHESSI (hard X-ray)
    • SDO/AIA (EUV imaging)
    • SDO/EVE ESP (EUV irradiance)
    • IRIS SJI (UV imaging)

Each query uses the full available time range for the instrument as described
in the paper. Results are printed to the console. The Fido.fetch() calls are
provided but commented out; uncomment to download data.
"""

import astropy.units as u
from sunpy.net import Fido, vso
from sunpy.net.vso import attrs as vattrs

# RHESSI Query
#   Time Range: 2002-02-12 – present
#   Instrument: RHESSI
rhessi_start = "2002-02-12"
rhessi_end = "now"
rhessi_query = Fido.search(
    vattrs.Time(rhessi_start, rhessi_end),
    vattrs.Instrument("RHESSI")
)
print("RHESSI Search Results:")
print(rhessi_query)
# To download RHESSI data, uncomment the next line:
# Fido.fetch(rhessi_query)

# SDO/AIA Query
#   Time Range: 2010-02-01 – present (AIA operational since Feb 2010)
#   Instrument: AIA
aia_start = "2010-02-01"
aia_end = "now"
aia_query = Fido.search(
    vattrs.Time(aia_start, aia_end),
    vattrs.Instrument("AIA")
)
print("\nSDO/AIA Search Results:")
print(aia_query)
# To download AIA data, uncomment the next line:
# Fido.fetch(aia_query)

# SDO/EVE ESP Query
#   Time Range: 2010-04-30 – present
#   Instrument: EVE, Detector: ESP
eve_start = "2010-04-30"
eve_end = "now"
eve_query = Fido.search(
    vattrs.Time(eve_start, eve_end),
    vattrs.Instrument("EVE"),
    vattrs.Detector("ESP")
)
print("\nSDO/EVE ESP Search Results:")
print(eve_query)
# To download EVE ESP data, uncomment the next line:
# Fido.fetch(eve_query)

# IRIS Slit‐Jaw Imager (SJI) Query
#   Time Range: 2013-07-16 – present
#   Instrument: IRIS, Detector: SJI
iris_start = "2013-07-16"
iris_end = "now"
iris_query = Fido.search(
    vattrs.Time(iris_start, iris_end),
    vattrs.Instrument("IRIS"),
    vattrs.Detector("SJI")
)
print("\nIRIS SJI Search Results:")
print(iris_query)
# To download IRIS SJI data, uncomment the next line:
# Fido.fetch(iris_query)
