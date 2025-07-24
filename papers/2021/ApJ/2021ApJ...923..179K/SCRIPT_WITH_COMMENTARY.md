# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3

"""
This script constructs a Sunpy VSO query for the SOHO/SWAN instrument.
Based on the provided VSO interface and context, we are interested in data
for the SOHO/SWAN instrument. The context specifies data from the SOHO/SWAN
instrument for studying backscattered Lyman-alpha intensities, which are used
to derive heliolatitudinal variations of the solar wind mass flux.

We use a time range from 1996-01-12 (the start available in the VSO interface)
to 2017-12-31 (to match the end of the data collection period noted in the context).

Note: The Fido.fetch command is commented out to avoid executing an actual download.
"""

from sunpy.net import Fido, attrs as a
import datetime

# Define the query time range based on the intersection of available data and context.
# VSO available full time range: "1996/01/12 - present"
# Context data collection period for SOHO/SWAN: 1995 - end of 2017
start_time = "1996-01-12"
end_time = "2017-12-31"

# Define the instrument details from the VSO interface.
# Instrument: SWAN from SOHO.
source = "SOHO"
instrument = "SWAN"

# Create a query object using Sunpy's Fido.
# a.Time is provided with start and end times.
# a.Source and a.Instrument specify the instrument details.
query_result = Fido.search(a.Time(start_time, end_time),
                           a.Source(source),
                           a.Instrument(instrument))

# Print the query results.
print("VSO Query Results:")
print(query_result)

# Uncomment the line below to fetch the data (download not executed in this script).
# downloaded_files = Fido.fetch(query_result)

if __name__ == "__main__":
    # This script is designed to query the data and print out the results.
    # Further processing of the query_result can be performed here if needed.
    pass
