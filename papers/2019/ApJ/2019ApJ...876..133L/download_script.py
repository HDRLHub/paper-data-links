# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
A Python Sunpy VSO query script for downloading solar observation data.
This script constructs three separate queries:
  1. SDO/HMI vector magnetic field data during the flare stage (00:12 UT to 01:00 UT).
  2. SDO/HMI vector magnetic field data during the post-flare stage (03:12 UT to 04:00 UT).
  3. SDO/AIA EUV images at 1600 Å near the flare peak time.
  
These queries rely on data as described in the context:
  - HMI provides full-disk photospheric magnetograms (using the FeI 6173 Å spectral line)
    used to examine the evolution of the photospheric horizontal magnetic field (Bh).
  - AIA images at 1600 Å are used to trace the morphology of flare ribbons.
  
Note: The Fido.fetch commands are commented out to only display the query results.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time ranges for the observations (using an example date from context: 2011-02-15)
# Flare stage: 00:12 UT to 01:00 UT (vector magnetograms for HMI)
flare_stage_start = '2011-02-15T00:12:00'
flare_stage_end   = '2011-02-15T01:00:00'

# Post-flare stage: 03:12 UT to 04:00 UT (vector magnetograms for HMI)
post_flare_start = '2011-02-15T03:12:00'
post_flare_end   = '2011-02-15T04:00:00'

# AIA observation: image taken at flare peak time (example: 01:56 UT, corresponding to GOES peak for AR11158)
aia_peak_time = '2011-02-15T01:56:00'
aia_delta = 60  # seconds of duration around the peak time

# ------------------------------------------------------------------------------------
# Query 1: SDO/HMI vector magnetic field data during flare stage
# We select HMI data with observable 'vector_magnetic_field' and narrow wavelength range around 6173 Å.
print("Querying SDO/HMI vector magnetic field data for flare stage (00:12 UT to 01:00 UT).")
hmi_flare_query = Fido.search(
    a.Time(flare_stage_start, flare_stage_end),
    a.Instrument("HMI"),
    a.Physobs("vector_magnetic_field"),
    a.Wavelength(6173*u.angstrom, 6174*u.angstrom)  # the FeI line near 6173 Å
)
print(hmi_flare_query)

# Uncomment the following line to fetch the data
# hmi_flare_files = Fido.fetch(hmi_flare_query)

# ------------------------------------------------------------------------------------
# Query 2: SDO/HMI vector magnetic field data during post-flare stage
print("\nQuerying SDO/HMI vector magnetic field data for post-flare stage (03:12 UT to 04:00 UT).")
hmi_postflare_query = Fido.search(
    a.Time(post_flare_start, post_flare_end),
    a.Instrument("HMI"),
    a.Physobs("vector_magnetic_field"),
    a.Wavelength(6173*u.angstrom, 6174*u.angstrom)
)
print(hmi_postflare_query)

# Uncomment the following line to fetch the data
# hmi_postflare_files = Fido.fetch(hmi_postflare_query)

# ------------------------------------------------------------------------------------
# Query 3: SDO/AIA 1600 Å images used for flare ribbon imaging
print("\nQuerying SDO/AIA 1600 Å images near flare peak time (around 01:56 UT).")
aia_query = Fido.search(
    a.Time(aia_peak_time, aia_peak_time),  # Using an instantaneous time; you may adjust the duration as needed.
    a.Instrument("AIA"),
    a.Wavelength(1600*u.angstrom, 1600*u.angstrom)
)
print(aia_query)

# Uncomment the following line to fetch the data
# aia_files = Fido.fetch(aia_query)

if __name__ == '__main__':
    print("\nQuery script executed. Check the printed query results for details.")
