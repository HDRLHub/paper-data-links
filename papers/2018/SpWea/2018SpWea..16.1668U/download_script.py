# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client (Fido) to query data from the Virtual Solar Observatory.
We query two datasets:
  1. HMI (Helioseismic and Magnetic Imager) data from SDO, focusing on the line‐of‐sight magnetic field,
     which is used for solar surface magnetic field studies.
  2. AIA (Atmospheric Imaging Assembly) data from SDO, selecting the 171 Å channel that images the solar atmosphere.
The time range for both queries is set from 2011/01/07 to 2012/12/31 as specified in the context.
"""

# Import necessary modules from SunPy and Astropy.
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the queries, according to the study period.
time_start = '2011-01-07'
time_end = '2012-12-31'
time_range = a.Time(time_start, time_end)

# -------------------------------------------------------------------------------
# Query 1: HMI data from SDO
# -------------------------------------------------------------------------------
# In the context, HMI provides full-disk line‐of‐sight magnetic field measurements.
# We use the 'HMI' instrument on the 'SDO' source with the physical observable 'LOS_magnetic_field'.
query_hmi = Fido.search(
    time_range,
    a.Instrument("HMI"),
    a.Source("SDO"),
    a.Physobs("LOS_magnetic_field")
)

# Print the query results for HMI.
print("HMI Query Results:")
print(query_hmi)

# Uncomment the following line to fetch HMI data once you are ready to download.
# hmi_files = Fido.fetch(query_hmi)

# -------------------------------------------------------------------------------
# Query 2: AIA data from SDO
# -------------------------------------------------------------------------------
# In the context, AIA is used to image various layers of the solar atmosphere at different wavelengths.
# Here we select the AIA filter at approximately 171 Å which is widely used to track loop motion and cool structures.
query_aia = Fido.search(
    time_range,
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Wavelength(171 * u.AA)
)

# Print the query results for AIA.
print("AIA Query Results:")
print(query_aia)

# Uncomment the following line to fetch AIA data.
# aia_files = Fido.fetch(query_aia)

# End of script
