# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query solar data from the Virtual Solar Observatory (VSO) using SunPy.
We perform two separate queries:
  1. SDO/HMI data for LOS magnetic field measurements from 2010-01-01 to 2015-12-31.
     Note: HMI observations on SDO began in 2010.
  2. SOHO/MDI data for LOS magnetic field measurements from 2000-01-01 to 2011-04-12.
     Although the paper's analysis spans until 2015, MDI data are available only until 2011.
The queries are constructed with explicit attribute definitions.
Fido.fetch commands are provided but commented out to avoid automatic downloads.
"""

# Import required sunpy modules and attributes
from sunpy.net import Fido, attrs as a

# -------------------------------
# Query 1: SDO/HMI Data Query
# -------------------------------
# Time range: 2010-01-01 to 2015-12-31 (HMI data available from 2010 onward)
# Instrument: HMI on board the Solar Dynamics Observatory (SDO)
# Physical Observable: LOS_magnetic_field (as a proxy for radial magnetic field in the context)
hmi_time_start = '2010-01-01'
hmi_time_end = '2015-12-31'
hmi_query = Fido.search(
    a.Time(hmi_time_start, hmi_time_end),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)

# Print the query results for SDO/HMI
print("SDO/HMI Query Result:")
print(hmi_query)

# Uncomment the following line to fetch the SDO/HMI data files
# hmi_files = Fido.fetch(hmi_query)

# -------------------------------
# Query 2: SOHO/MDI Data Query
# -------------------------------
# Time range: 2000-01-01 to 2011-04-12 (MDI provides full-disk magnetic field data during this interval)
# Instrument: MDI on board the Solar and Heliospheric Observatory (SOHO)
# Physical Observable: LOS_magnetic_field
mdi_time_start = '2000-01-01'
mdi_time_end = '2011-04-12'
mdi_query = Fido.search(
    a.Time(mdi_time_start, mdi_time_end),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Detector('MDI'),
    a.Physobs('LOS_magnetic_field')
)

# Print the query results for SOHO/MDI
print("\nSOHO/MDI Query Result:")
print(mdi_query)

# Uncomment the following line to fetch the SOHO/MDI data files
# mdi_files = Fido.fetch(mdi_query)

if __name__ == '__main__':
    print("VSO queries constructed. Check the printed query objects for details.")
