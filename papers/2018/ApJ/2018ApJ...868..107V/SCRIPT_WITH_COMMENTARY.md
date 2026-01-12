# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query data from the Virtual Solar Observatory (VSO)
using SunPy for two instruments relevant to the provided science context.

In this example we query:
1. GOES-16/SUVI data for two time intervals:
   - Overall event coverage from 15:20:24 UT to 17:00:24 UT (with focus on the 195 Å channel).
   - CME shell segmentation period from 15:49:00 UT to 15:57:00 UT.
2. SDO/AIA data for the CME cavity and flux rope evolution from 15:17:30 UT to 16:40:00 UT.

Note:
- We assume an observation date of 2017-04-01 which is within the SUVI available time range.
- The actual data fetching via Fido.fetch is commented out.
"""

from sunpy.net import Fido
from sunpy.net import attrs as a
import astropy.units as u

# ------------------------------
# 1. Query for GOES-16/SUVI data (Overall Event Coverage)
# ------------------------------
# Setting the time range for the overall event (assumed date: 2017-04-01)
start_time_overall = "2017-04-01T15:20:24"
end_time_overall   = "2017-04-01T17:00:24"

# We focus on the 195 Å channel observations as highlighted in the context.
# The instrument is SUVI onboard GOES-16.
query_overall = Fido.search(
    a.Time(start_time_overall, end_time_overall),
    a.Instrument("SUVI"),
    a.Source("GOES16"),
    a.Wavelength(195 * u.angstrom)
)

print("GOES-16/SUVI Overall Event Query Results:")
print(query_overall)

# To download the data, one would use:
# files_overall = Fido.fetch(query_overall)
# print("Downloaded GOES-16/SUVI overall event files:", files_overall)

# ------------------------------
# 2. Query for GOES-16/SUVI data (CME Shell Segmentation)
# ------------------------------
# Setting the time range for the CME shell segmentation period
start_time_segmentation = "2017-04-01T15:49:00"
end_time_segmentation   = "2017-04-01T15:57:00"

query_segmentation = Fido.search(
    a.Time(start_time_segmentation, end_time_segmentation),
    a.Instrument("SUVI"),
    a.Source("GOES16"),
    a.Wavelength(195 * u.angstrom)
)

print("\nGOES-16/SUVI Segmentation Period Query Results:")
print(query_segmentation)

# To download the segmentation period data, one would use:
# files_segmentation = Fido.fetch(query_segmentation)
# print("Downloaded GOES-16/SUVI segmentation files:", files_segmentation)

# ------------------------------
# 3. Query for SDO/AIA data (CME Cavity and Flux Rope Evolution)
# ------------------------------
# Setting the time range for the AIA event (assumed date: 2017-04-01)
start_time_aia = "2017-04-01T15:17:30"
end_time_aia   = "2017-04-01T16:40:00"

# In the context, multiple wavelengths are used.
# For this query, we use the key channels mentioned: 94 Å, 131 Å, 171 Å, 193 Å, 211 Å, 335 Å, and 304 Å.
# Note: The available wavelengths are given as comma-separated values in the VSO interface.
query_aia = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Wavelength(94 * u.angstrom),
    a.Wavelength(131 * u.angstrom),
    a.Wavelength(171 * u.angstrom),
    a.Wavelength(193 * u.angstrom),
    a.Wavelength(211 * u.angstrom),
    a.Wavelength(335 * u.angstrom),
    a.Wavelength(304 * u.angstrom)
)

print("\nSDO/AIA CME Cavity and Flux Rope Evolution Query Results:")
print(query_aia)

# To download the AIA data, one would use:
# files_aia = Fido.fetch(query_aia)
# print("Downloaded SDO/AIA files:", files_aia)

if __name__ == "__main__":
    print("\nQueries executed. Review the printed query summaries above for details.")
