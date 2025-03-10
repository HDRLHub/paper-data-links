# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use SunPy's VSO interface to query two datasets:
1. SOHO/MDI data (LOS_magnetic_field) covering part of Solar Cycle 23.
2. SDO/HMI data (LOS_magnetic_field) covering from Solar Cycle 24 into cycle 23/24 overlap.

These queries reflect the instruments and time ranges as described in the context.
The study period is from July 1, 1996 to August 23, 2018.
Since MDI/SOHO data are available until about April 12, 2011, we query MDI data from
July 1, 1996 to April 12, 2011. For HMI/SDO, data are available from March 29, 2010 to present,
so we query HMI data from March 29, 2010 to August 23, 2018.
"""

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define time ranges as strings
mdi_start = "1996-07-01"        # Start date for MDI (within available time, after 1996/04/30)
mdi_end   = "2011-04-12"        # End date corresponding to available MDI data
hmi_start = "2010-03-29"        # Start date for HMI data (available since 2010/03/29)
hmi_end   = "2018-08-23"        # End date for HMI data matching study period's end

# Query for SOHO/MDI LOS_magnetic_field data
# According to the VSO interface, we choose the record with a.Source=SOHO, a.Instrument=MDI and a.Physobs=LOS_magnetic_field.
mdi_query = Fido.search(
    a.Time(mdi_start, mdi_end),
    a.Instrument("MDI"),
    a.Source("SOHO"),
    a.Physobs("LOS_magnetic_field")
)

# Print the MDI query result
print("SOHO/MDI Query Results (LOS_magnetic_field):")
print(mdi_query)

# Uncomment the following line to fetch the MDI data files locally:
# mdi_files = Fido.fetch(mdi_query)

# Query for SDO/HMI LOS_magnetic_field data
# From the VSO interface, we require a.Source=SDO, a.Instrument=HMI and a.Physobs=LOS_magnetic_field,
# with available time beginning 2010/03/29.
hmi_query = Fido.search(
    a.Time(hmi_start, hmi_end),
    a.Instrument("HMI"),
    a.Source("SDO"),
    a.Physobs("LOS_magnetic_field")
)

# Print the HMI query result
print("SDO/HMI Query Results (LOS_magnetic_field):")
print(hmi_query)

# Uncomment the following line to fetch the HMI data files locally:
# hmi_files = Fido.fetch(hmi_query)

if __name__ == "__main__":
    # For debugging purposes, you can run this script directly.
    print("VSO queries executed. Check the printed results for details.")
