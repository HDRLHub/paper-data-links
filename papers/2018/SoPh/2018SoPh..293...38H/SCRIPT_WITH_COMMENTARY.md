# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query SDO/HMI data from the Virtual Solar Observatory.
For the current study, we are interested in photospheric magnetograms (LOS magnetic field) 
obtained by the Helioseismic and Magnetic Imager (HMI) onboard SDO. 

In our context, the paper analyzes flare events (e.g., from June 2000 to June 2015),
and for flares occurring since 2011, HMI magnetograms are used.
Here, we construct a query for SDO/HMI LOS magnetic field data within a one-hour window 
on June 1, 2012. The available data in the VSO interface for SDO/HMI indicate a wavelength
range of 6173.0 – 6174.0 Å which is typical for HMI magnetic observations.
"""

# Import necessary modules from sunpy.net
from sunpy.net import Fido, attrs as a

# Define the time range for the query.
start_time = '2012-06-01T00:00:00'
end_time = '2012-06-01T01:00:00'

# Print out the query parameters details for clarity.
print("Querying SDO/HMI LOS magnetic field data from {} to {}.".format(start_time, end_time))

# Construct the query using the VSO attributes.
# We specify the source as SDO, instrument as HMI, and physical observable (physobs) as LOS_magnetic_field.
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)

# Print the query results summary.
print(query_result)

# If you want to actually download the data, you can use the following line.
# However, the fetch command is commented out as per instructions.
# downloaded_files = Fido.fetch(query_result)

if __name__ == "__main__":
    print("SDO/HMI query script executed successfully.")
