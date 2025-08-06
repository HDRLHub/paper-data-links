# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script queries VSO for:
  1) White-light coronagraph images from SOHO/LASCO C2 for CME geometrical modeling
     over Solar Cycle 24 (~2007–2012).
  2) Photospheric vector magnetic field data from SDO/HMI for active region helicity
     measurements over 2011–2012.
The queries print the search results. To download data, uncomment the Fido.fetch calls.
"""

import sunpy.net as net
from sunpy.net import Fido, attrs as a
from sunpy.time import parse_time

# Define time ranges
# CME geometrical parameters period (Solar Cycle 24: 2007–2012)
geom_start = parse_time("2007-01-01")
geom_end   = parse_time("2012-12-31")

# Active region helicity period (within HMI availability: 2011–2012)
helicity_start = parse_time("2011-01-01")
helicity_end   = parse_time("2012-12-31")

# ------------------------------------------------------------------------
# 1) Query SOHO/LASCO C2 coronagraph intensity images
# ------------------------------------------------------------------------
geom_query = Fido.search(
    a.Time(geom_start, geom_end),
    a.vso.Source('SOHO'),
    a.vso.Instrument('LASCO'),
    a.vso.Detector('C2'),
    a.vso.Physobs('intensity')
)
print("SOHO/LASCO C2 intensity search results:")
print(geom_query)

# ------------------------------------------------------------------------
# 2) Query SDO/HMI vector magnetic field data
# ------------------------------------------------------------------------
vector_query = Fido.search(
    a.Time(helicity_start, helicity_end),
    a.vso.Source('SDO'),
    a.vso.Instrument('HMI'),
    a.vso.Physobs('vector_magnetic_field')
)
print("\nSDO/HMI vector magnetic field search results:")
print(vector_query)

# ------------------------------------------------------------------------
# To download data, uncomment the following lines:
# ------------------------------------------------------------------------
# geom_files = Fido.fetch(geom_query)
# vector_files = Fido.fetch(vector_query)
