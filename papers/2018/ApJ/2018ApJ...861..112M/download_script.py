# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Query Script for Prominence Tornadoes Study

This script creates two separate VSO queries:
1. A query for SDO/AIA data covering the full year 2011 in three EUV bands:
   - 171 Å (for prominence tornado detection as dark structures)
   - 193 Å (to capture additional thermal information, found within the 191–195 Å range)
   - 304 Å (to monitor prominence brightening associated with activity)
2. A query for LASCO/C2 data from SOHO for a specific eruptive event recorded on October 13, 2011.
   The LASCO/C2 coronagraph data is used to track the CME appearance following the tornado eruption.
   
Note: The Fido.fetch commands are provided as comments so that you can uncomment them as needed.
"""

# Import necessary modules from sunpy and astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# -----------------------------
# 1. Query SDO/AIA Data for the full year 2011 for selected wavelengths.
# -----------------------------

# Define time range for the full year 2011.
time_start_aia = "2011-01-01"
time_end_aia = "2011-12-31"

# Query for AIA 171 Å data
query_aia_171 = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument("AIA"),
    a.Wavelength(171 * u.AA)
)
print("SDO/AIA 171 Å Query Results:")
print(query_aia_171)

# Uncomment the following line to fetch the AIA 171 Å data:
# data_aia_171 = Fido.fetch(query_aia_171)

# Query for AIA 193 Å data (Note: 193 Å falls in the range 191–195 Å available in VSO interface)
query_aia_193 = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.AA)
)
print("\nSDO/AIA 193 Å Query Results:")
print(query_aia_193)

# Uncomment the following line to fetch the AIA 193 Å data:
# data_aia_193 = Fido.fetch(query_aia_193)

# Query for AIA 304 Å data
query_aia_304 = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument("AIA"),
    a.Wavelength(304 * u.AA)
)
print("\nSDO/AIA 304 Å Query Results:")
print(query_aia_304)

# Uncomment the following line to fetch the AIA 304 Å data:
# data_aia_304 = Fido.fetch(query_aia_304)

# -----------------------------
# 2. Query LASCO/C2 Data for the Representative Eruptive Event on October 13, 2011.
# -----------------------------

# Define a time window around the eruptive event:
# Tornado eruption observed ~01:00 UT and CME first appearance by ~02:03 UT.
time_start_lasco = "2011-10-13T01:00:00"
time_end_lasco   = "2011-10-13T03:00:00"

# Query for LASCO/C2 data using SOHO as the source and C2 as the detector
query_lasco_c2 = Fido.search(
    a.Time(time_start_lasco, time_end_lasco),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nSOHO LASCO/C2 Query Results:")
print(query_lasco_c2)

# Uncomment the following line to fetch the LASCO/C2 data:
# data_lasco_c2 = Fido.fetch(query_lasco_c2)

if __name__ == "__main__":
    print("\nVSO Data Queries Completed. Check the printed query results for each instrument/wavelength set.")
