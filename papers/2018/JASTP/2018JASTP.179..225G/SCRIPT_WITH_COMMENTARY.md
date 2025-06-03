# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates sample SunPy VSO queries for downloading solar data
from distinct instruments relevant to the context. In this example, we query:
  1. SOHO/LASCO C3 white‐light coronagraph images during the CME event on 21 June 2015.
  2. SDO/AIA EUV images from two channels (193 Å and 1600 Å) capturing the flare emissions.
  3. SDO/HMI magnetograms capturing the photospheric magnetic field at the flare source.
  
Note: The Fido.fetch() commands are provided as commented code lines, since the script is
only intended to demonstrate query construction.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# -------------------------------
# 1. SOHO/LASCO C3 Query (White-light Coronagraph Data)
# Data Collection: LASCO C3 images capturing the initial CME appearance and expansion.
# Time Range covers approximately 02:00 UT to 06:00 UT on June 21, 2015.
# Using SOHO as the source, LASCO as the instrument and C3 as the detector.
lasco_time = a.Time("2015-06-21T02:00:00", "2015-06-21T06:00:00")
lasco_source = a.Source("SOHO")
lasco_instrument = a.Instrument("LASCO")
lasco_detector = a.Detector("C3")
# Build the query for LASCO C3 data.
lasco_query = Fido.search(lasco_time, lasco_source, lasco_instrument, lasco_detector)
print("SOHO/LASCO C3 Query Results:")
print(lasco_query)
# Uncomment the following line to fetch the data:
# lasco_files = Fido.fetch(lasco_query)

# -------------------------------
# 2. SDO/AIA Query (EUV Imaging Data)
# Two separate queries are constructed for different phases of the flare:
# a) Confined flare phase using the 1600 Å channel (flare ribbons) around 01:45 UT.
# b) Eruptive flare phase using the 193 Å channel capturing extended disturbances around 02:20 UT.
#
# a) Query for the 1600 Å images:
aia_time_1600 = a.Time("2015-06-21T01:40:00", "2015-06-21T01:50:00")
aia_source = a.Source("SDO")
aia_instrument = a.Instrument("AIA")
# The available wavelengths in the VSO interface for AIA include 1600 Å.
aia_wavelength_1600 = a.Wavelength(1600 * u.Angstrom, 1600 * u.Angstrom)
aia_query_1600 = Fido.search(aia_time_1600, aia_source, aia_instrument, aia_wavelength_1600)
print("\nSDO/AIA 1600 Å Query Results (Confined Flare Phase):")
print(aia_query_1600)
# Uncomment the following line to fetch AIA 1600 Å data:
# aia_files_1600 = Fido.fetch(aia_query_1600)

# b) Query for the 193 Å images (using the range that includes 193 Å, e.g., 191-195 Å):
aia_time_193 = a.Time("2015-06-21T02:00:00", "2015-06-21T02:40:00")
aia_wavelength_193 = a.Wavelength(191 * u.Angstrom, 195 * u.Angstrom)
aia_query_193 = Fido.search(aia_time_193, aia_source, aia_instrument, aia_wavelength_193)
print("\nSDO/AIA 193 Å Query Results (Eruptive Flare Phase):")
print(aia_query_193)
# Uncomment the following line to fetch AIA 193 Å data:
# aia_files_193 = Fido.fetch(aia_query_193)

# -------------------------------
# 3. SDO/HMI Query (Photospheric Magnetogram Data)
# Query for the HMI line-of-sight magnetogram capturing the active region at ~01:11 UT.
hmi_time = a.Time("2015-06-21T01:10:00", "2015-06-21T01:20:00")
hmi_source = a.Source("SDO")
hmi_instrument = a.Instrument("HMI")
# Although the VSO interface contains multiple HMI physobs options, here we are interested in the general LOS magnetic field.
hmi_query = Fido.search(hmi_time, hmi_source, hmi_instrument)
print("\nSDO/HMI Query Results (Magnetogram):")
print(hmi_query)
# Uncomment the following line to fetch HMI data:
# hmi_files = Fido.fetch(hmi_query)

# -------------------------------
# End of Script
if __name__ == '__main__':
    print("\nCompleted all queries. Review query results above before fetching actual data.")
