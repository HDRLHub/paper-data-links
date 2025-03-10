# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs SunPy VSO queries that reflect the instruments and time ranges discussed in the study.
The study uses UVCS on board SOHO to observe sungrazing comets (Comet C/2002 S2) via HI Lyα emissions.
We have two observation periods:
  1. Observation Period 1: 23:17 UT on 18 September 2002 to 00:16 UT on 19 September 2002.
  2. Observation Period 2: 21:31 UT to 22:22 UT on 18 September 2002.
Note: We use the "UVCS" instrument from SOHO with the detector "LVA" as it covers the wavelength range (1095 – 1360 Å)
which includes HI Lyα. The VSO interface confirms availability of UVCS data from 1996 onwards.
"""

from sunpy.net import Fido, attrs as a

# -------------------------
# Query for UVCS observation period 1
# Time range: 2002-09-18T23:17:00 to 2002-09-19T00:16:00
# Instrument: UVCS on SOHO, with detector LVA (HI Lyα falls within the wavelength coverage)
# -------------------------
time_period1 = a.Time("2002-09-18T23:17:00", "2002-09-19T00:16:00")
source_uvcs = a.Source("SOHO")
instrument_uvcs = a.Instrument("UVCS")
# Specify the detector LVA from the available options in the VSO interface for UVCS.
detector_lva = a.Detector("LVA")

query_result1 = Fido.search(time_period1, source_uvcs, instrument_uvcs, detector_lva)
print("Query Result for UVCS Observation Period 1:")
print(query_result1)

# Uncomment the following line to fetch the data for period 1:
# files1 = Fido.fetch(query_result1)

# -------------------------
# Query for UVCS observation period 2
# Time range: 2002-09-18T21:31:00 to 2002-09-18T22:22:00
# Instrument: UVCS on SOHO, again using the detector LVA
# -------------------------
time_period2 = a.Time("2002-09-18T21:31:00", "2002-09-18T22:22:00")
query_result2 = Fido.search(time_period2, source_uvcs, instrument_uvcs, detector_lva)
print("\nQuery Result for UVCS Observation Period 2:")
print(query_result2)

# Uncomment the following line to fetch the data for period 2:
# files2 = Fido.fetch(query_result2)

# Note: Although instruments like LASCO and AIA (from SDO) are also available in the VSO interface (see vso_interface)
# and are mentioned in the study for contextual purposes, the detailed time ranges provided in the paper are for UVCS.
# Therefore, we explicitly query UVCS based on the required values.
  
if __name__ == "__main__":
    pass
