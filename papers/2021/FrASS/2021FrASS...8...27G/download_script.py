# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query ACE spacecraft observations of an interplanetary shock
at DOY 118, 2001. In particular, we query ACE/EPAM and ACE/SWICS instruments during two distinct periods:
1. Upstream Phase – approximately 30 minutes prior to the shock crossing.
2. Downstream Phase – approximately 12 minutes after the shock crossing.

Note: The Fido.fetch commands are provided but commented out, as per instruction.
"""

from sunpy.net import Fido, attrs as a
import datetime

# Define the shock crossing time for DOY 118, 2001.
# For this example, we assume the shock crossing occurs at 2001-04-28T00:00:00.
shock_crossing_time = datetime.datetime(2001, 4, 28, 0, 0, 0)

# Define the upstream phase: 30 minutes before the shock crossing.
upstream_start = shock_crossing_time - datetime.timedelta(minutes=30)
upstream_end = shock_crossing_time

# Define the downstream phase: 12 minutes after the shock crossing.
downstream_start = shock_crossing_time
downstream_end = shock_crossing_time + datetime.timedelta(minutes=12)

# -------------------------------------------
# Query for ACE/EPAM data during the upstream phase.
# EPAM is an instrument onboard ACE which provides energetic particle measurements.
# -------------------------------------------
print("Querying ACE/EPAM data for the upstream phase (30 minutes before shock)...")
query_ace_epam_upstream = Fido.search(
    a.Time(upstream_start, upstream_end),
    a.Instrument("EPAM")
)
print(query_ace_epam_upstream)

# Uncomment the following lines to fetch the upstream ACE/EPAM data
# files_ace_epam_upstream = Fido.fetch(query_ace_epam_upstream)
# print("Fetched upstream ACE/EPAM files:", files_ace_epam_upstream)

# -------------------------------------------
# Query for ACE/EPAM data during the downstream phase.
# Downstream measurements capture the enhanced energetic particle intensity.
# -------------------------------------------
print("Querying ACE/EPAM data for the downstream phase (12 minutes after shock)...")
query_ace_epam_downstream = Fido.search(
    a.Time(downstream_start, downstream_end),
    a.Instrument("EPAM")
)
print(query_ace_epam_downstream)

# Uncomment the following lines to fetch the downstream ACE/EPAM data
# files_ace_epam_downstream = Fido.fetch(query_ace_epam_downstream)
# print("Fetched downstream ACE/EPAM files:", files_ace_epam_downstream)

# -------------------------------------------
# Query for ACE/SWICS data during the upstream phase.
# SWICS on ACE provides in situ ion composition measurements.
# -------------------------------------------
print("Querying ACE/SWICS data for the upstream phase (30 minutes before shock)...")
query_ace_swics_upstream = Fido.search(
    a.Time(upstream_start, upstream_end),
    a.Instrument("SWICS")
)
print(query_ace_swics_upstream)

# Uncomment the following lines to fetch the upstream ACE/SWICS data
# files_ace_swics_upstream = Fido.fetch(query_ace_swics_upstream)
# print("Fetched upstream ACE/SWICS files:", files_ace_swics_upstream)

# -------------------------------------------
# Query for ACE/SWICS data during the downstream phase.
# These data help to determine shock-accelerated ion composition changes.
# -------------------------------------------
print("Querying ACE/SWICS data for the downstream phase (12 minutes after shock)...")
query_ace_swics_downstream = Fido.search(
    a.Time(downstream_start, downstream_end),
    a.Instrument("SWICS")
)
print(query_ace_swics_downstream)

# Uncomment the following lines to fetch the downstream ACE/SWICS data
# files_ace_swics_downstream = Fido.fetch(query_ace_swics_downstream)
# print("Fetched downstream ACE/SWICS files:", files_ace_swics_downstream)

if __name__ == "__main__":
    print("SunPy VSO queries complete. Review the printed query results above.")
