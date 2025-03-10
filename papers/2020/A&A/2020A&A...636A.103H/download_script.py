# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
A simple Sunpy VSO query script for downloading SOHO proton monitor data
from the CELIAS instrument (using the Proton Monitor, PM) on board SOHO.

This example is based on the context provided which uses a test case on SOHO/PM
to study proton plasma properties (e.g., number density). The query is constructed
for a short time interval in 2005 (a representative period as mentioned in the paper).
The available VSO interface shows that the SOHO/CELIAS instrument with detector PM and 
physical observable 'number_density' covers the time range from 1995/12/15 to present.

The script queries this data using Sunpy's VSO client. The Fido.fetch command is provided 
but commented out to avoid downloading data accidentally.
"""

import datetime
from sunpy.net import Fido, attrs as a

# Define the query time range - chosen to represent a day in 2005 as per the example in the paper.
start_time = "2005-06-01"
end_time = "2005-06-02"

# Construct the query using the time range and instrument details.
# Here we specify:
#   - Source: "SOHO"
#   - Instrument: "CELIAS"
#   - Detector: "PM"
#   - Physical Observable: "number_density"
query = Fido.search(a.Time(start_time, end_time),
                    a.Source("SOHO"),
                    a.Instrument("CELIAS"),
                    a.Detector("PM"),
                    a.Physobs("number_density"))

# Print out the query results
print("Query Results:")
print(query)

# If you wish to download the files, uncomment the line below.
# downloaded_files = Fido.fetch(query)
# print("Downloaded Files:", downloaded_files)

if __name__ == "__main__":
    # Execution entry point
    pass
