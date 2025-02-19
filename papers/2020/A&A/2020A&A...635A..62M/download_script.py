# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs Sunpy VSO queries to download data from two instruments,
as specified by the scientific context of the paper on the 14 June 2012 CME.

We will query:
1. SDO/AIA:
   - Observation at 13:45:00 UT on 14 June 2012.
   - Wavelength: 211 Å (EUV imagery capturing the active region).
2. SOHO/LASCO (Detector C2):
   - White-light coronagraph image at ~14:12:07 UT on 14 June 2012.
   - This data provides a white-light view of the CME.

Note: The Fido.fetch() commands are provided in commented form to avoid actual downloads.
"""

# Import the necessary modules from sunpy and astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Query 1: SDO/AIA EUV imaging at 211 Å at 13:45:00 UT on 14 June 2012.
# The VSO interface for SDO/AIA is available from 2010/05/12 to present.
start_time_aia = "2012-06-14T13:45:00"
end_time_aia = "2012-06-14T13:45:00"
wavelength_aia = 211 * u.AA  # 211 Angstrom

# Build the query for SDO/AIA data.
query_aia = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(wavelength_aia, wavelength_aia)
)

# Print the query results for the AIA search.
print("SDO/AIA Query Results:")
print(query_aia)

# Uncomment the following line to fetch the data for SDO/AIA:
# downloaded_aia_files = Fido.fetch(query_aia)

# Query 2: SOHO LASCO/C2 white-light coronagraph imaging at ~14:12:07 UT on 14 June 2012.
# The VSO interface shows LASCO/C2 data available from 1995/12/08 to present.
start_time_lasco = "2012-06-14T14:12:07"
end_time_lasco = "2012-06-14T14:12:07"

# Build the query for LASCO/C2 data.
query_lasco = Fido.search(
    a.Time(start_time_lasco, end_time_lasco),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print the query results for the LASCO search.
print("\nSOHO/LASCO (C2) Query Results:")
print(query_lasco)

# Uncomment the following line to fetch the data for LASCO/C2:
# downloaded_lasco_files = Fido.fetch(query_lasco)

if __name__ == "__main__":
    print("\nVSO query construction complete. Review the printed query results.")
