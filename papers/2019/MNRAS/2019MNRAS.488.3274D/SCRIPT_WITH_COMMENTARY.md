# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO Fido interface to query solar observations from the VIRGO/SPM instrument onboard the SOHO spacecraft.
We construct two queries:
1. A query for the full VIRGO/SPM dataset covering the period from April 11, 1996 to March 30, 2014.
2. A query for the selected VIRGO/SPM subset (active phase analysis) covering the period from April 22, 1999 to July 20, 1999.

Note:
- The available VSO interface indicates VIRGO/SPM data (a.Source: "SOHO", a.Instrument: "VIRGO", a.Detector: "SPM") with a full time range starting from 1995/12/06.
- We use the time ranges and instrument details as specified in the context.
- The Fido.fetch commands are provided but commented out.
"""

from sunpy.net import Fido, attrs as a

# Define time ranges for the two queries
# Full VIRGO/SPM dataset time range as mentioned in the paper:
time_range_full_start = "1996-04-11"
time_range_full_end   = "2014-03-30"

# Selected subset for active phase analysis time range
time_range_active_start = "1999-04-22"
time_range_active_end   = "1999-07-20"

# Query 1: Full VIRGO/SPM dataset
# In this query we use:
# - time range from 1996-04-11 to 2014-03-30
# - Instrument VIRGO
# - Detector SPM (as specified in the VSO interface)
query_full = Fido.search(a.Time(time_range_full_start, time_range_full_end),
                         a.Instrument("VIRGO"),
                         a.Detector("SPM"))

# Print out the query results for the full dataset
print("Query results for the full VIRGO/SPM dataset (1996-04-11 to 2014-03-30):")
print(query_full)

# Uncomment the following line to fetch the data for the full dataset
# files_full = Fido.fetch(query_full)

# Query 2: VIRGO/SPM subset for active phase analysis
# In this query we use:
# - time range from 1999-04-22 to 1999-07-20
# - Instrument VIRGO
# - Detector SPM, as provided in the vso_interface; note that this subset is chosen to have fewer data gaps.
query_active = Fido.search(a.Time(time_range_active_start, time_range_active_end),
                           a.Instrument("VIRGO"),
                           a.Detector("SPM"))

# Print out the query results for the active phase subset
print("\nQuery results for the VIRGO/SPM active phase subset (1999-04-22 to 1999-07-20):")
print(query_active)

# Uncomment the following line to fetch the data for the active phase subset
# files_active = Fido.fetch(query_active)

if __name__ == "__main__":
    print("\nSunPy VSO queries have been executed. Review the printed query information for details.")
