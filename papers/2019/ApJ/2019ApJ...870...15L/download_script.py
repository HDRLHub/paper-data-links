# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy's VSO client to query AIA (SDO) data for selected events in June 2015.
The queries focus on the time intervals and instrument used in the study:
  - Event 1 (2015 June 22): from 17:49 UT to 18:23 UT
  - Event 2 (2015 June 21): from 01:37 UT to 02:10 UT
  - Event 3 (2015 June 25): from 08:10 UT to 08:20 UT

Only the required parameters (time range and instrument) are specified.
Additional keywords such as source and physical observable are included to reflect the instrument's usage.
Feel free to uncomment the Fido.fetch commands to download the data.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs as a

# -------------------------- Event 1 --------------------------
# 2015 June 22 Event: AIA observed data from approximately 17:49 UT to 18:23 UT.
time_event1 = a.Time("2015-06-22T17:49:00", "2015-06-22T18:23:00")
instrument_aia = a.Instrument("AIA")
source_sdo = a.Source("SDO")
physobs_intensity = a.Physobs("intensity")

# Build the query for Event 1
result_event1 = Fido.search(time_event1, instrument_aia, source_sdo, physobs_intensity)
print("Event 1 (2015-06-22) AIA Query Result:")
print(result_event1)
# To download the data for Event 1, uncomment the line below:
# files_event1 = Fido.fetch(result_event1)

# -------------------------- Event 2 --------------------------
# 2015 June 21 Event: AIA observed data from approximately 01:37 UT to 02:10 UT.
time_event2 = a.Time("2015-06-21T01:37:00", "2015-06-21T02:10:00")

# Build the query for Event 2 using the same instrument parameters
result_event2 = Fido.search(time_event2, instrument_aia, source_sdo, physobs_intensity)
print("Event 2 (2015-06-21) AIA Query Result:")
print(result_event2)
# To download the data for Event 2, uncomment the line below:
# files_event2 = Fido.fetch(result_event2)

# -------------------------- Event 3 --------------------------
# 2015 June 25 Event: AIA observed data from approximately 08:10 UT to 08:20 UT.
time_event3 = a.Time("2015-06-25T08:10:00", "2015-06-25T08:20:00")

# Build the query for Event 3 using the same instrument parameters
result_event3 = Fido.search(time_event3, instrument_aia, source_sdo, physobs_intensity)
print("Event 3 (2015-06-25) AIA Query Result:")
print(result_event3)
# To download the data for Event 3, uncomment the line below:
# files_event3 = Fido.fetch(result_event3)

# End of script
