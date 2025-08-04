# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory for full-disk magnetogram data from the
Helioseismic and Magnetic Imager (HMI) on board the Solar Dynamics Observatory (SDO). 
The data pertain to the line-of-sight (radial) magnetic field observations used as the lower
boundary condition in solar coronal magnetic field modeling, as described in the paper.
We set the query time period within Solar Cycle 24; here we choose a one-day period during
the cycle (May 5–6, 2015). The data are taken using the Fe I 6173 Å spectral line.

Note: The Fido.fetch command is provided but commented out.
"""

# Import required modules from sunpy and astropy
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the time range for Solar Cycle 24 magnetogram data (example: May 5-6, 2015)
time_start = '2015-05-05'
time_end = '2015-05-06'

# Construct the search query:
# 1. a.Time specifies the time range.
# 2. a.Source and a.Instrument pinpoint the data from SDO/HMI.
# 3. a.Physobs selects the observable: line-of-sight magnetic field.
# 4. a.Wavelength defines the spectral line near 6173 Å.
query = Fido.search(
    a.Time(time_start, time_end),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6173*u.Angstrom, 6174*u.Angstrom)
)

# Print the query results to review what data would be retrieved.
print("Query Results:")
print(query)

# To actually download the data, uncomment the following line:
# files = Fido.fetch(query)

if __name__ == '__main__':
    # The script only prints the query result. Data fetching is disabled by default.
    pass
