# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
#!/usr/bin/env python3
"""
Sunpy VSO Query Script for LASCO C2 and C3 Data
Context: White light images from SOHO/LASCO for June 17, 2016 and tracking path from June 8–21, 2016.
"""

# Import the Fido client and VSO attributes
from sunpy.net import Fido
from sunpy.net.vso.attrs import Source, Instrument, Detector, Time

# ---------------------------------------------------------------------------
# Query 1: LASCO C3 image on 17 June 2016 at 06:30 UT
# ---------------------------------------------------------------------------
time_c3_single = Time('2016-06-17 06:30:00', '2016-06-17 06:30:00')
source_soho   = Source('SOHO')
instrument_l  = Instrument('LASCO')
detector_c3   = Detector('C3')

# Build the query
query_c3 = Fido.search(time_c3_single,
                       source_soho,
                       instrument_l,
                       detector_c3)

# Print the search results for verification
print("=== Query Results: LASCO C3 on 2016-06-17 06:30 UT ===")
print(query_c3)

# To download the data, uncomment the following line:
# files_c3 = Fido.fetch(query_c3)



# ---------------------------------------------------------------------------
# Query 2: LASCO C2 image on 17 June 2016 at 06:36 UT
# ---------------------------------------------------------------------------
time_c2_single = Time('2016-06-17 06:36:00', '2016-06-17 06:36:00')
detector_c2    = Detector('C2')

# Build the query
query_c2 = Fido.search(time_c2_single,
                       source_soho,
                       instrument_l,
                       detector_c2)

# Print the search results for verification
print("\n=== Query Results: LASCO C2 on 2016-06-17 06:36 UT ===")
print(query_c2)

# To download the data, uncomment the following line:
# files_c2 = Fido.fetch(query_c2)



# ---------------------------------------------------------------------------
# Query 3: LASCO C3 images for the Crab nebula path from 8–21 June 2016
# ---------------------------------------------------------------------------
time_path = Time('2016-06-08', '2016-06-21')
# Reuse source_soho, instrument_l, detector_c3

# Build the query
query_path = Fido.search(time_path,
                         source_soho,
                         instrument_l,
                         detector_c3)

# Print the search results for verification
print("\n=== Query Results: LASCO C3 from 2016-06-08 to 2016-06-21 ===")
print(query_path)

# To download the data, uncomment the following line:
# files_path = Fido.fetch(query_path)
```
