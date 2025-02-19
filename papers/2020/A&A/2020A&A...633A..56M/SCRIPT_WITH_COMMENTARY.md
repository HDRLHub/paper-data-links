# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query data for a study of a CME-driven shock observed during a C7.7 solar flare on 2017 September 2.
We query:
  1. SUVI data from GOES-16 in the 195 Å channel (EUV) used for imaging the shock/CME from 15:32:56 to 15:40:56 UT.
  2. LASCO C2 white-light coronagraph images from SOHO, also covering the interval 15:32:56 to 15:40:56 UT.
  
The SUVI instrument on GOES-16 has available wavelengths including 195 Å.
LASCO C2 is specified as the detector for SOHO LASCO.
Note that Fido.fetch commands are provided but commented out.
"""

import sunpy.net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the observations (2017-09-02 from 15:32:56 to 15:40:56 UT)
start_time = '2017-09-02T15:32:56'
end_time = '2017-09-02T15:40:56'

#======================================================================
# Query 1: GOES-16 SUVI Data in EUV at 195 Å
#----------------------------------------------------------------------
# SUVI provides EUV images in several channels including 195 Å.
# We use a.Wavelength keyword set to 195 Å.
query_suvi = Fido.search(
    a.Time(start_time, end_time),
    a.Source('GOES16'),
    a.Instrument('SUVI'),
    a.Wavelength(195 * u.angstrom)
)
print("Query Results for GOES-16 SUVI 195 Å data:")
print(query_suvi)

# Uncomment the following line to fetch the SUVI data:
# data_suvi = Fido.fetch(query_suvi)

#======================================================================
# Query 2: SOHO LASCO C2 White-Light Data
#----------------------------------------------------------------------
# LASCO data in white-light are recorded by various detectors.
# Here, we specifically query for LASCO data from detector 'C2' on board SOHO.
query_lasco_c2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("\nQuery Results for SOHO LASCO C2 white-light data:")
print(query_lasco_c2)

# Uncomment the following line to fetch the LASCO C2 data:
# data_lasco_c2 = Fido.fetch(query_lasco_c2)

# End of script.
    
if __name__ == '__main__':
    print("VSO query script execution complete.")
