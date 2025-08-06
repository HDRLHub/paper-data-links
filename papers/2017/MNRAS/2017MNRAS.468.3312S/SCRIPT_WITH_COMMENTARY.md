# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the SOHO/GOLF helioseismic radial velocity data
(LOS_velocity) from the VSO using SunPy. It fetches approximately 23 days
of data, matching the duration used in the referenced study.
"""

import sunpy.net.dataretriever.client as drclient  # for reference, not used directly
from sunpy.net import Fido, attrs as a
from sunpy.time import parse_time

# -----------------------------------------------------------------------------
# 1. Define the time range for the 23-day helioseismic time series
#    The study uses ~23 days of consecutive data at 60 s cadence.
#    Here we select an example 23-day window.
# -----------------------------------------------------------------------------
start_time = parse_time("2005-01-01T00:00:00")
end_time   = parse_time("2005-01-24T00:00:00")

time_query = a.Time(start_time, end_time)

# -----------------------------------------------------------------------------
# 2. Specify the instrument and observational parameters from the VSO interface
# -----------------------------------------------------------------------------
source_query     = a.Source("SOHO")
instrument_query = a.Instrument("GOLF")
detector_query   = a.Detector("Fsmain")
physobs_query    = a.Physobs("LOS_velocity")

# -----------------------------------------------------------------------------
# 3. Perform the search using Fido
# -----------------------------------------------------------------------------
print("Querying VSO for SOHO/GOLF helioseismic velocity data...")
query_result = Fido.search(time_query,
                           source_query,
                           instrument_query,
                           detector_query,
                           physobs_query)

# -----------------------------------------------------------------------------
# 4. Display the results
# -----------------------------------------------------------------------------
print("Search results:")
print(query_result)

# -----------------------------------------------------------------------------
# 5. Fetch the data (commented out)
# -----------------------------------------------------------------------------
# Uncomment the line below to download the files to your local machine.
# files = Fido.fetch(query_result)
# print("Downloaded files:")
# print(files)
# -----------------------------------------------------------------------------
