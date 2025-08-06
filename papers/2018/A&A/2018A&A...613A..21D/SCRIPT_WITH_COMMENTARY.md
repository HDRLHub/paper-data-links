# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net as net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Query 1: STEREO-A / PLASTIC number density from 2013-12-25 to 2013-12-31
time1 = a.Time('2013-12-25', '2013-12-31')
plastic_density_query = Fido.search(
    time1,
    a.Source('STEREO_A'),
    a.Instrument('PLASTIC'),
    a.Detector('SWS'),
    a.Physobs('number_density')
)
print(plastic_density_query)
# Fido.fetch(plastic_density_query)

# Query 2: STEREO-A / PLASTIC solar wind velocity from 2013-12-25 to 2013-12-31
plastic_velocity_query = Fido.search(
    time1,
    a.Source('STEREO_A'),
    a.Instrument('PLASTIC'),
    a.Detector('SWS'),
    a.Physobs('particle_velocity')
)
print(plastic_velocity_query)
# Fido.fetch(plastic_velocity_query)

# Query 3: STEREO-A / PLASTIC thermal velocity from 2013-12-25 to 2013-12-31
plastic_thermal_query = Fido.search(
    time1,
    a.Source('STEREO_A'),
    a.Instrument('PLASTIC'),
    a.Detector('SWS'),
    a.Physobs('thermal_velocity')
)
print(plastic_thermal_query)
# Fido.fetch(plastic_thermal_query)

# Query 4: STEREO-A / SECCHI EUVI 195 Å images from 2013-12-26 02:10 to 2013-12-26 04:27
time2 = a.Time('2013-12-26 02:10', '2013-12-26 04:27')
euvi_query = Fido.search(
    time2,
    a.Source('STEREO_A'),
    a.Instrument('SECCHI'),
    a.Detector('EUVI'),
    a.Wavelength(195 * u.angstrom)
)
print(euvi_query)
# Fido.fetch(euvi_query)

# Query 5: STEREO-A / SECCHI COR1 white-light images from 2013-12-26 02:10 to 2013-12-26 04:27
cor1_query = Fido.search(
    time2,
    a.Source('STEREO_A'),
    a.Instrument('SECCHI'),
    a.Detector('COR1')
)
print(cor1_query)
# Fido.fetch(cor1_query)

# Query 6: STEREO-A / SECCHI COR2 white-light images from 2013-12-26 02:10 to 2013-12-26 04:27
cor2_query = Fido.search(
    time2,
    a.Source('STEREO_A'),
    a.Instrument('SECCHI'),
    a.Detector('COR2')
)
print(cor2_query)
# Fido.fetch(cor2_query)

# Query 7: STEREO-A / SWAVES LFR radio intensity from 2013-12-26 02:30 to 2013-12-26 04:40
time3 = a.Time('2013-12-26 02:30', '2013-12-26 04:40')
swaves_query = Fido.search(
    time3,
    a.Source('STEREO_A'),
    a.Instrument('SWAVES'),
    a.Detector('LFR')
)
print(swaves_query)
# Fido.fetch(swaves_query)

# Query 8: SOHO / LASCO C2 coronagraph images from 2013-12-26 02:30 to 2013-12-26 07:24
time4 = a.Time('2013-12-26 02:30', '2013-12-26 07:24')
lasco_query = Fido.search(
    time4,
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print(lasco_query)
# Fido.fetch(lasco_query)

# Query 9: SDO / AIA EUV images from 2013-12-26 04:00 to 2013-12-26 04:05
time5 = a.Time('2013-12-26 04:00', '2013-12-26 04:05')
aia_query = Fido.search(
    time5,
    a.Source('SDO'),
    a.Instrument('AIA')
)
print(aia_query)
# Fido.fetch(aia_query)
