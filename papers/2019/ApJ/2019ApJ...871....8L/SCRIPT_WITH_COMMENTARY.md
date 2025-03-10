# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query for solar observations related to the CME-driven shock on 2017 September 10.
It queries three instruments that observed the event:
    1. GOES 16: Provided early-stage EUV imaging at 131 Å and 195 Å.
    2. SOHO: Provided white-light coronagraph images of the CME and its shock.
    3. STEREO A: Provided complementary white-light imaging from a different vantage point.

The only required parameters for these queries are the time range and instrument name.
For GOES 16 and STEREO A, we further specify the satellite source.
"""

from sunpy.net import Fido, attrs as a

# Define the time range for the data query based on the early eruption imaging (~16:42 UT on September 10, 2017).
start_time = '2017-09-10T16:42:00'
end_time = '2017-09-10T16:45:00'

# ------------------------------
# Query 1: GOES 16 observations
# ------------------------------
# GOES 16 provided high-temperature EUV images in channels 131 Å and 195 Å.
# While wavelength constraints are available, here the query uses only the required time and instrument attributes.
query_goes = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('goes'),
    a.Source('goes16')
)
print("GOES 16 Query Result:")
print(query_goes)

# ------------------------------
# Query 2: SOHO observations
# ------------------------------
# SOHO delivered white-light coronagraph imaging which captured the CME and its shock.
query_soho = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('soho')
)
print("SOHO Query Result:")
print(query_soho)

# ------------------------------
# Query 3: STEREO A observations
# ------------------------------
# STEREO A provided complementary white-light coronagraph imaging from a different vantage point.
query_stereo = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('stereo'),
    a.Source('stereo_a')
)
print("STEREO A Query Result:")
print(query_stereo)

# ------------------------------
# Download data (commented out)
# ------------------------------
# To fetch the files from the queries above, uncomment the following lines:
# files_goes = Fido.fetch(query_goes)
# files_soho = Fido.fetch(query_soho)
# files_stereo = Fido.fetch(query_stereo)

if __name__ == "__main__":
    print("VSO queries executed. Review the printed query results for details.")
