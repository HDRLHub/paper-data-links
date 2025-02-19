# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for white-light coronagraph images of CMEs
obtained by the LASCO instrument on board SOHO. The study specifies a time range from 1996 to
March 2017 for CME analysis. In the VSO interface provided, the LASCO instrument is available with
various detectors. Here we use the "C2" detector (available from 1995/12/08 to present) as it covers
the complete period required by the study for LASCO CME observations.
"""

import sunpy.net as net
from sunpy.net import Fido, attrs as a

# Define the time range for the query corresponding to the study's period for CME observations.
time_start = '1996-01-01'
time_end = '2017-03-31'

# Define the query attributes:
# 1. Time range based on study (1996 to March 2017).
# 2. Source is SOHO.
# 3. Instrument is LASCO.
# 4. Detector is set to "C2" (covers the required full time range).
# 5. Physical observable is "intensity", which corresponds to white-light coronagraph images.
time_attr = a.Time(time_start, time_end)
source_attr = a.Source('SOHO')
instrument_attr = a.Instrument('LASCO')
detector_attr = a.Detector('C2')
physobs_attr = a.Physobs('intensity')

# Build the search query using Fido.search:
query = Fido.search(time_attr,
                    source_attr,
                    instrument_attr,
                    detector_attr,
                    physobs_attr)

# Print out the summary of the query results.
print("Query Results Summary:")
print(query)

# To download the data, uncomment the following lines:
# files = Fido.fetch(query)
# print("Downloaded files:")
# print(files)
