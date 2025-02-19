# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for SOHO LASCO data.
In this specific query, we search for LASCO observations from SOHO during the period
when SOHO’s coronagraph imagery was used to study near‐Sun comets (approximately 1996 to 2008).
Only the time range and the instrument are specified in this query as per the provided context.

The VSO interface indicates LASCO is available on SOHO with three detectors (C1, C2, C3).
For this query we simply specify the instrument "LASCO" without filtering by a specific detector.
If needed, one can further refine the query by including a detector keyword (e.g., a.Detector('C2')).
"""

from sunpy.net import Fido, attrs as a

# Define the time range corresponding to the period covered by SOHO comet observations in the paper.
start_time = '1996-01-01'
end_time = '2008-12-31'

# Build the query for SOHO LASCO observations.
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO')
)

# Print the query results to inspect available data.
print("Query Result for SOHO LASCO observations from {} to {}:".format(start_time, end_time))
print(query_result)

# Uncomment the following line to download the data after verifying the query result.
# downloaded_files = Fido.fetch(query_result)
    
if __name__ == "__main__":
    # The query has been performed and the result printed.
    # Further processing can be implemented here as needed.
    pass
