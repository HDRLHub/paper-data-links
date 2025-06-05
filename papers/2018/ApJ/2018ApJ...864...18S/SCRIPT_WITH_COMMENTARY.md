# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query data from the Virtual Solar Observatory (VSO) using SunPy.
We construct three explicit queries for:
  1. SDO/HMI line-of-sight (LOS) magnetogram data at 7 March 2011 06:00 UT.
  2. STEREO_A SECCHI coronagraph data (using the COR1 detector) around 7 March 2011.
  3. SOHO/LASCO coronagraph data (using the C2 detector) around 7 March 2011.
  
The queries reflect the instrumentation and time ranges as described in the paper's context.
Note: The Fido.fetch commands are commented out.
"""

from sunpy.net import Fido, attrs as a
from astropy import time

# Define query times based on the paper context.
# For SDO/HMI, a LOS magnetogram known to be taken at 7 March 2011 06:00 UT.
hmi_start = '2011-03-07T06:00:00'
hmi_end = '2011-03-07T06:10:00'

# For coronagraph observations (STEREO and SOHO) we choose a short interval around the CME event.
cme_start = '2011-03-07T06:00:00'
cme_end = '2011-03-07T06:15:00'

# 1. Query SDO/HMI data for LOS magnetograms.
# Data is available from SDO/HMI as described in the VSO interface.
# We use the 'LOS_magnetic_field' physical observable and set the instrument to 'HMI'.
query_hmi = Fido.search(
    a.Time(hmi_start, hmi_end),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print("Query Results for SDO/HMI LOS magnetogram:")
print(query_hmi)

# Uncomment the following line to download HMI data:
# hmi_files = Fido.fetch(query_hmi)

# 2. Query STEREO_A SECCHI data using the COR1 detector (coronagraph images).
# In the context, SECCHI coronagraph images from STEREO A are used.
query_stereo_a = Fido.search(
    a.Time(cme_start, cme_end),
    a.Source('STEREO_A'),
    a.Instrument('SECCHI'),
    a.Detector('COR1')
)
print("\nQuery Results for STEREO_A SECCHI COR1 coronagraph data:")
print(query_stereo_a)

# Uncomment the following line to download STEREO_A data:
# stereo_a_files = Fido.fetch(query_stereo_a)

# 3. Query SOHO/LASCO data using the C2 detector.
# SOHO LASCO C2 provides white-light coronagraph data as required for the CME reconstruction.
query_soho_lasco = Fido.search(
    a.Time(cme_start, cme_end),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("\nQuery Results for SOHO/LASCO C2 coronagraph data:")
print(query_soho_lasco)

# Uncomment the following line to download SOHO/LASCO data:
# soho_lasco_files = Fido.fetch(query_soho_lasco)

if __name__ == '__main__':
    # This main guard allows the script to be run stand-alone.
    pass
