# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query solar observations
for two instruments used in the study described in the context:
1. SOHO/LASCO (specifically, the C2 detector, since its full time range
   covers the date in question) is used to capture white‐light coronagraph
   images of the CME events observed on 2017 September 4.
2. STEREO-A/SECCHI (using the COR2 detector, appropriate for white‐light
   imaging of CMEs) is used to track the evolution of the same CME events
   from 2017 September 3 through September 8.
The queries below specify the time ranges and instruments corresponding
to the observations described in the paper.
Note: The Fido.fetch commands are provided but commented out to avoid
downloading data during script execution.
"""

from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Query 1: SOHO/LASCO - white-light coronagraph observation of CME events
# The paper describes CME-1 and CME-2 first observed on 2017-09-04 around 19:00 UT.
# We select a time range covering this period.
soho_lasco_time = TimeRange("2017-09-04T18:00:00", "2017-09-04T21:00:00")
query_lasco = Fido.search(
    a.Time(soho_lasco_time.start.iso, soho_lasco_time.end.iso),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("SOHO/LASCO Query Results:")
print(query_lasco)

# Uncomment the following line to download the SOHO/LASCO data
# lasco_files = Fido.fetch(query_lasco)

# Query 2: STEREO-A/SECCHI - white-light CME tracking observations 
# The paper uses STEREO-A observations from 2017 September 3 to 2017 September 8
# to track the evolution of CME events. We select the COR2 detector for imaging.
stereo_time = TimeRange("2017-09-03T00:00:00", "2017-09-08T23:59:59")
query_stereo = Fido.search(
    a.Time(stereo_time.start.iso, stereo_time.end.iso),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("\nSTEREO-A/SECCHI (COR2) Query Results:")
print(query_stereo)

# Uncomment the following line to download the STEREO-A/SECCHI data
# stereo_files = Fido.fetch(query_stereo)

if __name__ == "__main__":
    print("\nQueries completed. Review the printed query results for details.")
