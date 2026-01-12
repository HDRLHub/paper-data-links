# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to construct queries corresponding to the observational data
discussed in the paper. It queries for the following instruments and time periods:

1. Wilcox Solar Observatory (WSO):
   - Time Range: March 1996 to February 1997
   - Note: WSO data may not be available in the VSO interface.

2. Global Oscillation Network Group (GONG):
   - Query 1 (Minimum 23/24 Observations): Two-year period covering 2008 and 2009.
   - Query 2 (Minimum 24/25 Observations): Two-year period spanning 2019 to 2020.

Other data sets (OMNI and SILSO) mentioned in the paper are not available via the VSO interface.
The script prints query results (but does not execute any data fetching commands).
"""

from sunpy.net import Fido, attrs as a
from datetime import datetime

# ------------------------ Query 1: Wilcox Solar Observatory (WSO) ------------------------
# Define the time range for the minimum 22/23 period: March 1996 - February 1997.
wso_start = "1996-03-01"
wso_end   = "1997-02-28"

# Construct the query for WSO data.
# Note: WSO data may not be available via the VSO interface.
query_wso = Fido.search(
    a.Time(wso_start, wso_end),
    a.Instrument("WSO")
)

print("WSO Query Results (March 1996 to February 1997):")
print(query_wso)

# To fetch the data, uncomment the following line:
# files_wso = Fido.fetch(query_wso)

# ------------------------ Query 2: Global Oscillation Network Group (GONG) ------------------------
# Query for the Minimum 23/24 Observations (2008-2009).
gong_23_start = "2008-01-01"
gong_23_end   = "2009-12-31"

query_gong_23 = Fido.search(
    a.Time(gong_23_start, gong_23_end),
    a.Instrument("GONG")
)

print("\nGONG Query Results for Minimum 23/24 (2008-2009):")
print(query_gong_23)

# To fetch the GONG 23/24 data, uncomment the following line:
# files_gong_23 = Fido.fetch(query_gong_23)

# Query for the Minimum 24/25 Observations (2019-2020).
gong_24_start = "2019-01-01"
gong_24_end   = "2020-12-31"

query_gong_24 = Fido.search(
    a.Time(gong_24_start, gong_24_end),
    a.Instrument("GONG")
)

print("\nGONG Query Results for Minimum 24/25 (2019-2020):")
print(query_gong_24)

# To fetch the GONG 24/25 data, uncomment the following line:
# files_gong_24 = Fido.fetch(query_gong_24)

# ------------------------ Note on OMNI and SILSO Data ------------------------
# The paper also uses in situ solar wind measurements (OMNI) and sunspot data (SILSO).
# These datasets are not available through the VSO interface, so queries cannot be constructed for them here.

if __name__ == "__main__":
    print("\nVSO queries constructed successfully. Please review the printed query results above.")
