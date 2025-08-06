# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido
from sunpy.net.vso import attrs as a

# -----------------------------------------------------------------------------
# Query 1: SDO/AIA 193 Å (Post-Eruption Arcade) on 2013-03-15 ~15:00 UT
# -----------------------------------------------------------------------------
time_aia_193 = a.Time('2013-03-15T14:59:00', '2013-03-15T15:01:00')
source_sdo = a.Source('SDO')
instrument_aia = a.Instrument('AIA')
wavelength_193 = a.Wavelength(193 * u.angstrom)
query_aia_193 = Fido.search(time_aia_193, source_sdo, instrument_aia, wavelength_193)
print('AIA 193 Å PEA Query Results:')
print(query_aia_193)
# Fetch command (commented out)
# files_aia_193 = Fido.fetch(query_aia_193)

# -----------------------------------------------------------------------------
# Query 2: SDO/AIA 1600 Å (Flare Ribbons) on 2013-03-15 ~07:35 UT
# -----------------------------------------------------------------------------
time_aia_1600 = a.Time('2013-03-15T07:34:00', '2013-03-15T07:36:00')
wavelength_1600 = a.Wavelength(1600 * u.angstrom)
query_aia_1600 = Fido.search(time_aia_1600, source_sdo, instrument_aia, wavelength_1600)
print('\nAIA 1600 Å Ribbon Query Results:')
print(query_aia_1600)
# files_aia_1600 = Fido.fetch(query_aia_1600)

# -----------------------------------------------------------------------------
# Query 3: SDO/HMI LOS Magnetogram at 6173 Å on 2013-03-15 ~06:11 UT
# -----------------------------------------------------------------------------
time_hmi = a.Time('2013-03-15T06:10:00', '2013-03-15T06:12:00')
instrument_hmi = a.Instrument('HMI')
physobs_los = a.Physobs('LOS_magnetic_field')
wavelength_6173 = a.Wavelength(6173 * u.angstrom)
query_hmi = Fido.search(time_hmi, source_sdo, instrument_hmi, physobs_los, wavelength_6173)
print('\nHMI LOS Magnetogram Query Results:')
print(query_hmi)
# files_hmi = Fido.fetch(query_hmi)

# -----------------------------------------------------------------------------
# Query 4: SOHO/LASCO C2 White-Light Coronagraph on 2013-03-15 ~07:12 UT
# -----------------------------------------------------------------------------
time_lasco_c2 = a.Time('2013-03-15T07:11:00', '2013-03-15T07:13:00')
source_soho = a.Source('SOHO')
instrument_lasco = a.Instrument('LASCO')
detector_c2 = a.Detector('C2')
query_lasco_c2 = Fido.search(time_lasco_c2, source_soho, instrument_lasco, detector_c2)
print('\nLASCO C2 Query Results:')
print(query_lasco_c2)
# files_lasco_c2 = Fido.fetch(query_lasco_c2)

# -----------------------------------------------------------------------------
# Query 5: STEREO_A/SECCHI COR2 White-Light Coronagraph on 2013-03-15 ~08:08 UT
# -----------------------------------------------------------------------------
time_stereo_a = a.Time('2013-03-15T08:07:00', '2013-03-15T08:09:00')
source_stereo_a = a.Source('STEREO_A')
instrument_secchi = a.Instrument('SECCHI')
detector_cor2 = a.Detector('COR2')
query_cor2_a = Fido.search(time_stereo_a, source_stereo_a, instrument_secchi, detector_cor2)
print('\nSECCHI COR2-A Query Results:')
print(query_cor2_a)
# files_cor2_a = Fido.fetch(query_cor2_a)

# -----------------------------------------------------------------------------
# Query 6: STEREO_B/SECCHI COR2 White-Light Coronagraph on 2013-03-15 ~08:08 UT
# -----------------------------------------------------------------------------
time_stereo_b = a.Time('2013-03-15T08:07:00', '2013-03-15T08:09:00')
source_stereo_b = a.Source('STEREO_B')
query_cor2_b = Fido.search(time_stereo_b, source_stereo_b, instrument_secchi, detector_cor2)
print('\nSECCHI COR2-B Query Results:')
print(query_cor2_b)
# files_cor2_b = Fido.fetch(query_cor2_b)
