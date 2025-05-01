# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query solar data related to a solar jet event on 2002 August 19.
We create two separate queries:
  1. TRACE EUV images using the 195 Å filter.
  2. RHESSI X-ray data in three different energy ranges for hard X-ray imaging.
  
Note: We only print the query results. The actual data downloading (Fido.fetch) commands are commented out.
"""

# Import necessary modules from sunpy.net and astropy.units for unit handling
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ------------------------- Query 1: TRACE Data -------------------------
# Description:
# Query TRACE data for EUV imaging of the jet in the 195 Å passband.
# The event time is on 2002 August 19 around 21:01 UT.
# We choose a 5-minute interval around the snapshot time to capture the event.
trace_start_time = "2002-08-19T21:00:00"
trace_end_time = "2002-08-19T21:05:00"

# Build the query for TRACE. We use the instrument "TRACE", specify the time range,
# and filter by wavelength 195 Å using astropy.units.
trace_query = Fido.search(
    a.Time(trace_start_time, trace_end_time),
    a.Instrument("TRACE"),
    a.Wavelength(195*u.AA)
)

# Print query results for TRACE data
print("TRACE Query Results:")
print(trace_query)

# To fetch the data if needed, uncomment the next line:
# trace_files = Fido.fetch(trace_query)

# ------------------------- Query 2: RHESSI Data -------------------------
# Description:
# Query RHESSI data for hard X-ray imaging of the jet during the flare.
# The event time is on 2002 August 19 between 21:01:27 UT and 21:01:55 UT.
# We create three individual queries corresponding to:
#   - 10-18 keV (thermal component)
#   - 18-30 keV (elongated emission along the jet)
#   - 30-100 keV (nonthermal, footpoint emission)
rhessi_start_time = "2002-08-19T21:01:27"
rhessi_end_time = "2002-08-19T21:01:55"

# Query for 10-18 keV data
rhessi_query_low = Fido.search(
    a.Time(rhessi_start_time, rhessi_end_time),
    a.Instrument("RHESSI"),
    a.Wavelength(10*u.keV, 18*u.keV)
)

print("\nRHESSI Query Results (10-18 keV):")
print(rhessi_query_low)

# Query for 18-30 keV data
rhessi_query_mid = Fido.search(
    a.Time(rhessi_start_time, rhessi_end_time),
    a.Instrument("RHESSI"),
    a.Wavelength(18*u.keV, 30*u.keV)
)

print("\nRHESSI Query Results (18-30 keV):")
print(rhessi_query_mid)

# Query for 30-100 keV data
rhessi_query_high = Fido.search(
    a.Time(rhessi_start_time, rhessi_end_time),
    a.Instrument("RHESSI"),
    a.Wavelength(30*u.keV, 100*u.keV)
)

print("\nRHESSI Query Results (30-100 keV):")
print(rhessi_query_high)

# To fetch the RHESSI data, you can uncomment the following lines:
# rhessi_files_low = Fido.fetch(rhessi_query_low)
# rhessi_files_mid = Fido.fetch(rhessi_query_mid)
# rhessi_files_high = Fido.fetch(rhessi_query_high)

if __name__ == "__main__":
    print("\nQueries complete. Check the printed query results for details on available data.")
