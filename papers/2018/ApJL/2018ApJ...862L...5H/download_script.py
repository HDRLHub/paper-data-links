# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to construct queries for helioseismic data as described in the paper.
We query for two key instruments:
1. SDO/HMI observations: covering April 2010 – May 2018.
2. SOHO/MDI observations: covering May 1996 – February 2011.

Both queries use the time range and instrument parameters. The VSO interface (available instruments)
confirms that SDO/HMI and SOHO/MDI are available. Note that GONG and NSO observations are not provided
by the VSO interface, hence they are not queried here.
"""

# Import required modules from SunPy
from sunpy.net import Fido, attrs as a

# --------------------- Query 1: SDO/HMI ---------------------
# The paper indicates that HMI observations started in April 2010 and ended in May 2018.
# VSO interface for SDO/HMI: Available from "2010/03/29 - present".
# We therefore choose a query time interval that aligns with the paper's observation period.
hmi_start_time = "2010-04-01T00:00:00"
hmi_end_time = "2018-05-01T00:00:00"

# Construct the query for SDO/HMI data using the required time range and instrument.
query_hmi = Fido.search(
    a.Time(hmi_start_time, hmi_end_time),
    a.Instrument("HMI"),        # Instrument specified in paper and VSO interface
    a.Source("SDO")             # Data source for HMI observations
)

# Print the results of the HMI query.
print("SDO/HMI Query Results:")
print(query_hmi)

# Uncomment the following line to download the HMI data:
# hmi_files = Fido.fetch(query_hmi)


# --------------------- Query 2: SOHO/MDI ---------------------
# The paper specifies that the MDI observations were from May 1996 to February 2011.
# VSO interface for SOHO/MDI data shows available time ranges that cover this period.
mdi_start_time = "1996-05-01T00:00:00"
mdi_end_time = "2011-02-28T00:00:00"

# Construct the query for SOHO/MDI data using the specified time range and instrument.
query_mdi = Fido.search(
    a.Time(mdi_start_time, mdi_end_time),
    a.Instrument("MDI"),        # Instrument as per the paper and VSO records
    a.Source("SOHO")            # Data source for MDI observations
)

# Print the results of the MDI query.
print("SOHO/MDI Query Results:")
print(query_mdi)

# Uncomment the following line to download the MDI data:
# mdi_files = Fido.fetch(query_mdi)


if __name__ == "__main__":
    # The script prints the query results for both instruments.
    # Data fetching lines remain commented out for controlled execution.
    pass
