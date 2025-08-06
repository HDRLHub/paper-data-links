# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
import astropy.units as u
from sunpy.net import Fido, attrs as a

# This script searches for VSO data needed for analysis of the 14 June 2012 CME event
# Instruments: SDO/AIA, SDO/HMI, SOHO/LASCO C2
# Time ranges and wavelengths are taken directly from the context

# 1. SDO/AIA EUV imaging at 131 Å from 13:00–14:00 UT on 14 June 2012
time_aia = a.Time("2012-06-14T13:00:00", "2012-06-14T14:00:00")
inst_aia = a.Instrument('AIA')
wave_131 = a.Wavelength(131.0 * u.Angstrom, 131.0 * u.Angstrom)

result_aia_131 = Fido.search(time_aia, inst_aia, wave_131)
print("AIA 131 Å search results:")
print(result_aia_131)
# Uncomment to download:
# files_aia_131 = Fido.fetch(result_aia_131)

# 2. SDO/AIA EUV imaging at 94 Å from 13:00–14:00 UT on 14 June 2012
wave_94 = a.Wavelength(94.0 * u.Angstrom, 94.0 * u.Angstrom)

result_aia_94 = Fido.search(time_aia, inst_aia, wave_94)
print("AIA 94 Å search results:")
print(result_aia_94)
# Uncomment to download:
# files_aia_94 = Fido.fetch(result_aia_94)

# 3. SDO/HMI line-of-sight magnetograms (Fe I 6173 Å) from 08–21 June 2012
time_hmi_los = a.Time("2012-06-08T00:00:00", "2012-06-21T23:59:59")
inst_hmi = a.Instrument('HMI')
wave_6173 = a.Wavelength(6173.0 * u.Angstrom, 6173.0 * u.Angstrom)
physobs_los = a.Physobs('LOS_magnetic_field')

result_hmi_los = Fido.search(time_hmi_los, inst_hmi, wave_6173, physobs_los)
print("HMI LOS magnetogram search results:")
print(result_hmi_los)
# Uncomment to download:
# files_hmi_los = Fido.fetch(result_hmi_los)

# 4. SDO/HMI vector magnetic field (Fe I 6173 Å) from 08–21 June 2012
physobs_vec = a.Physobs('vector_magnetic_field')

result_hmi_vec = Fido.search(time_hmi_los, inst_hmi, wave_6173, physobs_vec)
print("HMI vector magnetic field search results:")
print(result_hmi_vec)
# Uncomment to download:
# files_hmi_vec = Fido.fetch(result_hmi_vec)

# 5. SOHO/LASCO C2 coronagraph images around the CME time on 14 June 2012
#    Event observed at ~14:12 UT; we search from 14:12–14:15 UT for context
time_lasco = a.Time("2012-06-14T14:12:00", "2012-06-14T14:15:00")
inst_lasco = a.Instrument('LASCO')
det_c2 = a.Detector('C2')

result_lasco_c2 = Fido.search(time_lasco, inst_lasco, det_c2)
print("LASCO C2 search results:")
print(result_lasco_c2)
# Uncomment to download:
# files_lasco_c2 = Fido.fetch(result_lasco_c2)

print("Query script complete.")
