# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ----------------------------------------------------------------------
# 1. SOHO/EIT Group A events: 195 Å images, 2010-05-23 to 2010-07-19
# ----------------------------------------------------------------------
time_eit_group_a = a.Time('2010-05-23T00:00:00', '2010-07-19T23:59:59')
source_soho = a.Source('SOHO')
instrument_eit = a.Instrument('EIT')
wavelength_195 = a.Wavelength(195.0 * u.Angstrom)

result_eit_group_a = Fido.search(source_soho, instrument_eit, wavelength_195, time_eit_group_a)
print("SOHO/EIT Group A search results:")
print(result_eit_group_a)
# To download: uncomment the next line
# files_eit_group_a = Fido.fetch(result_eit_group_a)

# ----------------------------------------------------------------------
# 2. SOHO/EIT Group B events: 195 Å images, 2011-09-06 to 2015-11-09
# ----------------------------------------------------------------------
time_eit_group_b = a.Time('2011-09-06T00:00:00', '2015-11-09T23:59:59')

result_eit_group_b = Fido.search(source_soho, instrument_eit, wavelength_195, time_eit_group_b)
print("\nSOHO/EIT Group B search results:")
print(result_eit_group_b)
# To download: uncomment the next line
# files_eit_group_b = Fido.fetch(result_eit_group_b)

# ----------------------------------------------------------------------
# 3. SOHO/MDI magnetograms: LOS magnetic field, 2010-05-01 to 2011-04-30
# ----------------------------------------------------------------------
instrument_mdi = a.Instrument('MDI')
physobs_los_mf = a.Physobs('LOS_magnetic_field')
time_mdi_overlap = a.Time('2010-05-01T00:00:00', '2011-04-30T23:59:59')

result_mdi_overlap = Fido.search(source_soho, instrument_mdi, physobs_los_mf, time_mdi_overlap)
print("\nSOHO/MDI overlap period search results:")
print(result_mdi_overlap)
# To download: uncomment the next line
# files_mdi_overlap = Fido.fetch(result_mdi_overlap)

# ----------------------------------------------------------------------
# 4. SDO/AIA images: 193 Å, 2010-05-23 to 2015-11-09
# ----------------------------------------------------------------------
source_sdo = a.Source('SDO')
instrument_aia = a.Instrument('AIA')
wavelength_193 = a.Wavelength(193.0 * u.Angstrom)
time_aia_full = a.Time('2010-05-23T00:00:00', '2015-11-09T23:59:59')

result_aia_full = Fido.search(source_sdo, instrument_aia, wavelength_193, time_aia_full)
print("\nSDO/AIA full period search results:")
print(result_aia_full)
# To download: uncomment the next line
# files_aia_full = Fido.fetch(result_aia_full)

# ----------------------------------------------------------------------
# 5. SDO/AIA events (Cycle 24): 193 Å, 2012-03-07 to 2015-12-28
# ----------------------------------------------------------------------
time_aia_cycle24 = a.Time('2012-03-07T00:00:00', '2015-12-28T23:59:59')

result_aia_cycle24 = Fido.search(source_sdo, instrument_aia, wavelength_193, time_aia_cycle24)
print("\nSDO/AIA Cycle 24 search results:")
print(result_aia_cycle24)
# To download: uncomment the next line
# files_aia_cycle24 = Fido.fetch(result_aia_cycle24)

# ----------------------------------------------------------------------
# 6. SDO/HMI magnetograms: LOS magnetic field, 2010-05-01 to 2011-04-30
# ----------------------------------------------------------------------
instrument_hmi = a.Instrument('HMI')

result_hmi_overlap = Fido.search(source_sdo, instrument_hmi, physobs_los_mf, time_mdi_overlap)
print("\nSDO/HMI overlap period search results:")
print(result_hmi_overlap)
# To download: uncomment the next line
# files_hmi_overlap = Fido.fetch(result_hmi_overlap)

# ----------------------------------------------------------------------
# 7. SDO/HMI magnetograms (Cycle 24): LOS magnetic field, 2012-03-07 to 2015-12-28
# ----------------------------------------------------------------------
result_hmi_cycle24 = Fido.search(source_sdo, instrument_hmi, physobs_los_mf, time_aia_cycle24)
print("\nSDO/HMI Cycle 24 search results:")
print(result_hmi_cycle24)
# To download: uncomment the next line
# files_hmi_cycle24 = Fido.fetch(result_hmi_cycle24)
