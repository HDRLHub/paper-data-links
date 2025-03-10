# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client to query SOHO/LASCO data for a study 
of coronal mass ejections (CMEs) recorded from 1996 to mid‐2017. The paper 
focuses on LASCO observations (specifically the C2 and C3 coronagraphs) that 
provide height–time measurements of CMEs.

Note:
- We query data from the LASCO instrument on board SOHO.
- The detectors C2 and C3 are selected because they cover the extended 
  field of view used in the study.
- The time range is set from January 1, 1996 to June 30, 2017 to match 
  the study period.
- Fido.fetch commands are provided as comments; they will download the data 
  if uncommented.
"""

# Import the necessary modules from sunpy.net
from sunpy.net import Fido, attrs as a

# Define the time range using the study period: 1996 to mid-2017
start_time = "1996-01-01"
end_time = "2017-06-30"

# Query for LASCO C2 data from SOHO
# The SOHO/LASCO C2 coronagraph is used to capture images of the outer corona,
# providing key height–time data for CME kinematics.
query_c2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print the query results for LASCO C2 data
print("Query results for LASCO C2 data:")
print(query_c2)

# Query for LASCO C3 data from SOHO
# The SOHO/LASCO C3 coronagraph complements C2 by extending the field of view 
# out to 32 solar radii, capturing the later stages of CME propagation.
query_c3 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)

# Print the query results for LASCO C3 data
print("Query results for LASCO C3 data:")
print(query_c3)

# To download the data, uncomment the following Fido.fetch commands:
# fetched_c2 = Fido.fetch(query_c2)
# fetched_c3 = Fido.fetch(query_c3)

if __name__ == '__main__':
    # This main block is provided for script execution purposes.
    # The queries are executed when the script is run.
    pass
