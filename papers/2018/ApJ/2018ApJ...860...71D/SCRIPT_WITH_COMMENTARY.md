# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script builds two SunPy VSO queries to obtain data from instruments that are available in the provided VSO interface.
We query:
  1. SDO/AIA data from the Atmospheric Imaging Assembly. In this example we choose a common EUV wavelength - 304 Å,
     and set the time range around the time of the CME onset on 2014 May 25.
  2. SOHO/LASCO data from two detectors (C2 and C3). These data cover the CME detection period starting at 2014 May 25 (10:00 UT)
     through early May 26.
Note: The VSO interface provided only includes SDO/AIA and SOHO/LASCO, so we restrict our queries to these missions.
The Fido.fetch commands are commented out so that this script only prints the query results.
"""

from sunpy.net import Fido, attrs as a

# Query 1: SDO/AIA data
# Time range chosen: 2014-05-25T00:00:00 to 2014-05-26T00:00:00
# Instrument: AIA (on board SDO) with a typical wavelength (304 Å)
time_aia = a.Time("2014-05-25T00:00:00", "2014-05-26T00:00:00")
instrument_aia = a.Instrument("AIA")
source_aia = a.Source("SDO")
wavelength_aia = a.Wavelength(304 * 1e-10, 304 * 1e-10)  # 304 Å converted to meters if needed; SunPy often accepts Angstrom directly.
print("Querying SDO/AIA data ...")
aia_query = Fido.search(time_aia, source_aia, instrument_aia, wavelength_aia)
print(aia_query)

# Uncomment the following line to fetch the SDO/AIA data:
# aia_files = Fido.fetch(aia_query)

# Query 2: SOHO/LASCO C2 data
# Time range chosen: 2014-05-25T10:00:00 to 2014-05-26T00:00:00.
# Instrument: LASCO (on board SOHO) with Detector: C2.
time_lasco = a.Time("2014-05-25T10:00:00", "2014-05-26T00:00:00")
instrument_lasco = a.Instrument("LASCO")
source_lasco = a.Source("SOHO")
detector_c2 = a.Detector("C2")
print("\nQuerying SOHO/LASCO C2 data ...")
lasco_c2_query = Fido.search(time_lasco, source_lasco, instrument_lasco, detector_c2)
print(lasco_c2_query)

# Uncomment the following line to fetch the SOHO/LASCO C2 data:
# lasco_c2_files = Fido.fetch(lasco_c2_query)

# Query 3: SOHO/LASCO C3 data
# Using the same time range, but with Detector: C3.
detector_c3 = a.Detector("C3")
print("\nQuerying SOHO/LASCO C3 data ...")
lasco_c3_query = Fido.search(time_lasco, source_lasco, instrument_lasco, detector_c3)
print(lasco_c3_query)

# Uncomment the following line to fetch the SOHO/LASCO C3 data:
# lasco_c3_files = Fido.fetch(lasco_c3_query)

if __name__ == "__main__":
    print("VSO queries have been executed and results printed. Adjust time ranges or parameters as needed for further analysis.")
