# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This Python script uses Sunpy's VSO interface to query data for the SWAN instrument on board
the SOHO satellite. The query is set up for the full available time range starting from "1996-01-12"
to the present. The SWAN instrument primarily observes the hydrogen Lyman-alpha emission, which is used
in studies such as the comprehensive survey of water production in comets.

The VSO query here is constructed with the following parameters:
    - Time: 1996-01-12 to present
    - Instrument: SWAN
    - Source: SOHO

Note: The script prints the query result. The actual data download (Fido.fetch) command is included as a
comment for users who wish to download the data.
"""

# Import necessary classes from sunpy.net
from sunpy.net import Fido, attrs as a

# Define the time range for the data query. According to the interface, data available from 1996-01-12 to present.
time_range = a.Time("1996-01-12", "present")

# Specify the source and instrument based on the VSO interface.
source = a.Source("SOHO")
instrument = a.Instrument("SWAN")

# Build the query using the Sunpy Fido search interface.
query_result = Fido.search(time_range, source, instrument)

# Print out the details of the query result to verify the search parameters.
print("Query Result:")
print(query_result)

# To download the data, you would use the following command:
# downloaded_files = Fido.fetch(query_result)
# print("Downloaded files:", downloaded_files)

if __name__ == "__main__":
    # The main block is executed if the script is run as a standalone program.
    # We already printed the query result above.
    pass
