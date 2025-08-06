# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Download VIRGO Total Solar Irradiance (TSI) data from the Virtual Solar Observatory (VSO)
Time Range: 1996-01-01 to 2015-12-31
Instrument: VIRGO on SOHO
Detectors: DIARAD and PMOD
Physical Observable: intensity (broadband TSI)
"""
import sunpy.net.vso as vso
from sunpy.net import attrs as a

# Initialize the VSO client
client = vso.VSOClient()

# Define the common time range for the study
time_range = a.Time('1996-01-01', '2015-12-31')

# Define the common instrument and physical observable
instrument = a.Instrument('VIRGO')
physobs = a.Physobs('intensity')

# --------------------------------------------------------------------------
# Query 1: VIRGO DIARAD detector (broadband TSI)
# --------------------------------------------------------------------------
detector_diarad = a.Detector('DIARAD')
result_diarad = client.search(time_range, instrument, detector_diarad, physobs)
print("Search results for VIRGO DIARAD (TSI):")
print(result_diarad)
# To download this data, uncomment the following line:
# client.fetch(result_diarad)

# --------------------------------------------------------------------------
# Query 2: VIRGO PMOD detector (broadband TSI)
# --------------------------------------------------------------------------
detector_pmod = a.Detector('PMOD')
result_pmod = client.search(time_range, instrument, detector_pmod, physobs)
print("\nSearch results for VIRGO PMOD (TSI):")
print(result_pmod)
# To download this data, uncomment the following line:
# client.fetch(result_pmod)
