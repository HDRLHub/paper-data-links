# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the VSO database via sunpy to retrieve data from several instruments
that were used in the SOL2014-09-01 flare study. In this example, we query three instruments:
1. RHESSI – for hard X-ray observations during the impulsive phase.
2. SDO/HMI – for photospheric magnetic field (magnetogram) observations taken during the flare.
3. SOHO/LASCO – specifically the C2 coronagraph channel, for white‐light CME observations.

Note:
- The SOL2014-09-01 event is used with appropriate time ranges based on the paper details.
- The script uses sunpy.net.vso.Fido and attributes (a) for a readable and explicit query.
- Fido.fetch commands are provided as comments.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# --------------------------------------------------------------------------------
# Query 1: RHESSI Hard X-ray Observations
# --------------------------------------------------------------------------------
# According to the study, RHESSI captured the impulsive phase of the flare.
# We use a one-hour window around the event on September 1, 2014.
rhessi_start = "2014-09-01T11:00:00"
rhessi_end   = "2014-09-01T12:00:00"

# Build the query for RHESSI data using instrument "RHESSI"
query_rhessi = Fido.search(a.Time(rhessi_start, rhessi_end),
                           a.Instrument("RHESSI"))
print("RHESSI Query Results:")
print(query_rhessi)
# To download the data, uncomment the line below:
# data_rhessi = Fido.fetch(query_rhessi)

# --------------------------------------------------------------------------------
# Query 2: SDO/HMI Magnetogram Observations
# --------------------------------------------------------------------------------
# We select a narrow time window around 12:04 UT on September 1, 2014,
# which is a synchronous magnetogram observation during the flare.
hmi_start = "2014-09-01T12:04:00"
hmi_end   = "2014-09-01T12:05:00"  # 1 minute window

# Build the query for SDO/HMI data.
query_hmi = Fido.search(a.Time(hmi_start, hmi_end),
                        a.Instrument("HMI"))
print("\nSDO/HMI Query Results:")
print(query_hmi)
# To download the data, uncomment the line below:
# data_hmi = Fido.fetch(query_hmi)

# --------------------------------------------------------------------------------
# Query 3: SOHO/LASCO C2 Coronagraph Observations
# --------------------------------------------------------------------------------
# The CME was first observed by SOHO/LASCO C2 at 11:12:05 UT on September 1, 2014.
# We use a one-hour window starting at the first appearance time.
lasco_start = "2014-09-01T11:12:05"
lasco_end   = "2014-09-01T12:12:05"

# Build the query for SOHO data selecting instrument "LASCO" and detector "C2".
query_lasco = Fido.search(a.Time(lasco_start, lasco_end),
                          a.Instrument("LASCO"),
                          a.Detector("C2"))
print("\nSOHO/LASCO C2 Query Results:")
print(query_lasco)
# To download the data, uncomment the line below:
# data_lasco = Fido.fetch(query_lasco)

# --------------------------------------------------------------------------------
# End of Queries
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    print("\nAll queries executed. Please review the printed query results above.")
