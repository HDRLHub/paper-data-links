# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido
from sunpy.net.vso import attrs as a

# Define time ranges for the observations
time_aia = a.Time('2011-05-11 02:00:00', '2011-05-11 04:00:00')
time_hmi = a.Time('2011-05-11 02:00:00', '2011-05-11 03:00:00')
time_lasco = a.Time('2011-05-11 02:48:00', '2011-05-11 04:00:00')

# ----------------------------------------------------------------------
# 1) Query SDO/AIA for the EUV channels used in the analysis:
#    171 Å, 193 Å, 211 Å, and 335 Å over the flare and EUV wave period.
# ----------------------------------------------------------------------

# AIA 171 Å
result_aia171 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(171 * u.angstrom))
print("AIA 171 Å results:")
print(result_aia171)
# files_aia171 = Fido.fetch(result_aia171)

# AIA 193 Å
result_aia193 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(193 * u.angstrom))
print("AIA 193 Å results:")
print(result_aia193)
# files_aia193 = Fido.fetch(result_aia193)

# AIA 211 Å
result_aia211 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(211 * u.angstrom))
print("AIA 211 Å results:")
print(result_aia211)
# files_aia211 = Fido.fetch(result_aia211)

# AIA 335 Å
result_aia335 = Fido.search(time_aia,
                            a.Instrument('AIA'),
                            a.Wavelength(335 * u.angstrom))
print("AIA 335 Å results:")
print(result_aia335)
# files_aia335 = Fido.fetch(result_aia335)


# ----------------------------------------------------------------------
# 2) Query SDO/HMI for photospheric LOS magnetic field 
#    around the filament eruption (02:00 – 03:00 UT).
# ----------------------------------------------------------------------

result_hmi_los = Fido.search(time_hmi,
                             a.Instrument('HMI'),
                             a.Wavelength(6173 * u.angstrom),
                             a.Physobs('LOS_magnetic_field'))
print("HMI LOS Magnetic Field results:")
print(result_hmi_los)
# files_hmi_los = Fido.fetch(result_hmi_los)


# ----------------------------------------------------------------------
# 3) Query SOHO/LASCO C2 white-light coronagraph data 
#    for the CME propagation starting at 02:48 UT.
# ----------------------------------------------------------------------

result_lasco_c2 = Fido.search(time_lasco,
                              a.Source('SOHO'),
                              a.Instrument('LASCO'),
                              a.Detector('C2'))
print("SOHO LASCO C2 results:")
print(result_lasco_c2)
# files_lasco_c2 = Fido.fetch(result_lasco_c2)
