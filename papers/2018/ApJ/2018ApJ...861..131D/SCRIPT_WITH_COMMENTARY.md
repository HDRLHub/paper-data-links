# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to build SunPy VSO queries using the Fido interface.
We construct queries for several instruments mentioned in our study:
  1. SDO/AIA – For high-cadence EUV observations (2013-11-10 flare event).
  2. SDO/HMI – For photospheric magnetic field measurements (post-2010).
  3. SOHO/MDI – For photospheric magnetic field in the pre-2010 era.
  4. SOHO/EIT – For full-Sun EUV imaging to compare with magnetic topology.
  5. SOHO/LASCO – For white-light coronagraph measurements of CMEs.
Each query uses only the required parameters (time range and instrument)
based on the vso_interface provided.
Note: The Fido.fetch commands are commented out to avoid running the downloads.
"""

from sunpy.net import Fido, attrs as a

# --------------------------
# Query 1: SDO/AIA Data Query
# --------------------------
# We use SDO/AIA data which is available from 2010 May onwards.
# For this example, we choose a one-hour interval covering the SOL2013-11-10T05:14 flare event.
aia_time = a.Time("2013-11-10T05:00:00", "2013-11-10T06:00:00")
aia_query = Fido.search(
    aia_time,
    a.Instrument("AIA"),
    a.Source("SDO")
)
print("SDO/AIA Query Result:")
print(aia_query)
# Uncomment the following line to fetch AIA data
# aia_files = Fido.fetch(aia_query)

# --------------------------
# Query 2: SDO/HMI Data Query
# --------------------------
# SDO/HMI provides high-resolution photospheric magnetic field data after 2010.
# We use the same time interval as above for consistency with the flare event.
hmi_time = a.Time("2013-11-10T05:00:00", "2013-11-10T06:00:00")
hmi_query = Fido.search(
    hmi_time,
    a.Instrument("HMI"),
    a.Source("SDO")
)
print("\nSDO/HMI Query Result:")
print(hmi_query)
# Uncomment the following line to fetch HMI data
# hmi_files = Fido.fetch(hmi_query)

# --------------------------
# Query 3: SOHO/MDI Data Query
# --------------------------
# SOHO/MDI data, used for photospheric magnetic field observations before 2010,
# is queried here for an event from 2001.
mdi_time = a.Time("2001-04-15T13:00:00", "2001-04-15T14:00:00")
mdi_query = Fido.search(
    mdi_time,
    a.Instrument("MDI"),
    a.Source("SOHO")
)
print("\nSOHO/MDI Query Result:")
print(mdi_query)
# Uncomment the following line to fetch MDI data
# mdi_files = Fido.fetch(mdi_query)

# --------------------------
# Query 4: SOHO/EIT Data Query
# --------------------------
# SOHO/EIT provides full-Sun EUV images. In our study EIT imagery is used to compare
# against PFSS-modelled open flux. The time interval is chosen to cover the 2001 event.
eit_time = a.Time("2001-04-15T13:00:00", "2001-04-15T14:00:00")
eit_query = Fido.search(
    eit_time,
    a.Instrument("EIT"),
    a.Source("SOHO")
)
print("\nSOHO/EIT Query Result:")
print(eit_query)
# Uncomment the following line to fetch EIT data
# eit_files = Fido.fetch(eit_query)

# --------------------------
# Query 5: SOHO/LASCO Data Query
# --------------------------
# SOHO/LASCO white-light coronagraph images help detect CMEs.
# Here we select a time interval corresponding to the SOL2013-11-10 event.
lasco_time = a.Time("2013-11-10T05:00:00", "2013-11-10T06:00:00")
lasco_query = Fido.search(
    lasco_time,
    a.Instrument("LASCO"),
    a.Source("SOHO")
)
print("\nSOHO/LASCO Query Result:")
print(lasco_query)
# Uncomment the following line to fetch LASCO data
# lasco_files = Fido.fetch(lasco_query)

if __name__ == '__main__':
    print("\nVSO Query script executed successfully. Review the printed query results for details.")
