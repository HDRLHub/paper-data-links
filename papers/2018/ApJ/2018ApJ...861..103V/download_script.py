# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query observational data relevant for the study of streamer-blowout CMEs (SBOs).
We are querying two sets of SOHO LASCO observations (C2 and C3) covering the period of January 1996 to December 2015,
and a set of SDO/AIA observations for 2011 (in the 304 Å channel) used for comparison with prominence eruptions.
Note: The actual data download commands (Fido.fetch) are commented out.
"""

from sunpy.net import Fido, attrs as a
from astropy import units as u

# -------------------------
# Query 1: SOHO LASCO/C2 observations (white-light coronagraph imaging) from 1996 to 2015
# LASCO/C2 images are used to study streamer swelling and depletion.
start_time_lasco = "1996-01-01T00:00:00"
end_time_lasco = "2015-12-31T23:59:59"
query_lasco_c2 = Fido.search(
    a.Time(start_time_lasco, end_time_lasco),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Physobs("intensity")
)
print("Query Result for SOHO LASCO/C2 (1996 - 2015):")
print(query_lasco_c2)

# Uncomment the following line to fetch LASCO/C2 data
# lasco_c2_files = Fido.fetch(query_lasco_c2)

# -------------------------
# Query 2: SOHO LASCO/C3 observations (white-light coronagraph imaging) from 1996 to 2015
# LASCO/C3 images provide measurements of CME final speeds for kinetic energy estimations.
query_lasco_c3 = Fido.search(
    a.Time(start_time_lasco, end_time_lasco),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3"),
    a.Physobs("intensity")
)
print("\nQuery Result for SOHO LASCO/C3 (1996 - 2015):")
print(query_lasco_c3)

# Uncomment the following line to fetch LASCO/C3 data
# lasco_c3_files = Fido.fetch(query_lasco_c3)

# -------------------------
# Query 3: SDO/AIA observations for the year 2011 used to compare prominence eruptions (PEs)
# We select the 304 Å channel as it is commonly used to observe chromospheric features and prominence eruptions.
start_time_aia = "2011-01-01T00:00:00"
end_time_aia = "2011-12-31T23:59:59"
query_aia_304 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(304 * u.AA),
    a.Physobs("intensity")
)
print("\nQuery Result for SDO/AIA 304 Å (2011):")
print(query_aia_304)

# Uncomment the following line to fetch SDO/AIA data
# aia_304_files = Fido.fetch(query_aia_304)

if __name__ == '__main__':
    print("\nSunPy VSO queries have been executed. Review the printed query results for details.")
