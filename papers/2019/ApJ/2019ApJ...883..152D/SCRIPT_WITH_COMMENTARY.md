# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to search for LASCO coronagraph data from SOHO.
In the context of the paper, data from LASCO C2 and C3 on April 30, 2011 are required.
The paper uses LASCO C2 for a face‐on total brightness observation at 16:23:04 UT,
and LASCO C3 for a similar total brightness observation at 16:17:04 UT.
Since the VSO interface only lists SOHO/LASCO detectors (C1, C2, C3),
we restrict our queries to LASCO C2 and LASCO C3, with the time ranges as specified.
Note: The actual downloading step is commented out.
"""

from sunpy.net import Fido, attrs as a

#------------------------------------------------------------------
# Query for SOHO LASCO C2 total brightness observation at 16:23:04 UT
#------------------------------------------------------------------
# Define the time of observation for LASCO C2 total brightness data
time_c2 = a.Time("2011-04-30T16:23:04", "2011-04-30T16:23:04")
# Define the instrument and detector attributes for LASCO C2
instr_c2 = a.Instrument("LASCO")
source_c2 = a.Source("SOHO")
detector_c2 = a.Detector("C2")
physobs = a.Physobs("intensity")  # Total brightness measurement

# Build the query for LASCO C2
print("Querying for SOHO LASCO C2 total brightness observation at 2011-04-30T16:23:04")
query_c2 = Fido.search(time_c2, source_c2, instr_c2, detector_c2, physobs)
print(query_c2)

#------------------------------------------------------------------
# Query for SOHO LASCO C3 total brightness observation at 16:17:04 UT
#------------------------------------------------------------------
# Define the time of observation for LASCO C3 total brightness data
time_c3 = a.Time("2011-04-30T16:17:04", "2011-04-30T16:17:04")
# Define the instrument and detector attributes for LASCO C3
instr_c3 = a.Instrument("LASCO")
source_c3 = a.Source("SOHO")
detector_c3 = a.Detector("C3")
# Use the same physical observable: intensity (total brightness)
  
# Build the query for LASCO C3
print("\nQuerying for SOHO LASCO C3 total brightness observation at 2011-04-30T16:17:04")
query_c3 = Fido.search(time_c3, source_c3, instr_c3, detector_c3, physobs)
print(query_c3)

#------------------------------------------------------------------
# Note: In the scientific paper, polarized brightness (pB) sequences were also used
# for LASCO C2. However, as the VSO interface does not differentiate pB observations
# for LASCO data, and the primary search parameters are time and instrument, we have 
# restricted the queries to the total brightness datasets.
# 
# If pB data were available in the interface, an additional query for pB images
# (e.g., by specifying a different a.Physobs or a custom attribute) would follow the same pattern.
#------------------------------------------------------------------

#------------------------------------------------------------------
# To download the data, one would typically use:
# files_c2 = Fido.fetch(query_c2)
# files_c3 = Fido.fetch(query_c3)
# (Download commands are commented out below to prevent execution)
#------------------------------------------------------------------
# files_c2 = Fido.fetch(query_c2)
# files_c3 = Fido.fetch(query_c3)

if __name__ == "__main__":
    print("\nCompleted VSO queries for SOHO LASCO data.")
