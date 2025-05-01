# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query SOHO/LASCO data,
specifically targeting the LASCO C2 detector data which is available
from 1995-12-08 to present. In our study (from December 2006 to June 2015),
we use LASCO data to identify CME events in the outer corona.

Note:
- The query uses a time range covering December 2006 to June 2015.
- The instrument is specified as LASCO with a detector "C2" (from SOHO).
- The Fido.fetch command is provided in a commented section,
  so you can enable it after verifying the query results.
"""

from sunpy.net import Fido, attrs as a

# Define the time range corresponding to the study period (Dec 2006 - Jun 2015)
start_time = "2006-12-01"
end_time   = "2015-06-30"

# Build the VSO query for SOHO LASCO C2 data
# Here, we specify:
#   - Time: from start_time to end_time.
#   - Source: "SOHO".
#   - Instrument: "LASCO".
#   - Detector: "C2" (covers the period of interest; note that C1 has limited availability)
query = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print out the query results to verify that the search returned expected datasets
print(query)

# If the query returns the desired data, you can proceed to download the files.
# Uncomment the following line to fetch the data:
# downloaded_files = Fido.fetch(query)
# print("Data download complete. Files saved:", downloaded_files)

if __name__ == "__main__":
    # The script has been executed successfully if this message is printed.
    print("VSO query executed. Review the output above for query details.")
