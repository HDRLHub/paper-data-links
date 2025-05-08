# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy to query the Virtual Solar Observatory (VSO) for two instruments,
reflecting our study of the CME–CME interaction event on 13–14 June 2012:

1. STEREO_A SECCHI EUVI:
   - Time Range: 13 June 2012 to 14 June 2012.
   - Instrument details: EUVI (Extreme Ultraviolet Imager), part of the SECCHI suite on STEREO_A.
2. SOHO LASCO (using the C2 detector):
   - Time Range: 13 June 2012 (around CME1) to 14 June 2012 (around CME2).
   - Instrument details: LASCO C2, available for the period 1995/12/08 – present.
   
Note: The Fido.fetch lines are commented out as per the instructions.
"""

import sunpy.net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ----------------------------------------------------------------------
# Query 1: STEREO_A SECCHI EUVI Data for 13–14 June 2012
# ----------------------------------------------------------------------
# Define the time range for the CME onsets using SECCHI EUVI data.
time_range_euvi = a.Time("2012-06-13T00:00:00", "2012-06-14T23:59:59")

# Construct query attributes: Using STEREO_A as the source, SECCHI as the instrument,
# and specifying the detector as EUVI.
query_attrs_euvi = a.Source("STEREO_A") & a.Instrument("SECCHI") & a.Detector("EUVI")

# Perform the query using Fido.
result_euvi = Fido.search(time_range_euvi, query_attrs_euvi)

# Print query results.
print("Query Results for STEREO_A SECCHI EUVI (13–14 June 2012):")
print(result_euvi)

# Uncomment the following line to fetch data:
# files_euvi = Fido.fetch(result_euvi)

# ----------------------------------------------------------------------
# Query 2: SOHO LASCO C2 Data for 13–14 June 2012
# ----------------------------------------------------------------------
# Define the time range for LASCO observations covering CME1 and CME2.
# The LASCO C2 data are valid for 2012 as its full time range is "1995/12/08 - present".
time_range_lasco = a.Time("2012-06-13T13:00:00", "2012-06-14T15:00:00")

# Construct query attributes: Using SOHO as the source, LASCO as the instrument,
# and specifying the detector as C2.
query_attrs_lasco = a.Source("SOHO") & a.Instrument("LASCO") & a.Detector("C2")

# Perform the query using Fido.
result_lasco = Fido.search(time_range_lasco, query_attrs_lasco)

# Print query results.
print("\nQuery Results for SOHO LASCO C2 (13–14 June 2012):")
print(result_lasco)

# Uncomment the following line to fetch data:
# files_lasco = Fido.fetch(result_lasco)

# End of script
