# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries three sets of solar data using SunPy's VSO interface:
  1. HMI vector magnetograms from SDO (pre-flare data) for the SOL2015-06-22 event.
  2. AIA ultraviolet images at 1600 Å from SDO (flare peak imaging) for the SOL2015-06-22 event.
  3. LASCO C2 white-light coronagraph data from SOHO (for CME association) around the flare timing.

Note:
- NOAA GOES soft X-ray data are not available in the provided VSO interface.
- The queries use the time ranges and instruments provided in the context.
- The Fido.fetch commands are included but commented out; they can be activated as needed.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# -----------------------
# Query 1: HMI vector magnetograms (SDO/HMI)
# Time chosen based on the pre-flare magnetogram for SOL2015-06-22 event (e.g., 17:36 UT)
hmi_time_start = '2015-06-22T17:30:00'
hmi_time_end   = '2015-06-22T17:45:00'

# Constructing the query for SDO/HMI vector magnetic field data
hmi_query = Fido.search(
    a.Time(hmi_time_start, hmi_time_end),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('vector_magnetic_field')
)

print("HMI Query Result:")
print(hmi_query)

# To download HMI data (uncomment the line below):
# hmi_files = Fido.fetch(hmi_query)

# -----------------------
# Query 2: AIA 1600 Å ultraviolet images (SDO/AIA)
# Time chosen for the flare peak imaging at SOL2015-06-22 (e.g., 18:23 UT)
aia_time_start = '2015-06-22T18:23:00'
aia_time_end   = '2015-06-22T18:30:00'

# Constructing the query for SDO/AIA data with narrowband filter at 1600 Å
aia_query = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(1600 * u.AA, 1600 * u.AA)
)

print("\nAIA Query Result:")
print(aia_query)

# To download AIA data (uncomment the line below):
# aia_files = Fido.fetch(aia_query)

# -----------------------
# Query 3: LASCO C2 coronagraph data (SOHO/LASCO)
# Time chosen around the flare window (SOL2015-06-22) to assess potential CME association.
lasco_time_start = '2015-06-22T18:00:00'
lasco_time_end   = '2015-06-22T19:00:00'

# Constructing the query for SOHO LASCO data specifying the C2 detector.
lasco_query = Fido.search(
    a.Time(lasco_time_start, lasco_time_end),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)

print("\nLASCO Query Result:")
print(lasco_query)

# To download LASCO data (uncomment the line below):
# lasco_files = Fido.fetch(lasco_query)

if __name__ == '__main__':
    print("\nQueries executed. Review the printed results for details.")
