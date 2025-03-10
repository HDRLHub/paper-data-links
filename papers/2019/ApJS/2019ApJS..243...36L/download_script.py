# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query solar data from the Virtual Solar Observatory (VSO)
using SunPy's Fido interface. We construct two distinct queries based on the context provided:

1. SDO/HMI: Querying line-of-sight magnetic field measurements for operational forecasting,
   corresponding to the testing interval defined in the paper (01 January 2016 – 31 December 2017).
2. SOHO/MDI: Querying magnetogram data from the 2009 workshop period for benchmark comparison.
   Although the exact dates of the workshop are not explicitly provided, we choose a representative
   period within the available MDI data (June 2009).

Note: Fido.fetch commands are provided as comments so no actual data retrieval occurs.
"""

from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# --- Query for SDO/HMI data (Operational Forecasting Interval) ---
# The paper indicates this period as 01 January 2016 – 31 December 2017.
hmi_start_time = "2016-01-01"
hmi_end_time   = "2017-12-31"

# Construct a query for SDO/HMI. Using the "LOS_magnetic_field" observable is appropriate.
# The available full time range for SDO/HMI in the VSO interface is from "2010/03/29 - present".
query_hmi = Fido.search(
    a.Time(hmi_start_time, hmi_end_time),
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")
)
print("SDO/HMI Query Results:")
print(query_hmi)

# Uncomment the following line to fetch SDO/HMI data once you are ready.
# downloaded_files_hmi = Fido.fetch(query_hmi)

# --- Query for SOHO/MDI data (2009 Workshop Data) ---
# The paper describes using SOHO/MDI data from the 2009 workshop.
# We select a representative one-month period in mid-2009.
mdi_start_time = "2009-06-01"
mdi_end_time   = "2009-06-30"

# Construct a query for SOHO/MDI.
# For MDI, specifying both Source and Instrument and the Detector is helpful.
query_mdi = Fido.search(
    a.Time(mdi_start_time, mdi_end_time),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Detector("MDI")
)
print("\nSOHO/MDI Query Results:")
print(query_mdi)

# Uncomment the following line to fetch SOHO/MDI data when needed.
# downloaded_files_mdi = Fido.fetch(query_mdi)

if __name__ == "__main__":
    print("\nQueries constructed successfully. Review the printed query results above.")
