# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy's VSO interface to search for SOHO/SUMER spectral data that were used in the study.
Two separate queries are constructed:
1. A query for the first prominence (PRM1) observed on 8 October 1999.
2. A query for the second prominence (PRM04) observed on 7 June 2004.

Both queries use the SOHO/SUMER instrument since the available VSO interface for SUMER
covers the time range 1996/01/22 to 2017/04/04. The queries are explicitly built using only the required
values: time range and instrument information.
"""

# Import necessary modules from sunpy and astropy
from sunpy.net import Fido, attrs
import datetime

# Query 1: Retrieve SOHO/SUMER data for Prominence PRM1 observed on 8 October 1999.
# The VSO data for SUMER indicates that observations are available between 1996/01/22 and 2017/04/04.
time_range_PRM1 = attrs.Time("1999-10-08", "1999-10-08")  # Single day observation for PRM1.
instrument_SUMER = attrs.Instrument("SUMER")                # Specify the instrument.
source_SOHO    = attrs.Source("SOHO")                       # Specify the source.

# Build the query for PRM1 observation.
query_PRM1 = Fido.search(time_range_PRM1, instrument_SUMER, source_SOHO)

# Print query results for PRM1.
print("Query results for SOHO/SUMER PRM1 observation on 8 October 1999:")
print(query_PRM1)

# Uncomment the following line to download PRM1 data:
# files_PRM1 = Fido.fetch(query_PRM1)


# Query 2: Retrieve SOHO/SUMER data for Prominence PRM04 observed on 7 June 2004.
# (Note: Although the campaign spanned 7–8 June 2004, we are using 7 June 2004 as the representative date.)
time_range_PRM04 = attrs.Time("2004-06-07", "2004-06-07")   # Single day observation for PRM04.
# The instrument and source remain the same for SUMER on SOHO.
query_PRM04 = Fido.search(time_range_PRM04, instrument_SUMER, source_SOHO)

# Print query results for PRM04.
print("\nQuery results for SOHO/SUMER PRM04 observation on 7 June 2004:")
print(query_PRM04)

# Uncomment the following line to download PRM04 data:
# files_PRM04 = Fido.fetch(query_PRM04)

if __name__ == "__main__":
    # This block ensures the script runs when executed directly.
    pass
