# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query solar data using SunPy's VSO interface.
The queries below are constructed in the context of the recent study of CME–shock and streamer interactions 
associated with GLE events (2017 September 10). We query data from instruments available in the VSO:
  1. SOHO/LASCO (using detector C2) for white-light coronagraph observation at 2017-09-10 16:12:05 UT.
  2. STEREO_A/SECCHI COR1 for two white-light images at 2017-09-10 16:00:18 UT and 2017-09-10 16:05:18 UT.
  3. STEREO_A/SECCHI COR2 for a white-light coronagraph image at 2017-09-10 16:24:00 UT.

Note: The Fido.fetch commands are provided as comments – uncomment them to actually download the data.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

###############################################################################
# Query 1: SOHO/LASCO Coronagraph - Detector C2 at 2017-09-10 16:12:05 UT.
###############################################################################
# We define a short time window around the provided timestamp.
start_time_lasco = "2017-09-10T16:12:05"
end_time_lasco = "2017-09-10T16:15:00"

# Construct query for SOHO source, LASCO instrument with detector C2.
query_lasco = Fido.search(
    a.Time(start_time_lasco, end_time_lasco),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

print("Query Results for SOHO/LASCO C2 (white-light coronagraph image):")
print(query_lasco)

# Uncomment the following line to fetch the data:
# lasco_files = Fido.fetch(query_lasco)

###############################################################################
# Query 2: STEREO_A/SECCHI COR1 Coronagraph - First Image at 2017-09-10 16:00:18 UT.
###############################################################################
start_time_cor1_first = "2017-09-10T16:00:18"
end_time_cor1_first = "2017-09-10T16:02:00"  # small window around the observation time

# Construct query for STEREO_A source, SECCHI instrument with detector COR1.
query_cor1_first = Fido.search(
    a.Time(start_time_cor1_first, end_time_cor1_first),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)

print("\nQuery Results for STEREO_A/SECCHI COR1 (first image):")
print(query_cor1_first)

# Uncomment the following line to fetch the data:
# cor1_first_files = Fido.fetch(query_cor1_first)

###############################################################################
# Query 3: STEREO_A/SECCHI COR1 Coronagraph - Second Image at 2017-09-10 16:05:18 UT.
###############################################################################
start_time_cor1_second = "2017-09-10T16:05:18"
end_time_cor1_second = "2017-09-10T16:07:00"

# Construct query for the second COR1 image.
query_cor1_second = Fido.search(
    a.Time(start_time_cor1_second, end_time_cor1_second),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)

print("\nQuery Results for STEREO_A/SECCHI COR1 (second image):")
print(query_cor1_second)

# Uncomment the following line to fetch the data:
# cor1_second_files = Fido.fetch(query_cor1_second)

###############################################################################
# Query 4: STEREO_A/SECCHI COR2 Coronagraph at 2017-09-10 16:24:00 UT.
###############################################################################
start_time_cor2 = "2017-09-10T16:24:00"
end_time_cor2 = "2017-09-10T16:26:00"

# Construct query for STEREO_A/SECCHI with detector COR2.
query_cor2 = Fido.search(
    a.Time(start_time_cor2, end_time_cor2),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)

print("\nQuery Results for STEREO_A/SECCHI COR2 (white-light coronagraph image):")
print(query_cor2)

# Uncomment the following line to fetch the data:
# cor2_files = Fido.fetch(query_cor2)

###############################################################################
# End of queries.
###############################################################################

if __name__ == '__main__':
    print("\nAll queries have been executed. Review the printed query results above for details.")
