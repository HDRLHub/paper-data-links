# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs several VSO queries using SunPy for the multi-spacecraft observations described in the paper.
Each query is constructed with a specific time range and instrument, based on the context details.

In this example we query:
  • SDO/AIA on 2010/05/30 at 02:32:02 UT (EUV observation in 193 Å for the dark cavity)
  • STEREO-A SECCHI/EUVI on 2010/06/04 at 21:25:30 UT (EUV observation in 195 Å)
  • STEREO-B SECCHI/EUVI on 2010/06/07 at 14:26:02 UT (EUV observation in 195 Å)
  • PROBA2/SWAP for two phases on 2010/06/13 (quiescent phase from 00:00 to 01:35 UT and eruptive phase from 06:30 to 07:20 UT in 174 Å)
  • SOHO LASCO C2 from 2010/06/13 07:31:39 to 10:34:02 UT (white-light coronagraph observation)
  • SOHO LASCO C3 at 2010/06/13 10:41:30 UT (white-light coronagraph observation)
  
Note: The Fido.fetch commands are commented out to avoid accidental data download.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# -------------------------------------------
# Query 1: SDO/AIA east limb observation at 2010/05/30 02:32:02 UT 
# (EUV image at 193 Å for cavity morphology)
query_aia = Fido.search(
    a.Time("2010-05-30T02:32:02", "2010-05-30T02:32:02"),
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Physobs("intensity"),
    a.Wavelength(193 * u.AA)  # 193 Å to capture the dark cavity
)
print("SDO/AIA Query Results:")
print(query_aia)
# To download the data, uncomment the following line:
# fetched_aia = Fido.fetch(query_aia)

# -------------------------------------------
# Query 2: STEREO-A SECCHI/EUVI observation at 2010/06/04 21:25:30 UT 
# (EUV image at 195 Å, complementary to the AIA view)
query_stereo_a = Fido.search(
    a.Time("2010-06-04T21:25:30", "2010-06-04T21:25:30"),
    a.Instrument("SECCHI"),
    a.Source("STEREO_A"),
    a.Detector("EUVI"),
    a.Physobs("intensity"),
    a.Wavelength(195 * u.AA)  # 195 Å is used to observe the cavity and prominence details
)
print("\nSTEREO-A SECCHI/EUVI Query Results:")
print(query_stereo_a)
# To download the data, uncomment the following line:
# fetched_stereo_a = Fido.fetch(query_stereo_a)

# -------------------------------------------
# Query 3: STEREO-B SECCHI/EUVI observation at 2010/06/07 14:26:02 UT 
# (EUV image at 195 Å, providing a different vantage point)
query_stereo_b = Fido.search(
    a.Time("2010-06-07T14:26:02", "2010-06-07T14:26:02"),
    a.Instrument("SECCHI"),
    a.Source("STEREO_B"),
    a.Detector("EUVI"),
    a.Physobs("intensity"),
    a.Wavelength(195 * u.AA)
)
print("\nSTEREO-B SECCHI/EUVI Query Results:")
print(query_stereo_b)
# To download the data, uncomment the following line:
# fetched_stereo_b = Fido.fetch(query_stereo_b)

# -------------------------------------------
# Query 4: PROBA2/SWAP observations on 2010/06/13
# Part A: Quiescent phase observation (00:00 UT to 01:35 UT) in 174 Å
query_swap_quiescent = Fido.search(
    a.Time("2010-06-13T00:00:00", "2010-06-13T01:35:00"),
    a.Instrument("SWAP"),
    a.Source("PROBA2"),
    a.Physobs("intensity"),
    a.Wavelength(174 * u.AA)  # 174 Å is the central wavelength for SWAP observations
)
print("\nPROBA2/SWAP (Quiescent Phase) Query Results:")
print(query_swap_quiescent)
# To download the data, uncomment the following line:
# fetched_swap_quiescent = Fido.fetch(query_swap_quiescent)

# Part B: Eruptive phase observation (06:30 UT to 07:20 UT) in 174 Å
query_swap_eruptive = Fido.search(
    a.Time("2010-06-13T06:30:00", "2010-06-13T07:20:00"),
    a.Instrument("SWAP"),
    a.Source("PROBA2"),
    a.Physobs("intensity"),
    a.Wavelength(174 * u.AA)
)
print("\nPROBA2/SWAP (Eruptive Phase) Query Results:")
print(query_swap_eruptive)
# To download the data, uncomment the following line:
# fetched_swap_eruptive = Fido.fetch(query_swap_eruptive)

# -------------------------------------------
# Query 5: SOHO LASCO C2 white-light coronagraph observation on 2010/06/13
# Time range: from 07:31:39 to 10:34:02 UT
query_lasco_c2 = Fido.search(
    a.Time("2010-06-13T07:31:39", "2010-06-13T10:34:02"),
    a.Instrument("LASCO"),
    a.Source("SOHO"),
    a.Detector("C2"),
    a.Physobs("intensity")
)
print("\nSOHO LASCO C2 Query Results:")
print(query_lasco_c2)
# To download the data, uncomment the following line:
# fetched_lasco_c2 = Fido.fetch(query_lasco_c2)

# -------------------------------------------
# Query 6: SOHO LASCO C3 white-light coronagraph observation at 10:41:30 UT on 2010/06/13
query_lasco_c3 = Fido.search(
    a.Time("2010-06-13T10:41:30", "2010-06-13T10:41:30"),
    a.Instrument("LASCO"),
    a.Source("SOHO"),
    a.Detector("C3"),
    a.Physobs("intensity")
)
print("\nSOHO LASCO C3 Query Results:")
print(query_lasco_c3)
# To download the data, uncomment the following line:
# fetched_lasco_c3 = Fido.fetch(query_lasco_c3)

# End of script
if __name__ == "__main__":
    print("\nAll queries have been executed. Review the printed query results for details.")
