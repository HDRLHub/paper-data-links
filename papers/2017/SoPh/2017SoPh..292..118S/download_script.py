# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a

# Define the common time range for the 38 CMEs studied (2010-03-19 to 2013-12-07 UT)
time_range = a.Time('2010-03-19', '2013-12-07')

# 1. Query SOHO LASCO C2 white-light coronagraph data
source_soho = a.Source('SOHO')
instrument_lasco = a.Instrument('LASCO')
detector_c2 = a.Detector('C2')

print("Searching for SOHO LASCO C2 data...")
query_lasco_c2 = Fido.search(time_range, source_soho, instrument_lasco, detector_c2)
print(query_lasco_c2)
# To download: uncomment the line below
# files_lasco_c2 = Fido.fetch(query_lasco_c2)

# 2. Query STEREO-A SECCHI COR2 white-light coronagraph data
source_stereo_a = a.Source('STEREO_A')
instrument_secchi = a.Instrument('SECCHI')
detector_cor2 = a.Detector('COR2')

print("Searching for STEREO-A SECCHI COR2 data...")
query_stereo_a_cor2 = Fido.search(time_range, source_stereo_a, instrument_secchi, detector_cor2)
print(query_stereo_a_cor2)
# To download: uncomment the line below
# files_stereo_a_cor2 = Fido.fetch(query_stereo_a_cor2)

# 3. Query STEREO-B SECCHI COR2 white-light coronagraph data
source_stereo_b = a.Source('STEREO_B')

print("Searching for STEREO-B SECCHI COR2 data...")
query_stereo_b_cor2 = Fido.search(time_range, source_stereo_b, instrument_secchi, detector_cor2)
print(query_stereo_b_cor2)
# To download: uncomment the line below
# files_stereo_b_cor2 = Fido.fetch(query_stereo_b_cor2)

# 4. Query STEREO-A SECCHI HI1 heliospheric imager data
detector_hi1 = a.Detector('HI1')

print("Searching for STEREO-A SECCHI HI1 data...")
query_stereo_a_hi1 = Fido.search(time_range, source_stereo_a, instrument_secchi, detector_hi1)
print(query_stereo_a_hi1)
# To download: uncomment the line below
# files_stereo_a_hi1 = Fido.fetch(query_stereo_a_hi1)

# 5. Query STEREO-B SECCHI HI1 heliospheric imager data
print("Searching for STEREO-B SECCHI HI1 data...")
query_stereo_b_hi1 = Fido.search(time_range, source_stereo_b, instrument_secchi, detector_hi1)
print(query_stereo_b_hi1)
# To download: uncomment the line below
# files_stereo_b_hi1 = Fido.fetch(query_stereo_b_hi1)

# 6. (Optional) Query STEREO-A SECCHI HI2 heliospheric imager data for extended coverage
detector_hi2 = a.Detector('HI2')

print("Searching for STEREO-A SECCHI HI2 data...")
query_stereo_a_hi2 = Fido.search(time_range, source_stereo_a, instrument_secchi, detector_hi2)
print(query_stereo_a_hi2)
# To download: uncomment the line below
# files_stereo_a_hi2 = Fido.fetch(query_stereo_a_hi2)

# 7. (Optional) Query STEREO-B SECCHI HI2 heliospheric imager data for extended coverage
print("Searching for STEREO-B SECCHI HI2 data...")
query_stereo_b_hi2 = Fido.search(time_range, source_stereo_b, instrument_secchi, detector_hi2)
print(query_stereo_b_hi2)
# To download: uncomment the line below
# files_stereo_b_hi2 = Fido.fetch(query_stereo_b_hi2)

print("All queries completed. Review printed search tables for available files.")
