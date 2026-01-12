# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy's VSO interface (Fido) to query multiple instruments
that observed the CME on 12 December 2008. The queries reflect the instrument
usage described in the paper’s context, including:

  - SECCHI/COR1-A (STEREO_A) at 04:35 UT for early low-corona imaging.
  - SECCHI/COR1-B (STEREO_B) at 04:55 UT for a complementary low-corona view.
  - SOHO/LASCO-C3 for extended outer-corona imaging around 12:00 UT.
  - SOHO/LASCO-C2 for imaging during the GCS model fitting around 12:07 UT.
  - SECCHI/EUVI-A (STEREO_A) at 03:00 UT with 304 Å to view the associated prominence eruption.
  - SECCHI/COR2-A (STEREO_A) and SECCHI/COR2-B (STEREO_B) for mid-corona 3D geometry imaging around 12:07 UT.

Note: The Fido.fetch commands are commented out. The code prints the query results.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query 1: SECCHI/COR1-A (STEREO_A)
# Time Range: 04:35 UT on 12 December 2008
query_cor1_a = Fido.search(
    a.Time("2008-12-12T04:35:00", "2008-12-12T04:36:00"),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)
print("Query Result for SECCHI/COR1-A (STEREO_A):")
print(query_cor1_a)
# To download the data, uncomment the following line:
# files_cor1_a = Fido.fetch(query_cor1_a)

# Query 2: SECCHI/COR1-B (STEREO_B)
# Time Range: 04:55 UT on 12 December 2008
query_cor1_b = Fido.search(
    a.Time("2008-12-12T04:55:00", "2008-12-12T04:56:00"),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)
print("Query Result for SECCHI/COR1-B (STEREO_B):")
print(query_cor1_b)
# To download the data, uncomment the following line:
# files_cor1_b = Fido.fetch(query_cor1_b)

# Query 3: SOHO/LASCO-C3
# Time Range: Approximately around 12:00 UT to 12:30 UT on 12 December 2008,
# capturing the extended outer-corona CME evolution.
query_lasco_c3 = Fido.search(
    a.Time("2008-12-12T12:00:00", "2008-12-12T12:30:00"),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("Query Result for SOHO/LASCO-C3:")
print(query_lasco_c3)
# To download the data, uncomment the following line:
# files_lasco_c3 = Fido.fetch(query_lasco_c3)

# Query 4: SOHO/LASCO-C2
# Time Range: Around 12:07 UT on 12 December 2008,
# used for the GCS forward-model fitting.
query_lasco_c2 = Fido.search(
    a.Time("2008-12-12T12:07:00", "2008-12-12T12:08:00"),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("Query Result for SOHO/LASCO-C2:")
print(query_lasco_c2)
# To download the data, uncomment the following line:
# files_lasco_c2 = Fido.fetch(query_lasco_c2)

# Query 5: SECCHI/EUVI-A (STEREO_A)
# Time Range: 03:00 UT on 12 December 2008, observing the prominence eruption at 304 Å.
query_euvi_a = Fido.search(
    a.Time("2008-12-12T03:00:00", "2008-12-12T03:10:00"),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    a.Wave(304*u.AA)
)
print("Query Result for SECCHI/EUVI-A (STEREO_A):")
print(query_euvi_a)
# To download the data, uncomment the following line:
# files_euvi_a = Fido.fetch(query_euvi_a)

# Query 6: SECCHI/COR2-A (STEREO_A)
# Time Range: Around 12:07 UT on 12 December 2008,
# capturing mid-coronal imaging for 3D CME reconstruction.
query_cor2_a = Fido.search(
    a.Time("2008-12-12T12:07:00", "2008-12-12T12:08:00"),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("Query Result for SECCHI/COR2-A (STEREO_A):")
print(query_cor2_a)
# To download the data, uncomment the following line:
# files_cor2_a = Fido.fetch(query_cor2_a)

# Query 7: SECCHI/COR2-B (STEREO_B)
# Time Range: Around 12:07 UT on 12 December 2008,
# providing the complementary mid-corona view for 3D reconstruction.
query_cor2_b = Fido.search(
    a.Time("2008-12-12T12:07:00", "2008-12-12T12:08:00"),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("Query Result for SECCHI/COR2-B (STEREO_B):")
print(query_cor2_b)
# To download the data, uncomment the following line:
# files_cor2_b = Fido.fetch(query_cor2_b)

if __name__ == "__main__":
    # The script prints all query results when run.
    pass
