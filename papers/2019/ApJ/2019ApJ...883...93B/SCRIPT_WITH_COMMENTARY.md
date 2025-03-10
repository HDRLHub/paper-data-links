# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses sunpy's VSO client (Fido) to query SDO/HMI data.
We are using data available for the Helioseismic and Magnetic Imager (HMI)
on board the Solar Dynamics Observatory (SDO). According to our study, we
require data from April 30, 2010 through March 13, 2019.
In this example, we specifically query data with the physical observable
"LOS_magnetic_field" and a wavelength near 6173 Å, consistent with the VSO interface.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define time range based on the context for HMI observation period
time_range = a.Time("2010-04-30", "2019-03-13")

# Define the source and instrument based on VSO interface for SDO/HMI data
source = a.Source("SDO")
instrument = a.Instrument("HMI")

# Choose the physical observable: LOS_magnetic_field (one of the available ones)
physobs = a.Physobs("LOS_magnetic_field")

# For HMI, the available wavelength range is 6173.0 - 6174.0 Angstrom.
wavelength = a.Wave(6173.0 * u.AA, 6174.0 * u.AA)

# Perform the query with explicit parameters.
# The query includes: time range, source, instrument, physobs type and wavelength.
result = Fido.search(time_range, source, instrument, physobs, wavelength)

# Print the query results to inspect available data.
print("Query Results:")
print(result)

# To fetch the data, you could uncomment the following command:
# files = Fido.fetch(result)

if __name__ == "__main__":
    # This main block ensures the script can be executed as a standalone program.
    print("SDO/HMI data query completed. Review the printed query results for further action.")
