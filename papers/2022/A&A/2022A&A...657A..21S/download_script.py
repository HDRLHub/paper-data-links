# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query data for the Solar Dynamics Observatory
Helioseismic and Magnetic Imager (SDO/HMI) instrument. In this context, the HMI observations
are used to provide solar photospheric context during the June 5, 2020 solar event.
The query is set to retrieve LOS magnetic field data from SDO/HMI within the event time window.
Note:
   - Available HMI data span from 2010/03/29 to the present, as per the VSO interface.
   - The Fido.fetch command is provided but commented out. Uncomment to download the data.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs as a

# Define the time range corresponding to the solar radio bursts observed on June 5, 2020.
start_time = "2020-06-05T09:25:00"
end_time = "2020-06-05T09:39:00"

# Create a query for SDO/HMI data.
# We use the instrument "HMI", source "SDO", and observable "LOS_magnetic_field" as available in VSO.
query = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")
)

# Print out the query results summary.
print("Query results for SDO/HMI data:")
print(query)

# If data download is desired, uncomment the following line.
# downloaded_files = Fido.fetch(query)

if __name__ == "__main__":
    pass
