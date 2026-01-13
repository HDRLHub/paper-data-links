# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to construct Sunpy VSO queries using Fido.
We query two distinct datasets from the SOHO mission:
1. EUV images from the Extreme-ultraviolet Imaging Telescope (EIT) at 284 Å.
2. Magnetogram data from the Michelson Doppler Imager (MDI) observing the LOS magnetic field.
These datasets are chosen based on the scientific context of mapping solar wind footpoints,
as described in the paper which uses EIT (for imaging coronal structures) and MDI (for photospheric magnetic field)
to identify and map the source regions of solar wind. The time range selected is 2000 to 2008.
Note: The Fido.fetch commands are provided as comments and should not be executed.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the query (2000 to 2008, as per the data collection period used in the study)
time_start = "2000-01-01"
time_end = "2008-12-31"

####################################
# Query 1: SOHO/EIT at 284 Å images
####################################
# The EIT instrument provides EUV images; here we select the 284 Å wavelength,
# which is used in the mapping of solar wind footpoints.
eit_query = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("EIT"),
    a.Detector("EIT"),
    a.Physobs("intensity"),
    a.Wavelength(284 * u.AA)
)

print("Query Results for SOHO/EIT (284 Å):")
print(eit_query)

# Uncomment the following line to fetch the EIT data:
# eit_files = Fido.fetch(eit_query)

#########################################
# Query 2: SOHO/MDI LOS Magnetic Field Data
#########################################
# MDI magnetograms provide photospheric magnetic field observations.
# We query for the line-of-sight (LOS) magnetic field measurements using the wavelength 6768 Å.
mdi_query = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Detector("MDI"),
    a.Physobs("LOS_magnetic_field"),
    a.Wavelength(6768 * u.AA)
)

print("\nQuery Results for SOHO/MDI (LOS Magnetic Field):")
print(mdi_query)

# Uncomment the following line to fetch the MDI data:
# mdi_files = Fido.fetch(mdi_query)

if __name__ == "__main__":
    print("\nSunpy VSO query script executed successfully.")
