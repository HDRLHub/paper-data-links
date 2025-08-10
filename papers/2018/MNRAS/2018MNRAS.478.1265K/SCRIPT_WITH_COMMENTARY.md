# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates several SunPy VSO queries using the Fido interface.
It is constructed based on the instrumentation and time ranges described in the paper.
We focus on three instruments onboard SOHO:
  1. LASCO C3 for the spallation event on 29 November 2015.
  2. LASCO C2 for observations during the double X-type flare on 6 and 9 September 2017.
  3. EIT (Extreme Ultraviolet Imaging Telescope) for general context of solar imaging.
  
Note: The Fido.fetch calls are provided but commented out as per instruction.
"""

# Import required modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
from datetime import datetime

# ----------------------------
# Query 1: LASCO C3 spallation event on 29 November 2015
# ----------------------------
# Define the time window: 11:30 UT on 29 November 2015.
start_time_c3 = "2015-11-29T11:30:00"
end_time_c3   = "2015-11-29T11:31:00"

# Create the query for LASCO C3 data.
# Using SOHO LASCO instrument with Detector "C3".
query_lasco_c3 = Fido.search(
    a.Time(start_time_c3, end_time_c3),
    a.Instrument("LASCO"),         # Instrument: LASCO
    a.Detector("C3"),              # Detector: C3 (as per VSO interface available instruments)
    a.Source("SOHO")               # Source: SOHO
)

print("Query Results for LASCO C3 (Spallation event on 29 November 2015):")
print(query_lasco_c3)

# To fetch the data, uncomment the next line:
# files_c3 = Fido.fetch(query_lasco_c3)


# ----------------------------
# Query 2: LASCO C2 observations for double X-type flare events in 2017
# ----------------------------
# For the disk event on 6 September 2017:
start_time_c2_disk = "2017-09-06T00:00:00"
end_time_c2_disk   = "2017-09-06T23:59:59"

query_lasco_c2_disk = Fido.search(
    a.Time(start_time_c2_disk, end_time_c2_disk),
    a.Instrument("LASCO"),         # Instrument: LASCO
    a.Detector("C2"),              # Detector: C2 for the disk event observations
    a.Source("SOHO")               # Source: SOHO
)

print("\nQuery Results for LASCO C2 (Disk event on 6 September 2017):")
print(query_lasco_c2_disk)

# For the limb event on 9 September 2017:
start_time_c2_limb = "2017-09-09T00:00:00"
end_time_c2_limb   = "2017-09-09T23:59:59"

query_lasco_c2_limb = Fido.search(
    a.Time(start_time_c2_limb, end_time_c2_limb),
    a.Instrument("LASCO"),         # Instrument: LASCO
    a.Detector("C2"),              # Detector: C2 for the limb event observations
    a.Source("SOHO")               # Source: SOHO
)

print("\nQuery Results for LASCO C2 (Limb event on 9 September 2017):")
print(query_lasco_c2_limb)

# To fetch the data, uncomment the following lines:
# files_c2_disk = Fido.fetch(query_lasco_c2_disk)
# files_c2_limb = Fido.fetch(query_lasco_c2_limb)

# ----------------------------
# Query 3: EIT observations for general solar imaging
# ----------------------------
# Here we select a sample day within the EIT operational period.
start_time_eit = "2016-01-01T00:00:00"
end_time_eit   = "2016-01-01T23:59:59"

query_eit = Fido.search(
    a.Time(start_time_eit, end_time_eit),
    a.Instrument("EIT"),           # Instrument: EIT (Extreme Ultraviolet Imaging Telescope)
    a.Source("SOHO")               # Source: SOHO
)

print("\nQuery Results for EIT (General solar imaging on 1 January 2016):")
print(query_eit)

# To fetch the data, uncomment the next line:
# files_eit = Fido.fetch(query_eit)

if __name__ == "__main__":
    # This block can be used to further process or analyze the queried data.
    # For now, we only print the query results.
    pass
