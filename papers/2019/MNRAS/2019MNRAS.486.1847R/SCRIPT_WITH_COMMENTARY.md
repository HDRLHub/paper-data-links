# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries SunPy's VSO for two datasets:
1. SDO/HMI data covering the period of Solar Cycle 24 (April 2010 – June 2017) 
   observed in the Fe I 6173 Å spectral line.
2. SOHO/MDI data covering Solar Cycle 23 (May 1996 – April 2011) observed in the Ni I 6768 Å spectral line.

The script uses explicit time ranges and instrument parameters as provided in the context.
Note: The Fido.fetch calls are provided as comments so that the query results can 
be inspected before downloading any data.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ---------------------------
# Query for SDO/HMI Data
# ---------------------------
# HMI observes the Doppler shift of the Fe I 6173 Å spectral line.
# The context specifies a time range from April 2010 to June 2017.
hmi_start = '2010-04-01'
hmi_end = '2017-06-30'
hmi_time = a.Time(hmi_start, hmi_end)

# Specify the source and instrument (SDO/HMI)
hmi_source = a.Source('SDO')
hmi_instrument = a.Instrument('HMI')

# Define the wavelength range according to the VSO interface: 6173.0 - 6174.0 Angstrom.
hmi_wavelength = a.Wavelength(6173 * u.Angstrom, 6174 * u.Angstrom)

# Build and execute the query for HMI data.
hmi_search_result = Fido.search(hmi_time, hmi_source, hmi_instrument, hmi_wavelength)
print("SDO/HMI Query Results:")
print(hmi_search_result)
# To download HMI data, uncomment the following line:
# hmi_files = Fido.fetch(hmi_search_result)

# ---------------------------
# Query for SOHO/MDI Data
# ---------------------------
# MDI (on board SOHO) observes the Ni I 6768 Å line.
# The context indicates a data period from May 1996 to April 2011.
mdi_start = '1996-05-01'
mdi_end = '2011-04-30'
mdi_time = a.Time(mdi_start, mdi_end)

# Specify the source and instrument (SOHO/MDI)
mdi_source = a.Source('SOHO')
mdi_instrument = a.Instrument('MDI')

# Define the exact wavelength for MDI data: 6768.0 Angstrom.
mdi_wavelength = a.Wavelength(6768 * u.Angstrom, 6768 * u.Angstrom)

# Build and execute the query for MDI data.
mdi_search_result = Fido.search(mdi_time, mdi_source, mdi_instrument, mdi_wavelength)
print("SOHO/MDI Query Results:")
print(mdi_search_result)
# To download MDI data, uncomment the following line:
# mdi_files = Fido.fetch(mdi_search_result)

if __name__ == '__main__':
    # Running the script will display the query results in the console.
    pass
