# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query full-disk magnetogram data from two instruments:
1. The Michelson Doppler Imager (MDI) on board SoHO, which observed Cycle 23.
2. The Helioseismic and Magnetic Imager (HMI) on board SDO, which observed Cycle 24.

The queries use the SunPy VSO client. The time ranges have been chosen to reflect the
data collection periods discussed in the paper:
  - SOHO/MDI: May 1996 to January 2008 (Cycle 23).
  - SDO/HMI: March 2010 to July 2018 (Cycle 24).

We query for the "LOS_magnetic_field" observable which is typically used for sunspot full-disk magnetograms.
Note: The Fido.fetch commands are commented out to prevent automatic downloads.
"""

from sunpy.net import Fido, attrs as a

# ---------------------------
# Query for SOHO MDI full-disk magnetograms (Cycle 23)
# ---------------------------
# Define the time range for Cycle 23 observations (approximately from May 1996 to January 2008)
mdi_time_start = '1996-05-01'
mdi_time_end = '2008-01-01'

# Construct the query for SOHO/MDI using the available attributes.
# According to the VSO interface, we need:
#   - Source: SOHO
#   - Instrument: MDI
#   - Detector: MDI (as specified in the vso_interface)
#   - Physical observable: LOS_magnetic_field
mdi_query = Fido.search(
    a.Time(mdi_time_start, mdi_time_end),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Detector('MDI'),
    a.Physobs('LOS_magnetic_field')
)

# Print the SOHO/MDI query results.
print("SOHO/MDI Query Results:")
print(mdi_query)

# Uncomment the following line to fetch the data:
# mdi_downloaded_files = Fido.fetch(mdi_query)


# ---------------------------
# Query for SDO HMI full-disk magnetograms (Cycle 24)
# ---------------------------
# Define the time range for Cycle 24 observations (from the start of HMI operation to July 2018)
hmi_time_start = '2010-03-29'
hmi_time_end = '2018-07-01'

# Construct the query for SDO/HMI.
# Attributes used are:
#   - Source: SDO
#   - Instrument: HMI
#   - Physical observable: LOS_magnetic_field (common for magnetogram measurements)
hmi_query = Fido.search(
    a.Time(hmi_time_start, hmi_time_end),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)

# Print the SDO/HMI query results.
print("SDO/HMI Query Results:")
print(hmi_query)

# Uncomment the following line to fetch the data:
# hmi_downloaded_files = Fido.fetch(hmi_query)


if __name__ == '__main__':
    pass
