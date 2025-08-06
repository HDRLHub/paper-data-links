# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query 1: EIT 284 Å pre-eruption context on 2001-12-20
time_pre_eruption = a.Time('2001-12-20T19:05:00', '2001-12-20T19:10:00')
instrument_eit = a.Instrument('EIT')
wavelength_284 = a.Wavelength(284 * u.Angstrom)
search_eit_pre = Fido.search(time_pre_eruption,
                             a.Source('SOHO'),
                             instrument_eit,
                             wavelength_284)
print(search_eit_pre)
# fetched_files_eit_pre = Fido.fetch(search_eit_pre)

# Query 2: EIT 195 Å running-difference images during main eruption (04:47–05:22 UT) on 2001-12-26
time_main_eruption = a.Time('2001-12-26T04:47:00', '2001-12-26T05:22:00')
wavelength_195 = a.Wavelength(195 * u.Angstrom)
search_eit_main = Fido.search(time_main_eruption,
                              a.Source('SOHO'),
                              instrument_eit,
                              wavelength_195)
print(search_eit_main)
# fetched_files_eit_main = Fido.fetch(search_eit_main)

# Query 3: MDI magnetogram at 04:51 UT on 2001-12-26 for LOS magnetic field
time_mdi = a.Time('2001-12-26T04:51:00', '2001-12-26T04:52:00')
instrument_mdi = a.Instrument('MDI')
physobs_magnetic = a.Physobs('LOS_magnetic_field')
search_mdi = Fido.search(time_mdi,
                         a.Source('SOHO'),
                         instrument_mdi,
                         physobs_magnetic)
print(search_mdi)
# fetched_files_mdi = Fido.fetch(search_mdi)

# Query 4: LASCO-C2 white-light images from 05:29 to 08:41 UT on 2001-12-26
time_lasco = a.Time('2001-12-26T05:29:00', '2001-12-26T08:41:00')
search_lasco_c2 = Fido.search(time_lasco,
                              a.Source('SOHO'),
                              a.Instrument('LASCO'),
                              a.Detector('C2'))
print(search_lasco_c2)
# fetched_files_lasco_c2 = Fido.fetch(search_lasco_c2)

# Query 5: LASCO-C3 white-light images from 05:29 to 08:41 UT on 2001-12-26
search_lasco_c3 = Fido.search(time_lasco,
                              a.Source('SOHO'),
                              a.Instrument('LASCO'),
                              a.Detector('C3'))
print(search_lasco_c3)
# fetched_files_lasco_c3 = Fido.fetch(search_lasco_c3)

# Query 6: TRACE 1600 Å images of flare ribbons and jet (04:23:38–05:19:57 UT) on 2001-12-26
time_trace = a.Time('2001-12-26T04:23:38', '2001-12-26T05:19:57')
instrument_trace = a.Instrument('TRACE')
wavelength_1600 = a.Wavelength(1600 * u.Angstrom)
search_trace = Fido.search(time_trace,
                           a.Source('TRACE'),
                           instrument_trace,
                           wavelength_1600)
print(search_trace)
# fetched_files_trace = Fido.fetch(search_trace)
