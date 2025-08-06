# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the two 12-hour time intervals for the events
time_event1 = a.Time('2011-09-06T21:45:00', '2011-09-07T09:45:00')
time_event2 = a.Time('2011-12-26T10:46:00', '2011-12-26T22:46:00')

# Define the seven AIA EUV wavelengths used in both events
wavelength_304 = a.Wavelength(304 * u.Angstrom)
wavelength_171 = a.Wavelength(171 * u.Angstrom)
wavelength_193 = a.Wavelength(193 * u.Angstrom)
wavelength_211 = a.Wavelength(211 * u.Angstrom)
wavelength_335 = a.Wavelength(335 * u.Angstrom)
wavelength_94  = a.Wavelength(94  * u.Angstrom)
wavelength_131 = a.Wavelength(131 * u.Angstrom)

# -------------- Event 1: 2011-09-06T21:45 – 2011-09-07T09:45 --------------

# Search for SDO/AIA data in all seven channels for Event 1
result_aia_e1_304 = Fido.search(time_event1, a.Instrument('AIA'), wavelength_304)
print('Event 1 | AIA 304 Å search results:')
print(result_aia_e1_304)
# files_aia_e1_304 = Fido.fetch(result_aia_e1_304)

result_aia_e1_171 = Fido.search(time_event1, a.Instrument('AIA'), wavelength_171)
print('Event 1 | AIA 171 Å search results:')
print(result_aia_e1_171)
# files_aia_e1_171 = Fido.fetch(result_aia_e1_171)

result_aia_e1_193 = Fido.search(time_event1, a.Instrument('AIA'), wavelength_193)
print('Event 1 | AIA 193 Å search results:')
print(result_aia_e1_193)
# files_aia_e1_193 = Fido.fetch(result_aia_e1_193)

result_aia_e1_211 = Fido.search(time_event1, a.Instrument('AIA'), wavelength_211)
print('Event 1 | AIA 211 Å search results:')
print(result_aia_e1_211)
# files_aia_e1_211 = Fido.fetch(result_aia_e1_211)

result_aia_e1_335 = Fido.search(time_event1, a.Instrument('AIA'), wavelength_335)
print('Event 1 | AIA 335 Å search results:')
print(result_aia_e1_335)
# files_aia_e1_335 = Fido.fetch(result_aia_e1_335)

result_aia_e1_94 = Fido.search(time_event1, a.Instrument('AIA'), wavelength_94)
print('Event 1 | AIA 94 Å search results:')
print(result_aia_e1_94)
# files_aia_e1_94 = Fido.fetch(result_aia_e1_94)

result_aia_e1_131 = Fido.search(time_event1, a.Instrument('AIA'), wavelength_131)
print('Event 1 | AIA 131 Å search results:')
print(result_aia_e1_131)
# files_aia_e1_131 = Fido.fetch(result_aia_e1_131)

# Search for SDO/HMI 720s LOS magnetograms for Event 1
result_hmi_e1 = Fido.search(time_event1,
                            a.Instrument('HMI'),
                            a.Physobs('LOS_magnetic_field'))
print('Event 1 | HMI LOS magnetogram search results:')
print(result_hmi_e1)
# files_hmi_e1 = Fido.fetch(result_hmi_e1)

# -------------- Event 2: 2011-12-26T10:46 – 2011-12-26T22:46 --------------

# Search for SDO/AIA data in all seven channels for Event 2
result_aia_e2_304 = Fido.search(time_event2, a.Instrument('AIA'), wavelength_304)
print('Event 2 | AIA 304 Å search results:')
print(result_aia_e2_304)
# files_aia_e2_304 = Fido.fetch(result_aia_e2_304)

result_aia_e2_171 = Fido.search(time_event2, a.Instrument('AIA'), wavelength_171)
print('Event 2 | AIA 171 Å search results:')
print(result_aia_e2_171)
# files_aia_e2_171 = Fido.fetch(result_aia_e2_171)

result_aia_e2_193 = Fido.search(time_event2, a.Instrument('AIA'), wavelength_193)
print('Event 2 | AIA 193 Å search results:')
print(result_aia_e2_193)
# files_aia_e2_193 = Fido.fetch(result_aia_e2_193)

result_aia_e2_211 = Fido.search(time_event2, a.Instrument('AIA'), wavelength_211)
print('Event 2 | AIA 211 Å search results:')
print(result_aia_e2_211)
# files_aia_e2_211 = Fido.fetch(result_aia_e2_211)

result_aia_e2_335 = Fido.search(time_event2, a.Instrument('AIA'), wavelength_335)
print('Event 2 | AIA 335 Å search results:')
print(result_aia_e2_335)
# files_aia_e2_335 = Fido.fetch(result_aia_e2_335)

result_aia_e2_94 = Fido.search(time_event2, a.Instrument('AIA'), wavelength_94)
print('Event 2 | AIA 94 Å search results:')
print(result_aia_e2_94)
# files_aia_e2_94 = Fido.fetch(result_aia_e2_94)

result_aia_e2_131 = Fido.search(time_event2, a.Instrument('AIA'), wavelength_131)
print('Event 2 | AIA 131 Å search results:')
print(result_aia_e2_131)
# files_aia_e2_131 = Fido.fetch(result_aia_e2_131)

# Search for SDO/HMI 720s LOS magnetograms for Event 2
result_hmi_e2 = Fido.search(time_event2,
                            a.Instrument('HMI'),
                            a.Physobs('LOS_magnetic_field'))
print('Event 2 | HMI LOS magnetogram search results:')
print(result_hmi_e2)
# files_hmi_e2 = Fido.fetch(result_hmi_e2)

print("All searches complete. Uncomment the Fido.fetch lines to download the data.")
