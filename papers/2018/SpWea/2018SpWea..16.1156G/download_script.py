# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query solar data from the Virtual Solar Observatory 
(VSO) using sunpy.net’s Fido interface for a multi-instrument, multi-time event study.
The focus here is on specific observing intervals relevant to the study:
    • EUV wave observation with GOES-16 SUVI around 15:53–16:30 UT on 10 September 2017.
    • Flare and current sheet imaging with SDO AIA from 15:50–16:10 UT on 10 September 2017.
    • White-light coronagraph observation of CME3 with SOHO LASCO (using detector C3) 
      around 16:40–17:00 UT on 10 September 2017.
    • Hard X-ray burst observation with RHESSI from 15:50–16:15 UT on 10 September 2017.
    • Coronagraph observation of CME components with SECCHI on STEREO-A (using detector EUVI)
      covering the interval for CME1 and CME2 on 9 September 2017.
Note: This script only prints the query results. The actual data download (Fido.fetch) commands 
are provided as commented-out lines.
"""

import datetime
from sunpy.net import Fido, attrs as a

# Query 1: GOES-16 SUVI EUV wave observation
# Time range chosen to cover the EUV wave that started at ~15:53 UT on 10 September 2017
time_start_suvi = '2017-09-10T15:53'
time_end_suvi   = '2017-09-10T16:30'
query_suvi = Fido.search(
    a.Time(time_start_suvi, time_end_suvi),
    a.Instrument('SUVI'),
    a.Source('GOES16')
)
print("GOES-16 SUVI query results:")
print(query_suvi)
# To download the data, uncomment the following line:
# files_suvi = Fido.fetch(query_suvi)

# Query 2: SDO AIA flare and current sheet observation in EUV (131 Å channel is typical)
# Time range set from 15:50 UT to 16:10 UT on 10 September 2017.
time_start_aia = '2017-09-10T15:50'
time_end_aia   = '2017-09-10T16:10'
query_aia = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument('AIA'),
    a.Source('SDO')
)
print("\nSDO AIA query results:")
print(query_aia)
# To download the data, uncomment the following line:
# files_aia = Fido.fetch(query_aia)

# Query 3: SOHO LASCO coronagraph observation of CME3 (using detector C3)
# Approximate time range around the CME's white-light signature ~16:40 UT on 10 September 2017.
time_start_lasco = '2017-09-10T16:40'
time_end_lasco   = '2017-09-10T17:00'
query_lasco = Fido.search(
    a.Time(time_start_lasco, time_end_lasco),
    a.Instrument('LASCO'),
    a.Source('SOHO'),
    a.Detector('C3')
)
print("\nSOHO LASCO (C3) query results:")
print(query_lasco)
# To download the data, uncomment the following line:
# files_lasco = Fido.fetch(query_lasco)

# Query 4: RHESSI hard X-ray observations during the flare
# The hard X-ray bursts are observed between ~15:50 UT and 16:15 UT on 10 September 2017.
time_start_rhessi = '2017-09-10T15:50'
time_end_rhessi   = '2017-09-10T16:15'
query_rhessi = Fido.search(
    a.Time(time_start_rhessi, time_end_rhessi),
    a.Instrument('RHESSI'),
    a.Source('RHESSI')
)
print("\nRHESSI query results:")
print(query_rhessi)
# To download the data, uncomment the following line:
# files_rhessi = Fido.fetch(query_rhessi)

# Query 5: STEREO-A SECCHI (EUVI) coronagraph observations of CME1 and CME2
# Covering the time interval on 9 September 2017 from ~19:00 UT to ~23:59 UT.
time_start_secchi = '2017-09-09T19:00'
time_end_secchi   = '2017-09-09T23:59'
query_secchi = Fido.search(
    a.Time(time_start_secchi, time_end_secchi),
    a.Instrument('SECCHI'),
    a.Source('STEREO_A'),
    a.Detector('EUVI')
)
print("\nSTEREO-A SECCHI (EUVI) query results:")
print(query_secchi)
# To download the data, uncomment the following line:
# files_secchi = Fido.fetch(query_secchi)

if __name__ == '__main__':
    print("\nAll queries have been executed. Review the printed query results above.")
