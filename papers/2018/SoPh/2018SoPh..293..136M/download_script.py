# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use SunPy's VSO interface (via Fido)
to query data from instruments that are available in the provided VSO interface.
We will query for data from:
  • SDO/AIA (Atmospheric Imaging Assembly on the Solar Dynamics Observatory)
  • SOHO/LASCO/C2 (for coronagraph images)
  • SOHO/ERNE (particle detector)

The time intervals for the queries are based on the scientific context
of the GLE 72 event on 10 September 2017, when the CME and associated SEP event occurred.
Note: The script prints out the query results and the actual data download via Fido.fetch is commented out.
"""

from sunpy.net import Fido, attrs as a
from datetime import datetime

# ---------------------------
# Query 1: SDO/AIA Data Query
# ---------------------------
# We set the time range to cover the CME shock observation as captured by AIA.
start_time_aia = '2017-09-10T16:00:00'
end_time_aia   = '2017-09-10T19:00:00'
# For SDO/AIA, the source is SDO and the instrument is AIA.
# The VSO interface indicates multiple wavelengths are available but we use the instrument
# without further wavelength restrictions as the context doesn't specify a particular channel.
print("Querying SDO/AIA data from", start_time_aia, "to", end_time_aia)
query_aia = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Instrument("AIA"),
    a.Source("SDO")
)
print(query_aia)
# To fetch the data, uncomment the line below:
# files_aia = Fido.fetch(query_aia)

# ---------------------------------------
# Query 2: SOHO LASCO/C2 Data Query
# ---------------------------------------
# The SOHO LASCO/C2 coronagraph first detected the CME at 16:00:07 UT.
# We use a shorter window to capture the initial observation of the CME.
start_time_lasco = '2017-09-10T16:00:07'
end_time_lasco   = '2017-09-10T17:00:00'
# For LASCO, the instrument is LASCO with detector set to C2 and source being SOHO.
print("\nQuerying SOHO LASCO/C2 data from", start_time_lasco, "to", end_time_lasco)
query_lasco = Fido.search(
    a.Time(start_time_lasco, end_time_lasco),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Source("SOHO")
)
print(query_lasco)
# To download the LASCO data, uncomment the next line:
# files_lasco = Fido.fetch(query_lasco)

# ---------------------------------------
# Query 3: SOHO ERNE Data Query
# ---------------------------------------
# SOHO ERNE data provide insights into the particle composition (e.g., Fe/O ratio)
# during the SEP event. We select a time range covering the main part of the event.
start_time_erne = '2017-09-10T16:15:00'
end_time_erne   = '2017-09-10T19:15:00'
# For ERNE, the instrument is ERNE, and the source is SOHO.
print("\nQuerying SOHO ERNE data from", start_time_erne, "to", end_time_erne)
query_erne = Fido.search(
    a.Time(start_time_erne, end_time_erne),
    a.Instrument("ERNE"),
    a.Source("SOHO")
)
print(query_erne)
# To download the ERNE data, uncomment the next line:
# files_erne = Fido.fetch(query_erne)

if __name__ == '__main__':
    print("\nQueries completed. Check the printed summary for each query.")
