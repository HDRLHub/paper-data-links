# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO module to query SDO/AIA data.
The context of the paper focused on observations of AR 11944 in January 2014.
Since the VSO interface only provides SDO instruments (and not Hinode/EIS),
we focus our query on SDO/AIA data.

We use the observation around January 8, 2014 at 11:00 UT,
which corresponds to the SDO/AIA imaging context described in the paper.
The query is restricted to the AIA instrument and the 171 Å wavelength,
which is typical for coronal imaging and is available via the VSO interface.
The script prints out the query results. The Fido.fetch command is provided as a comment.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Define the time range for the query from the context.
# Here we choose January 8, 2014 from 11:00 to 11:05 UT as a representative period.
time_range = TimeRange("2014-01-08 11:00:00", "2014-01-08 11:05:00")

# Set up the query attributes based on the required instrument and time range.
# In this query, we use SDO/AIA, and specifically request data in the 171 Å channel.
# This wavelength channel is among the available ones in the VSO interface for SDO/AIA.
query = Fido.search(
    a.Time(time_range.start, time_range.end),
    a.Instrument("AIA"),
    a.Wavelength(171 * u.angstrom)
)

# Print the query results to review the search output.
print("Query Results for SDO/AIA data:")
print(query)

# To download the data, uncomment the following line:
# downloads = Fido.fetch(query)
