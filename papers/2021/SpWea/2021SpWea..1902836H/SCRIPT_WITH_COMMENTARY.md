# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the SOHO/MDI data in the VSO for photospheric line-of-sight (LOS) magnetic field observations.
The query is based on the available VSO interface, selecting the instrument "MDI" 
from the SOHO source, with the observable "LOS_magnetic_field". The time range is chosen from one of the available 
ranges (e.g., using a single day from "1996-04-30" which is within the available time range of "1996/04/30 - 2011/04/12").
This dataset is particularly useful as the synoptic magnetograms from MDI serve as input to coronal models.
"""

# Import necessary classes from sunpy.net
from sunpy.net import Fido, attrs

# Define the query attributes:
# 1. Time: for this example we use one day "1996-04-30" to "1996-04-30 23:59:59"
# 2. Instrument: MDI and source: SOHO are implied in the interface; additionally we filter on the physical observable
#    'LOS_magnetic_field' as this corresponds to the magnetogram needed for coronal modeling.
time_attr = attrs.Time("1996-04-30 00:00:00", "1996-04-30 23:59:59")
instrument_attr = attrs.Instrument("MDI")
source_attr = attrs.Source("SOHO")
physobs_attr = attrs.Physobs("LOS_magnetic_field")

# Query the Virtual Solar Observatory (VSO) using Fido.search
# The query uses all the above attributes explicitly.
result = Fido.search(time_attr, source_attr, instrument_attr, physobs_attr)

# Print out the query results
print("Query Results:")
print(result)

# To fetch the data, uncomment the following line (fetch command is commented out by default):
# downloaded_files = Fido.fetch(result)

if __name__ == "__main__":
    # If needed, additional processing can be done here.
    pass
