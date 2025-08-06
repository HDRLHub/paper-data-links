# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3

"""
This script queries the Virtual Solar Observatory (VSO) for the
high-resolution line-of-sight synoptic magnetograms used in the
study of solar polar field reversals in solar cycles 23 and 24.

- SOHO/MDI: April 1996 – February 2009 (CR 1911–2080)
- SDO/HMI: April 2010 – August 2017 (CR 2096–2194)

Note: Radial synoptic magnetograms are not currently available via VSO,
so we retrieve the LOS magnetic field data as the closest proxy.
"""

from sunpy.net import Fido, attrs as a

# -------------------------------------------------------------------
# Query 1: SOHO/MDI high-resolution line-of-sight synoptic magnetograms
# Time range corresponds to Carrington Rotations 1911–2080:
#   April 1, 1996 – February 28, 2009
# -------------------------------------------------------------------
time_mdi = a.Time('1996-04-01', '2009-02-28')
instrument_mdi = a.Instrument('MDI')
source_mdi = a.Source('SOHO')
physobs_mdi = a.Physobs('LOS_magnetic_field')

# Perform the search
result_mdi = Fido.search(time_mdi, instrument_mdi, source_mdi, physobs_mdi)

# Display the query results
print("SOHO/MDI LOS Magnetogram Search Results:")
print(result_mdi)

# To download the data, uncomment the following line:
# files_mdi = Fido.fetch(result_mdi)


# -------------------------------------------------------------------
# Query 2: SDO/HMI line-of-sight synoptic magnetograms
# Time range corresponds to Carrington Rotations 2096–2194:
#   April 1, 2010 – August 31, 2017
# -------------------------------------------------------------------
time_hmi = a.Time('2010-04-01', '2017-08-31')
instrument_hmi = a.Instrument('HMI')
source_hmi = a.Source('SDO')
physobs_hmi = a.Physobs('LOS_magnetic_field')

# Perform the search
result_hmi = Fido.search(time_hmi, instrument_hmi, source_hmi, physobs_hmi)

# Display the query results
print("\nSDO/HMI LOS Magnetogram Search Results:")
print(result_hmi)

# To download the data, uncomment the following line:
# files_hmi = Fido.fetch(result_hmi)
