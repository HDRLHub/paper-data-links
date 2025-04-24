# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use SunPy's VSO client (Fido) to query data 
corresponding to several observational events described in the paper.
We query data for:
  1. SDO/AIA observations of the low-corona CME evolution on 2013 September 24 (filament eruption) in the 193 Å passband.
  2. SDO/AIA observations on 2015 February 09 capturing the hot channel eruption,
     with separate queries for the leading edge (193 Å) and hot channel (131 Å).
  3. SDO/AIA snapshot of the hot blob observed on 2017 September 10 (131 Å).
  4. GOES16/SUVI observation on 2017 September 10 of the CME leading edge in the 195 Å channel.
  5. SOHO/LASCO observation (using the C2 detector) on 2013 September 24 capturing 
     the CME’s appearance in white-light.
Note: The queries are printed to inspect the search results and the corresponding 
Fido.fetch commands are provided as comments.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# -----------------------------------------------------------------
# Query 1: SDO/AIA - 2013 September 24 Filament Eruption in 193 Å
# Time Range: 2013-09-24T19:40:00 to 2013-09-24T20:10:00
# Instrument: AIA; Wavelength: 193 Å (within the 191-195 Å range available)
query1 = Fido.search(
    a.Time("2013-09-24T19:40:00", "2013-09-24T20:10:00"),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.AA)
)
print("SDO/AIA Filament Eruption Query (2013-09-24, 193 Å):")
print(query1)
# To download the data for Query 1, uncomment the next line:
# files1 = Fido.fetch(query1)

# -----------------------------------------------------------------
# Query 2a: SDO/AIA - 2015 February 09 Hot Channel Eruption - Leading Edge in 193 Å
# Time Range: 2015-02-09T22:50:00 to 2015-02-09T23:14:00
# Instrument: AIA; Wavelength: 193 Å
query2a = Fido.search(
    a.Time("2015-02-09T22:50:00", "2015-02-09T23:14:00"),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.AA)
)
print("\nSDO/AIA Hot Channel Eruption (2015-02-09) - Leading Edge Query (193 Å):")
print(query2a)
# To download the data for Query 2a, uncomment the next line:
# files2a = Fido.fetch(query2a)

# -----------------------------------------------------------------
# Query 2b: SDO/AIA - 2015 February 09 Hot Channel Eruption - Hot Channel in 131 Å
# Time Range: 2015-02-09T22:50:00 to 2015-02-09T23:14:00
# Instrument: AIA; Wavelength: 131 Å
query2b = Fido.search(
    a.Time("2015-02-09T22:50:00", "2015-02-09T23:14:00"),
    a.Instrument("AIA"),
    a.Wavelength(131 * u.AA)
)
print("\nSDO/AIA Hot Channel Eruption (2015-02-09) - Hot Channel Query (131 Å):")
print(query2b)
# To download the data for Query 2b, uncomment the next line:
# files2b = Fido.fetch(query2b)

# -----------------------------------------------------------------
# Query 3: SDO/AIA - 2017 September 10 Hot Blob Observation in 131 Å
# Time Instance: A narrow window around 15:55 UT to capture the 15:55:06 snapshot
query3 = Fido.search(
    a.Time("2017-09-10T15:55:00", "2017-09-10T15:55:10"),
    a.Instrument("AIA"),
    a.Wavelength(131 * u.AA)
)
print("\nSDO/AIA Hot Blob Observation Query (2017-09-10, 131 Å):")
print(query3)
# To download the data for Query 3, uncomment the next line:
# files3 = Fido.fetch(query3)

# -----------------------------------------------------------------
# Query 4: GOES16/SUVI - 2017 September 10 CME Leading Edge in 195 Å
# Time Range: Approximated from 15:55 UT to 16:05 UT to cover concurrent observations.
query4 = Fido.search(
    a.Time("2017-09-10T15:55:00", "2017-09-10T16:05:00"),
    a.Source("GOES16"),
    a.Instrument("SUVI"),
    a.Wavelength(195 * u.AA)
)
print("\nGOES16/SUVI CME Leading Edge Query (2017-09-10, 195 Å):")
print(query4)
# To download the data for Query 4, uncomment the next line:
# files4 = Fido.fetch(query4)

# -----------------------------------------------------------------
# Query 5: SOHO/LASCO - 2013 September 24 CME Appearance in White-light (C2)
# Time Range: 2013-09-24T20:36:00 to 2013-09-24T20:40:00
# Instrument: LASCO; Detector: C2; For white-light observations the wavelength filter is not used.
query5 = Fido.search(
    a.Time("2013-09-24T20:36:00", "2013-09-24T20:40:00"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nSOHO/LASCO C2 CME Appearance Query (2013-09-24, white-light):")
print(query5)
# To download the data for Query 5, uncomment the next line:
# files5 = Fido.fetch(query5)

if __name__ == "__main__":
    pass
