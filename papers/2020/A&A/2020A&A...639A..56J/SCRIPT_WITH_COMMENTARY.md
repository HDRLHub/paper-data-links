# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the Virtual Solar Observatory (VSO) for data
relevant to a study of a CME/flare event on September 27/28, 2012. The queries request:

1. SDO/AIA data in the EUV (using the 193 Å filter, which falls within the 191–195 Å range 
   available for AIA) to capture on-disk signatures such as the EIT wave and coronal dimming.
2. SOHO/LASCO data from the C2 coronagraph covering the white-light corona seen at
   00:00 UT on September 28, 2012.
3. SOHO/LASCO data from the C3 coronagraph, also covering the same time interval for
   complementary white-light views.

Each query prints the search results. The commands for fetching the data are provided
but commented out to prevent accidental download.
"""

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define time ranges based on the event timings in the paper:

# For SDO/AIA: The event (flare/CME on-disk signatures) occurred around late September 27
# to early September 28, 2012. Here, we choose a time window that covers the period
# during which the on-disk phenomena (such as the EIT wave) were observed.
time_range_aia = a.Time("2012-09-27T23:30:00", "2012-09-28T01:00:00")

# For SOHO/LASCO: The CME was first seen in the LASCO C2 field-of-view at 00:00 UT on
# September 28, 2012. We define a time interval around this observation.
time_range_lasco = a.Time("2012-09-28T00:00:00", "2012-09-28T01:00:00")

# -----------------------------------------------------------------------------
# Query 1: SDO/AIA Data
# -----------------------------------------------------------------------------
# The Atmospheric Imaging Assembly (AIA) on board SDO provides EUV images. While the paper
# emphasizes the 193 Å filter for on-disk signatures, the VSO interface lists available wavelengths
# as 191.0 - 195.0 Å (among others). Thus, we search for images in that range.
aia_query = Fido.search(
    time_range_aia,
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Wavelength(191*u.AA, 195*u.AA)
)

print("SDO/AIA Query:")
print(aia_query)
# To fetch the data, remove the comment from the following line:
# aia_files = Fido.fetch(aia_query)

# -----------------------------------------------------------------------------
# Query 2: SOHO/LASCO C2 Data
# -----------------------------------------------------------------------------
# LASCO C2 provides white-light coronagraph images essential for tracking the CME evolution.
lasco_c2_query = Fido.search(
    time_range_lasco,
    a.Instrument("LASCO"),
    a.Source("SOHO"),
    a.Detector("C2")
)

print("\nSOHO/LASCO C2 Query:")
print(lasco_c2_query)
# To fetch the data, remove the comment from the following line:
# lasco_c2_files = Fido.fetch(lasco_c2_query)

# -----------------------------------------------------------------------------
# Query 3: SOHO/LASCO C3 Data
# -----------------------------------------------------------------------------
# Complementing the C2 data, LASCO C3 provides additional white-light views of the outer corona.
lasco_c3_query = Fido.search(
    time_range_lasco,
    a.Instrument("LASCO"),
    a.Source("SOHO"),
    a.Detector("C3")
)

print("\nSOHO/LASCO C3 Query:")
print(lasco_c3_query)
# To fetch the data, remove the comment from the following line:
# lasco_c3_files = Fido.fetch(lasco_c3_query)

if __name__ == '__main__':
    print("\nQueries completed. Review the printed query results above.")
