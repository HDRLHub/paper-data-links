# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query remote‐sensing data for a CME event as described
in the context. In this example we construct several queries for white‐light coronagraph and 
heliospheric imager observations. Note that the Fido.fetch commands are commented out so that 
no data are actually downloaded.

The instruments and observation times were chosen to reflect the data used in the paper:
    • LASCO C2: first detection of the CME in white-light at 12:36 UT on 3 November 2010.
    • LASCO C3: early and later observations on 3 and 4 November 2010.
    • STEREO SECCHI COR2 (STEREO-A): CME propagation on 3 November 2010.
    • STEREO SECCHI HI1: entry times for STEREO-A (3:29 UT) and STEREO-B (4:49 UT) on 4 November 2010.
    • STEREO SECCHI HI2: CME first appearance at 10:10 UT on 5 November 2010.
    
Only the time ranges and instrument (plus detector when distinct) keywords are required.
We assume the available VSO interface supports these queries (see provided vso_interface).

Note: Do not run Fido.fetch commands in this script.
"""

from sunpy.net import Fido, attrs as a  # Import Fido and attributes

# -------------------------------------------------------------------
# 1. Query for LASCO C2 (SOHO) - first detection at 12:36 UT on 3 November 2010.
time_start = "2010-11-03T12:30:00"
time_end   = "2010-11-03T12:45:00"
query_c2 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("Query results for LASCO C2 (SOHO) between {} and {}:".format(time_start, time_end))
print(query_c2)
# To download the data, uncomment the following line:
# files_c2 = Fido.fetch(query_c2)

# -------------------------------------------------------------------
# 2. Query for LASCO C3 (SOHO) - initial observation on 3 November 2010 at ~14:06 UT.
time_start = "2010-11-03T14:00:00"
time_end   = "2010-11-03T14:10:00"
query_c3_initial = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("\nQuery results for LASCO C3 (Initial observation) between {} and {}:".format(time_start, time_end))
print(query_c3_initial)
# To download the data, uncomment the following line:
# files_c3_initial = Fido.fetch(query_c3_initial)

# -------------------------------------------------------------------
# 3. Query for LASCO C3 (SOHO) - mass determination between 4 UT and 6 UT on 4 November 2010.
time_start = "2010-11-04T04:00:00"
time_end   = "2010-11-04T06:00:00"
query_c3_mass = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("\nQuery results for LASCO C3 (Mass determination) between {} and {}:".format(time_start, time_end))
print(query_c3_mass)
# To download the data, uncomment the following line:
# files_c3_mass = Fido.fetch(query_c3_mass)

# -------------------------------------------------------------------
# 4. Query for STEREO-A SECCHI COR2 - CME imaging on 3 November 2010.
# Although explicit times are not provided, we use the event date.
time_start = "2010-11-03T00:00:00"
time_end   = "2010-11-03T23:59:59"
query_cor2 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("\nQuery results for STEREO-A SECCHI COR2 on 3 November 2010:")
print(query_cor2)
# To download the data, uncomment the following line:
# files_cor2 = Fido.fetch(query_cor2)

# -------------------------------------------------------------------
# 5. Query for STEREO-A SECCHI HI1 - CME enters field-of-view at 3:29 UT on 4 November 2010.
time_start = "2010-11-04T03:25:00"
time_end   = "2010-11-04T03:35:00"
query_hi1_a = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("HI1")
)
print("\nQuery results for STEREO-A SECCHI HI1 between {} and {}:".format(time_start, time_end))
print(query_hi1_a)
# To download the data, uncomment the following line:
# files_hi1_a = Fido.fetch(query_hi1_a)

# -------------------------------------------------------------------
# 6. Query for STEREO-B SECCHI HI1 - CME enters field-of-view at 4:49 UT on 4 November 2010.
time_start = "2010-11-04T04:45:00"
time_end   = "2010-11-04T04:55:00"
query_hi1_b = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("HI1")
)
print("\nQuery results for STEREO-B SECCHI HI1 between {} and {}:".format(time_start, time_end))
print(query_hi1_b)
# To download the data, uncomment the following line:
# files_hi1_b = Fido.fetch(query_hi1_b)

# -------------------------------------------------------------------
# 7. Query for STEREO-A SECCHI HI2 - CME first visible at 10:10 UT on 5 November 2010.
time_start = "2010-11-05T10:00:00"
time_end   = "2010-11-05T10:20:00"
query_hi2_a = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("HI2")
)
print("\nQuery results for STEREO-A SECCHI HI2 between {} and {}:".format(time_start, time_end))
print(query_hi2_a)
# To download the data, uncomment the following line:
# files_hi2_a = Fido.fetch(query_hi2_a)

# -------------------------------------------------------------------
# 8. Query for STEREO-B SECCHI HI2 - CME first visible at 10:10 UT on 5 November 2010.
time_start = "2010-11-05T10:00:00"
time_end   = "2010-11-05T10:20:00"
query_hi2_b = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("HI2")
)
print("\nQuery results for STEREO-B SECCHI HI2 between {} and {}:".format(time_start, time_end))
print(query_hi2_b)
# To download the data, uncomment the following line:
# files_hi2_b = Fido.fetch(query_hi2_b)

# End of script.
if __name__ == "__main__":
    print("\nAll queries have been executed and printed. To download data, uncomment the Fido.fetch lines.")
