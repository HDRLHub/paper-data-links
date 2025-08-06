# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Query Script for SDO/HMI and SOHO/MDI data
Query periods:
 - HMI: 2012-01-01 to 2012-12-31 (white-light and magnetic images)
 - MDI: 2000-01-01 to 2002-12-31 (white-light and magnetic images)
"""
import sunpy.net
from sunpy.net import Fido, attrs as a

# -------------------------------------------------------------------
# 1. Query SDO/HMI white-light images for the year 2012
# -------------------------------------------------------------------
hmi_wl_query = Fido.search(
    a.Time("2012-01-01", "2012-12-31"),
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("intensity")  # white-light (continuum)
)
print("HMI white-light search results:")
print(hmi_wl_query)

# To download the data, uncomment the following line:
# downloaded_hmi_wl = Fido.fetch(hmi_wl_query)

# -------------------------------------------------------------------
# 2. Query SDO/HMI magnetic (LOS field) images for the year 2012
# -------------------------------------------------------------------
hmi_mag_query = Fido.search(
    a.Time("2012-01-01", "2012-12-31"),
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")  # line‐of‐sight magnetic field
)
print("\nHMI magnetic (LOS) search results:")
print(hmi_mag_query)

# To download the data, uncomment the following line:
# downloaded_hmi_mag = Fido.fetch(hmi_mag_query)

# -------------------------------------------------------------------
# 3. Query SOHO/MDI white-light images for 2000–2002 (alignment studies)
# -------------------------------------------------------------------
mdi_wl_query = Fido.search(
    a.Time("2000-01-01", "2002-12-31"),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Physobs("intensity")  # white-light continuum
)
print("\nMDI white-light search results:")
print(mdi_wl_query)

# To download the data, uncomment the following line:
# downloaded_mdi_wl = Fido.fetch(mdi_wl_query)

# -------------------------------------------------------------------
# 4. Query SOHO/MDI magnetic (LOS field) images for 2000–2002 (alignment studies)
# -------------------------------------------------------------------
mdi_mag_query = Fido.search(
    a.Time("2000-01-01", "2002-12-31"),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Physobs("LOS_magnetic_field")  # line‐of‐sight magnetic field
)
print("\nMDI magnetic (LOS) search results:")
print(mdi_mag_query)

# To download the data, uncomment the following line:
# downloaded_mdi_mag = Fido.fetch(mdi_mag_query)
