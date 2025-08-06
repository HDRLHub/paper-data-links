# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Note: TESIS (CORONAS-PHOTON) EUV, Mg XII spectroheliograph, and SphinX instruments
# are not available via the Virtual Solar Observatory interface. Requests for these
# data must be handled through their native archives.

# 1. SOHO/EIT 304 Å to fill TESIS 304 Å data gaps on 2009-04-23
time_eit = a.Time("2009-04-23T02:00:00", "2009-04-23T11:00:00")
instrument_eit = a.Instrument("EIT")
wavelength_eit = a.Wavelength(304 * u.angstrom)

query_eit_304 = Fido.search(time_eit,
                            a.Source("SOHO"),
                            instrument_eit,
                            wavelength_eit)
print("SOHO/EIT 304 Å query results:")
print(query_eit_304)
# To download the data, uncomment the following line:
# Fido.fetch(query_eit_304)

# 2. SOHO/LASCO C2 white-light coronagraph for CME tracking from 07:38 to 11:00 UT
time_lasco_c2 = a.Time("2009-04-23T07:38:00", "2009-04-23T11:00:00")
instrument_lasco = a.Instrument("LASCO")
detector_c2 = a.Detector("C2")

query_lasco_c2 = Fido.search(time_lasco_c2,
                             a.Source("SOHO"),
                             instrument_lasco,
                             detector_c2)
print("\nSOHO/LASCO C2 white-light query results:")
print(query_lasco_c2)
# Fido.fetch(query_lasco_c2)

# 3. SOHO/LASCO C3 white-light coronagraph for extended CME evolution
detector_c3 = a.Detector("C3")

query_lasco_c3 = Fido.search(time_lasco_c2,  # same time range as C2
                             a.Source("SOHO"),
                             instrument_lasco,
                             detector_c3)
print("\nSOHO/LASCO C3 white-light query results:")
print(query_lasco_c3)
# Fido.fetch(query_lasco_c3)

# 4. STEREO-B/EUVI multi-wavelength imaging for prominence geometry and ribbon evolution
time_euvi = a.Time("2009-04-23T02:51:00", "2009-04-23T10:00:00")
source_stb = a.Source("STEREO_B")
instrument_secchi = a.Instrument("SECCHI")
detector_euvi = a.Detector("EUVI")

# EUVI 171 Å
query_euvi_171 = Fido.search(time_euvi,
                             source_stb,
                             instrument_secchi,
                             detector_euvi,
                             a.Wavelength(171 * u.angstrom))
print("\nSTEREO-B EUVI 171 Å query results:")
print(query_euvi_171)
# Fido.fetch(query_euvi_171)

# EUVI 195 Å
query_euvi_195 = Fido.search(time_euvi,
                             source_stb,
                             instrument_secchi,
                             detector_euvi,
                             a.Wavelength(195 * u.angstrom))
print("\nSTEREO-B EUVI 195 Å query results:")
print(query_euvi_195)
# Fido.fetch(query_euvi_195)

# EUVI 284 Å
query_euvi_284 = Fido.search(time_euvi,
                             source_stb,
                             instrument_secchi,
                             detector_euvi,
                             a.Wavelength(284 * u.angstrom))
print("\nSTEREO-B EUVI 284 Å query results:")
print(query_euvi_284)
# Fido.fetch(query_euvi_284)

# EUVI 304 Å
query_euvi_304 = Fido.search(time_euvi,
                             source_stb,
                             instrument_secchi,
                             detector_euvi,
                             a.Wavelength(304 * u.angstrom))
print("\nSTEREO-B EUVI 304 Å query results:")
print(query_euvi_304)
# Fido.fetch(query_euvi_304)

# 5. STEREO A & B COR1 and COR2 white-light coronagraphs for outer-corona CME kinematics
time_cor = a.Time("2009-04-23T04:00:00", "2009-04-23T11:00:00")
detector_cor1 = a.Detector("COR1")
detector_cor2 = a.Detector("COR2")

# STEREO-A COR1
query_sta_cor1 = Fido.search(time_cor,
                             a.Source("STEREO_A"),
                             instrument_secchi,
                             detector_cor1)
print("\nSTEREO-A COR1 white-light query results:")
print(query_sta_cor1)
# Fido.fetch(query_sta_cor1)

# STEREO-A COR2
query_sta_cor2 = Fido.search(time_cor,
                             a.Source("STEREO_A"),
                             instrument_secchi,
                             detector_cor2)
print("\nSTEREO-A COR2 white-light query results:")
print(query_sta_cor2)
# Fido.fetch(query_sta_cor2)

# STEREO-B COR1
query_stb_cor1 = Fido.search(time_cor,
                             a.Source("STEREO_B"),
                             instrument_secchi,
                             detector_cor1)
print("\nSTEREO-B COR1 white-light query results:")
print(query_stb_cor1)
# Fido.fetch(query_stb_cor1)

# STEREO-B COR2
query_stb_cor2 = Fido.search(time_cor,
                             a.Source("STEREO_B"),
                             instrument_secchi,
                             detector_cor2)
print("\nSTEREO-B COR2 white-light query results:")
print(query_stb_cor2)
# Fido.fetch(query_stb_cor2)
