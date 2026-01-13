# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
Sunpy VSO Query Script for SOL2015-12-16 CME Event
This script searches for and prints out VSO query results for:
  - SDO/AIA EUV imaging (131 Å and 171 Å)
  - SDO/HMI vector magnetograms (08:24 UT)
  - SOHO/LASCO white-light coronagraph frames (C2 at 11:12 UT, C3 at 12:30 UT)
Instruments not available in the provided VSO interface (STEREO A COR2, Wind) are noted below.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# 1. SDO/AIA 131 Å imaging: 2015-12-16 08:00 – 08:40 UT
time_aia = a.Time('2015-12-16T08:00', '2015-12-16T08:40')
inst_aia = a.Instrument('AIA')
wave_131 = a.Wavelength(131.0 * u.angstrom)
result_aia_131 = Fido.search(time_aia, inst_aia, wave_131)
print("AIA 131 Å query results:")
print(result_aia_131)
# fetched_files_aia_131 = Fido.fetch(result_aia_131)

# 2. SDO/AIA 171 Å imaging: 2015-12-16 08:00 – 08:40 UT
wave_171 = a.Wavelength(171.0 * u.angstrom)
result_aia_171 = Fido.search(time_aia, inst_aia, wave_171)
print("\nAIA 171 Å query results:")
print(result_aia_171)
# fetched_files_aia_171 = Fido.fetch(result_aia_171)

# 3. SDO/HMI vector magnetogram at 08:24 UT on 2015-12-16
time_hmi = a.Time('2015-12-16T08:24', '2015-12-16T08:24')
inst_hmi = a.Instrument('HMI')
phys_hmi = a.Physobs('vector_magnetic_field')
# HMI data are centered at 6173 Å; optional wavelength specification
wave_hmi = a.Wavelength(6173.0 * u.angstrom)
result_hmi_vec = Fido.search(time_hmi, inst_hmi, phys_hmi, wave_hmi)
print("\nHMI vector magnetic field query results:")
print(result_hmi_vec)
# fetched_files_hmi = Fido.fetch(result_hmi_vec)

# 4. SOHO/LASCO C2 white-light coronagraph at 11:12 UT on 2015-12-16
time_lasco_c2 = a.Time('2015-12-16T11:12', '2015-12-16T11:12')
inst_lasco = a.Instrument('LASCO')
det_c2 = a.Detector('C2')
phys_lasco = a.Physobs('intensity')
result_lasco_c2 = Fido.search(time_lasco_c2, inst_lasco, det_c2, phys_lasco)
print("\nLASCO C2 query results:")
print(result_lasco_c2)
# fetched_files_lasco_c2 = Fido.fetch(result_lasco_c2)

# 5. SOHO/LASCO C3 white-light coronagraph at 12:30 UT on 2015-12-16
time_lasco_c3 = a.Time('2015-12-16T12:30', '2015-12-16T12:30')
det_c3 = a.Detector('C3')
result_lasco_c3 = Fido.search(time_lasco_c3, inst_lasco, det_c3, phys_lasco)
print("\nLASCO C3 query results:")
print(result_lasco_c3)
# fetched_files_lasco_c3 = Fido.fetch(result_lasco_c3)

# Notes:
# - STEREO A COR2 is not available in the provided VSO interface.
# - In situ Wind spacecraft data are not retrievable via VSO in this interface.

if __name__ == "__main__":
    # This script is intended for interactive use; no further action when run as a module.
    pass
