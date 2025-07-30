# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query data that are relevant for SEP (Solar Energetic Particle) studies.
Based on the context provided, SEP measurements are performed by several instruments (e.g. GOES Energetic Particle Detectors)
which are used to study energetic protons, alpha particles, and heavier ions. Note that many specialized SEP instruments such as
LEMT, SIS, or STEP may not be available via the VSO interface. Therefore, we choose the GOES instrument as a proxy to retrieve
data relevant for SEP events.

The query below uses a fixed time range and the instrument "goes", reflecting the NOAA/GOES energetic particle detectors.
"""

# Import necessary modules from SunPy and Astropy
import sunpy.net.vso as vso
from sunpy.net import Fido, attrs

# Define the time range for the query. Adjust these times as needed for the event of interest.
time_start = '2021-01-01T00:00:00'
time_end = '2021-01-02T00:00:00'

# Construct the VSO query:
# We search for data between the specified times from the GOES instrument.
# Note: Detailed selection (such as energy channels or specific detectors) are beyond the basic
# available VSO query fields. Hence, only time and instrument are provided.
query_result = Fido.search(
    attrs.Time(time_start, time_end),
    attrs.Instrument('goes')
)

# Print the query result to see the details of matched data.
print(query_result)

# To actually fetch the data, you can use Fido.fetch.
# The following line is commented out to prevent automatic downloading.
# downloaded_files = Fido.fetch(query_result)

if __name__ == '__main__':
    print("SEP data query completed. Review the query output above for details.")
