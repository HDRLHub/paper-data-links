# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs VSO queries using SunPy for a multi-instrument observational study of a solar active region.
The observations cover the period from 17 July 2010 to 18 November 2010.
In this study, we are interested in:
  - EUV imaging of the AR from SDO/AIA in the 304 Å, 171 Å, and 195 Å channels.
  - Photospheric magnetic field measurements from SDO/HMI.
  - Additional complementary data from SOHO instruments (MDI magnetograms and LASCO C2 coronagraph images).
  
Note: The script is structured to print out query results.
The actual data downloads (via Fido.fetch) are provided as commented-out lines.
"""

# Import necessary modules from SunPy and Astropy units.
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the observation time range for the active region study.
start_time = "2010-07-17"
end_time = "2010-11-18"

# ------------------------------
# 1. Query for SDO/AIA EUV images
# We are interested in three channels: 304 Å, 171 Å, and 195 Å.
# The vso_interface for SDO/AIA shows that these wavelengths are available.
# ------------------------------

# Query AIA for the 304 Å channel.
aia_304_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("AIA"),
    a.Wavelength(304*u.AA, 304*u.AA)
)
print("SDO/AIA 304 Å query results:")
print(aia_304_query)

# Uncomment the following line to fetch AIA 304 Å data:
# aia_304_files = Fido.fetch(aia_304_query)

# Query AIA for the 171 Å channel.
aia_171_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("AIA"),
    a.Wavelength(171*u.AA, 171*u.AA)
)
print("SDO/AIA 171 Å query results:")
print(aia_171_query)

# Uncomment the following line to fetch AIA 171 Å data:
# aia_171_files = Fido.fetch(aia_171_query)

# Query AIA for the 195 Å channel.
aia_195_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("AIA"),
    a.Wavelength(195*u.AA, 195*u.AA)
)
print("SDO/AIA 195 Å query results:")
print(aia_195_query)

# Uncomment the following line to fetch AIA 195 Å data:
# aia_195_files = Fido.fetch(aia_195_query)


# ------------------------------
# 2. Query for SDO/HMI magnetograms
# The HMI data provide full-disk vector (or line-of-sight) magnetogram measurements over the AR near-side passages.
# ------------------------------

hmi_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("HMI")
)
print("SDO/HMI query results:")
print(hmi_query)

# Uncomment the following line to fetch HMI data:
# hmi_files = Fido.fetch(hmi_query)


# ------------------------------
# 3. Query for SOHO/MDI magnetograms
# MDI magnetograms provide complementary photospheric magnetic field measurements.
# Note: The available full time range for MDI is from 1996 to 2011/04/12.
# ------------------------------

mdi_query = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("MDI")
)
print("SOHO/MDI query results:")
print(mdi_query)

# Uncomment the following line to fetch MDI data:
# mdi_files = Fido.fetch(mdi_query)


# ------------------------------
# 4. Query for SOHO/LASCO C2 coronagraph images
# LASCO C2 images are used to identify and measure the characteristics of CMEs when the AR is observed near the solar limb.
# ------------------------------

lasco_query = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("SOHO/LASCO C2 query results:")
print(lasco_query)

# Uncomment the following line to fetch LASCO C2 data:
# lasco_files = Fido.fetch(lasco_query)


if __name__ == "__main__":
    print("VSO queries completed. Review the printed query results for details.")
