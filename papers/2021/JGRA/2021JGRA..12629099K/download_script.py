# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy’s VSO interface via Fido to query two datasets as described in the scientific context:
1. Advanced Composition Explorer (ACE) data between January 1, 2004 and December 31, 2010.
2. STEREO Ahead (STEREO A) data for a representative several-day interval during the period 2007-2010.
----------------------------------------------------------------------------
Note:
- The script prints the query results.
- The Fido.fetch() commands are provided but commented out so that the script does not actually download data.
- Only the time range and instrument have been specified explicitly based on the provided context.
"""

from sunpy.net import Fido, attrs as a

# ---------------------------
# Query 1: ACE Data Query
# ---------------------------
# Set the ACE data time range (2004-01-01 to 2010-12-31)
ace_start_time = "2004-01-01"
ace_end_time = "2010-12-31"

# Print status for clarity.
print("Querying ACE data from", ace_start_time, "to", ace_end_time)

# Build the query for ACE instrument data.
# Here we assume 'ace' is the valid instrument identifier in the VSO.
query_ace = Fido.search(a.Time(ace_start_time, ace_end_time), a.Instrument("ace"))

# Print the query result summary.
print("ACE query result:")
print(query_ace)

# To download the ACE data, uncomment the following line:
# ace_data = Fido.fetch(query_ace)

# ---------------------------
# Query 2: STEREO A Data Query
# ---------------------------
# Choose a representative interval for STEREO A when both STEREO spacecraft were functioning (2007-2010).
# Since exact dates for the several-day intervals are not specified, here we use a one-week period.
stereo_start_time = "2007-06-01"
stereo_end_time = "2007-06-07"

print("Querying STEREO A data from", stereo_start_time, "to", stereo_end_time)

# Build the query for STEREO A instrument data.
# We use 'stereo_a' as the assumed VSO identifier for STEREO Ahead.
query_stereo = Fido.search(a.Time(stereo_start_time, stereo_end_time), a.Instrument("stereo_a"))

# Print the query result summary.
print("STEREO A query result:")
print(query_stereo)

# To download the STEREO A data, uncomment the following line:
# stereo_data = Fido.fetch(query_stereo)

print("Finished querying VSO for ACE and STEREO A data.")

if __name__ == "__main__":
    # The main block is provided for direct script execution.
    pass
