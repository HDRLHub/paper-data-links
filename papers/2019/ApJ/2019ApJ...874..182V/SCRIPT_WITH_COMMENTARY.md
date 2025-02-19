# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy to construct VSO queries for downloading solar data related to
the formation and eruption of a sigmoidal structure in active region NOAA 11942.
The instruments used are:
  1. Atmospheric Imaging Assembly (AIA) on board SDO
  2. Helioseismic and Magnetic Imager (HMI) on board SDO
  3. Large Angle and Spectrometric Coronagraph (LASCO) on board SOHO

For AIA, we query two distinct periods:
  - Period 1 (AR evolution and sigmoid build-up): 03 Jan 2014 12:20 UT to 05 Jan 2014 20:40 UT,
    specifically targeting 171 Å images.
  - Period 2 (Filament initiation, eruption, and reconnection): 06 Jan 2014 05:35 UT to 07 Jan 2014 01:00 UT,
    here we target 304 Å images as they capture the filament material.

For HMI, we query observations tracking the photospheric magnetic field evolution 
from around 04 Jan 2014 to 07 Jan 2014.

For LASCO, we have two queries:
  - LASCO/C2: To capture the initial appearance of the CME (around 23:00 UT to 23:30 UT on 06 Jan 2014).
  - LASCO/C3: To track the CME propagation later on 07 Jan 2014 (from 00:42 UT to 08:00 UT).
  
Note: Fido.fetch commands are provided but commented out, so that no actual data download is initiated.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# -----------------------
# Query 1: AIA Data (Period 1: Sigmoid Build-Up)
# Time Range: 2014-01-03T12:20 to 2014-01-05T20:40
# Instrument: SDO/AIA, using the 171 Å wavelength channel
# -----------------------
time_range_aia_p1 = a.Time('2014-01-03T12:20', '2014-01-05T20:40')
instrument_aia = a.Instrument('AIA')
wavelength_171 = a.Wavelength(171 * u.angstrom)
# Construct and print the query for AIA period 1
result_aia_p1 = Fido.search(time_range_aia_p1, instrument_aia, wavelength_171)
print("AIA Period 1 Query Result:")
print(result_aia_p1)
# To fetch the data (disabled):
# files_aia_p1 = Fido.fetch(result_aia_p1)

# -----------------------
# Query 2: AIA Data (Period 2: Filament Initiation and Eruption)
# Time Range: 2014-01-06T05:35 to 2014-01-07T01:00
# Instrument: SDO/AIA, using the 304 Å wavelength to capture filament evolution
# -----------------------
time_range_aia_p2 = a.Time('2014-01-06T05:35', '2014-01-07T01:00')
wavelength_304 = a.Wavelength(304 * u.angstrom)
# Construct and print the query for AIA period 2
result_aia_p2 = Fido.search(time_range_aia_p2, instrument_aia, wavelength_304)
print("\nAIA Period 2 Query Result:")
print(result_aia_p2)
# To fetch the data (disabled):
# files_aia_p2 = Fido.fetch(result_aia_p2)

# -----------------------
# Query 3: HMI Data (Photospheric Magnetic Field Evolution)
# Time Range: 2014-01-04T00:00 to 2014-01-07T23:59
# Instrument: SDO/HMI (e.g., LOS magnetic field observations)
# -----------------------
time_range_hmi = a.Time('2014-01-04T00:00', '2014-01-07T23:59')
instrument_hmi = a.Instrument('HMI')
# Construct and print the query for HMI data
result_hmi = Fido.search(time_range_hmi, instrument_hmi)
print("\nHMI Query Result:")
print(result_hmi)
# To fetch the data (disabled):
# files_hmi = Fido.fetch(result_hmi)

# -----------------------
# Query 4: LASCO Data (C2 - CME Initial Appearance)
# Time Range: 2014-01-06T23:00 to 2014-01-06T23:30
# Instrument: SOHO/LASCO, Detector: C2
# -----------------------
time_range_lasco_c2 = a.Time('2014-01-06T23:00', '2014-01-06T23:30')
# Note: Specify the source to distinguish SOHO data.
source_soho = a.Source('SOHO')
detector_c2 = a.Detector('C2')
instrument_lasco = a.Instrument('LASCO')
# Construct and print the query for LASCO/C2 data
result_lasco_c2 = Fido.search(time_range_lasco_c2, source_soho, instrument_lasco, detector_c2)
print("\nLASCO/C2 Query Result:")
print(result_lasco_c2)
# To fetch the data (disabled):
# files_lasco_c2 = Fido.fetch(result_lasco_c2)

# -----------------------
# Query 5: LASCO Data (C3 - Extended CME Tracking)
# Time Range: 2014-01-07T00:42 to 2014-01-07T08:00
# Instrument: SOHO/LASCO, Detector: C3
# -----------------------
time_range_lasco_c3 = a.Time('2014-01-07T00:42', '2014-01-07T08:00')
detector_c3 = a.Detector('C3')
# Construct and print the query for LASCO/C3 data
result_lasco_c3 = Fido.search(time_range_lasco_c3, source_soho, instrument_lasco, detector_c3)
print("\nLASCO/C3 Query Result:")
print(result_lasco_c3)
# To fetch the data (disabled):
# files_lasco_c3 = Fido.fetch(result_lasco_c3)

if __name__ == '__main__':
    print("\nAll queries executed; data fetching commands remain commented out.")
