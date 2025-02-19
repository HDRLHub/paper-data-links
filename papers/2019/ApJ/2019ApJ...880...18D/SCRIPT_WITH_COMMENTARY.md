# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query data that correspond to the observational periods and instruments
described in the study. In this example we perform three separate queries:

1. SOHO/LASCO C2: Query white–light coronagraph data for CME signatures observed around 01:30–05:00 UT on July 23, 2017.
2. STEREO-A/SECCHI EUVI: Query EUV images in the 304 Å channel capturing the filament/prominence eruption
   around 22:30 UT on July 22, 2017.
3. STEREO-A/SECCHI COR2: Query white–light coronagraph data to capture the later phase (CME2 detection at 04:54 UT)
   with an observation window from 04:30–05:00 UT on July 23, 2017.

Note: The script prints out the query results. The actual data download commands (Fido.fetch) are provided
as commented-out lines.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# ------------------------------------------------------------------------------
# Query 1: SOHO/LASCO C2 Data for CME Observations on July 23, 2017
# ------------------------------------------------------------------------------
# The LASCO C2 coronagraph on SOHO captured CME signatures around 01:36 UT and 04:45 UT on July 23, 2017.
# We define a time window that covers these observations.
time_start_lasco = "2017-07-23T01:30:00"
time_end_lasco   = "2017-07-23T05:00:00"

query_lasco_c2 = Fido.search(
    a.Time(time_start_lasco, time_end_lasco),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Physobs("intensity")
)

print("SOHO LASCO C2 Query Results:")
print(query_lasco_c2)
# To download the data, uncomment the following line:
# files_lasco_c2 = Fido.fetch(query_lasco_c2)

# ------------------------------------------------------------------------------
# Query 2: STEREO-A SECCHI EUVI Data in the 304 Å Channel on July 22, 2017
# ------------------------------------------------------------------------------
# The EUVI instrument onboard STEREO-A captured the low-coronal filament/prominence eruption at ~22:30 UT on July 22, 2017.
# We refine our query to images in the 304 Å wavelength.
time_start_euvi = "2017-07-22T22:30:00"
time_end_euvi   = "2017-07-22T22:45:00"  # a short interval to capture the eruption onset

query_euvi_304 = Fido.search(
    a.Time(time_start_euvi, time_end_euvi),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    a.Wavelength(304*u.AA, 304*u.AA),
    a.Physobs("intensity")
)

print("\nSTEREO-A SECCHI EUVI (304 Å) Query Results:")
print(query_euvi_304)
# To download the data, uncomment the following line:
# files_euvi_304 = Fido.fetch(query_euvi_304)

# ------------------------------------------------------------------------------
# Query 3: STEREO-A SECCHI COR2 Data for CME Detection on July 23, 2017
# ------------------------------------------------------------------------------
# The COR2 coronagraph provides a higher coronal view where CME2 was detected at ~04:54 UT.
# We use a time window covering the later stage of the CME evolution.
time_start_cor2 = "2017-07-23T04:30:00"
time_end_cor2   = "2017-07-23T05:00:00"

query_cor2 = Fido.search(
    a.Time(time_start_cor2, time_end_cor2),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2"),
    a.Wavelength(6500*u.AA, 7500*u.AA),  # COR2 observes white-light in this band
    a.Physobs("intensity")
)

print("\nSTEREO-A SECCHI COR2 Query Results:")
print(query_cor2)
# To download the data, uncomment the following line:
# files_cor2 = Fido.fetch(query_cor2)

if __name__ == "__main__":
    print("\nVSO query script executed successfully.")
