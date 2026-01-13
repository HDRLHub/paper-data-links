# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script performs two separate Sunpy VSO queries for helioseismic data relevant to a study of solar Rossby modes.
It queries:
  1. SOHO/MDI Doppler (LOS_velocity) data available from 1996 June 06 to 2011 April 12.
  2. SDO/HMI Doppler (LOS_velocity) data available from 2010 March 29 to 2019 June 30.
  
Note: Although the paper’s combined dataset spans 1996–2019, MDI observations are only available until 2011 while HMI data provide continuity beyond.
Uncomment the Fido.fetch commands to download the data.
"""

# Import the necessary modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the observation time ranges based on the paper context:
# For SOHO/MDI data:
time_start_mdi = "1996-06-06"
time_end_mdi   = "2011-04-12"

# For SDO/HMI data:
time_start_hmi = "2010-03-29"
time_end_hmi   = "2019-06-30"

# ----------------------- Query for SOHO/MDI Data -----------------------
# The MDI instrument records LOS_velocity using Doppler measurements at a wavelength of 6768.0 Å.
# This dataset is used for helioseismic inferences of the solar internal rotation profile.
mdi_query = Fido.search(
    a.Time(time_start_mdi, time_end_mdi),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Physobs("LOS_velocity"),
    a.Wavelength(6768.0 * u.Angstrom)
)

# Print out the query results for SOHO/MDI.
print("Query Results for SOHO/MDI Data:")
print(mdi_query)

# To download the SOHO/MDI data, uncomment the following line:
# mdi_download = Fido.fetch(mdi_query)

# ----------------------- Query for SDO/HMI Data -----------------------
# The HMI instrument onboard SDO provides LOS_velocity measurements.
# Although the paper includes magnetic field measurements as well, here we query based on the Doppler (LOS_velocity) observable.
# The available wavelength information in the vso_interface is around 6173 Å.
hmi_query = Fido.search(
    a.Time(time_start_hmi, time_end_hmi),
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("LOS_velocity"),
    a.Wavelength(6173.0 * u.Angstrom)
)

# Print out the query results for SDO/HMI.
print("Query Results for SDO/HMI Data:")
print(hmi_query)

# To download the SDO/HMI data, uncomment the following line:
# hmi_download = Fido.fetch(hmi_query)

if __name__ == "__main__":
    print("VSO queries completed. Review above output for details of the search results.")
