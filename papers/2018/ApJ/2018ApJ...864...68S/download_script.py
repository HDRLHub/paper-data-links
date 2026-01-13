# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client (Fido) to query solar data that were used in the study.
The paper investigated the evolution of active regions, including filament formation and eruption,
by analyzing SDO’s AIA images (multiple EUV channels) and HMI magnetograms, as well as CME observations with SOHO/LASCO/C2.
Below, we construct separate queries for two events:
  1. The 2013 October event (filament formation and eruption in AR 11868):
     • AIA: Filament formation – October 18, 2013 (10:00 UT to 16:00 UT)
     • HMI: Magnetic evolution – October 15, 2013 14:00 UT to October 20, 2013 09:00 UT
  2. The 2010 July event (coronal and magnetic evolution in AR 11088):
     • AIA: Selected short time period on July 15, 2010 to capture coronal evolution
     • HMI: Full period covering emergence to eruption from July 11, 2010 to July 16, 2010
  3. The CME observation from SOHO/LASCO/C2 on October 20, 2013:
     • LASCO/C2: CME visible in white-light coronagraph images between 09:00 UT and 10:00 UT.
  
Note:
  - Only instruments available in the VSO interface are queried:
       SDO/AIA, SDO/HMI, and SOHO/LASCO (C2 detector).
  - Fido.fetch lines (which actually download the data) are provided as comments.
"""

from sunpy.net import Fido, attrs as a

# ----------------------------
# Query 1: SDO/AIA for 2013 October filament formation
# Time range: October 18, 2013 from 10:00 UT to 16:00 UT
start_time_aia_oct = "2013-10-18T10:00:00"
end_time_aia_oct = "2013-10-18T16:00:00"
query_aia_oct = Fido.search(
    a.Time(start_time_aia_oct, end_time_aia_oct),
    a.Instrument("AIA"),
    a.Source("SDO")
)
print("SDO/AIA October 18, 2013 query results:")
print(query_aia_oct)

# To download the data, uncomment the next line:
# aia_oct_files = Fido.fetch(query_aia_oct)

# ----------------------------
# Query 2: SDO/HMI for 2013 October magnetic evolution
# Time range: October 15, 2013 14:00 UT to October 20, 2013 09:00 UT
start_time_hmi_oct = "2013-10-15T14:00:00"
end_time_hmi_oct = "2013-10-20T09:00:00"
query_hmi_oct = Fido.search(
    a.Time(start_time_hmi_oct, end_time_hmi_oct),
    a.Instrument("HMI"),
    a.Source("SDO")
)
print("\nSDO/HMI October 2013 query results:")
print(query_hmi_oct)

# To download the data, uncomment the next line:
# hmi_oct_files = Fido.fetch(query_hmi_oct)

# ----------------------------
# Query 3: SDO/AIA for 2010 July coronal evolution
# Time range: A short period on July 15, 2010 to capture key AIA imagery
start_time_aia_jul = "2010-07-15T14:50:00"
end_time_aia_jul = "2010-07-15T15:55:00"
query_aia_jul = Fido.search(
    a.Time(start_time_aia_jul, end_time_aia_jul),
    a.Instrument("AIA"),
    a.Source("SDO")
)
print("\nSDO/AIA July 15, 2010 query results:")
print(query_aia_jul)

# To download the data, uncomment the next line:
# aia_jul_files = Fido.fetch(query_aia_jul)

# ----------------------------
# Query 4: SDO/HMI for 2010 July magnetic evolution
# Time range: July 11, 2010 to July 16, 2010 to cover emergence until eruption
start_time_hmi_jul = "2010-07-11T00:00:00"
end_time_hmi_jul = "2010-07-16T23:59:00"
query_hmi_jul = Fido.search(
    a.Time(start_time_hmi_jul, end_time_hmi_jul),
    a.Instrument("HMI"),
    a.Source("SDO")
)
print("\nSDO/HMI July 2010 query results:")
print(query_hmi_jul)

# To download the data, uncomment the next line:
# hmi_jul_files = Fido.fetch(query_hmi_jul)

# ----------------------------
# Query 5: SOHO/LASCO/C2 for CME observations during the 2013 October event
# Time range: October 20, 2013 from 09:00 UT to 10:00 UT
start_time_lasco = "2013-10-20T09:00:00"
end_time_lasco = "2013-10-20T10:00:00"
query_lasco = Fido.search(
    a.Time(start_time_lasco, end_time_lasco),
    a.Instrument("LASCO"),
    a.Source("SOHO"),
    a.detector("C2")
)
print("\nSOHO/LASCO/C2 October 20, 2013 query results:")
print(query_lasco)

# To download the data, uncomment the next line:
# lasco_files = Fido.fetch(query_lasco)

if __name__ == '__main__':
    print("\nQueries completed. Review the query results printed above.")
    print("To download data, uncomment the Fido.fetch lines as required.")
