# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# GOES_XRS query
result_goes_xrs = Fido.search(
    a.Time("2021-11-01 23:35", "2021-11-02 04:00"),
    a.Instrument("XRS")
)

# Solar_Orbiter_STIX query
result_stix = Fido.search(
    a.Time("2021-11-01 23:35", "2021-11-02 04:00"),
    a.Instrument("STIX"),
    a.Wavelength(4 * u.keV) | a.Wavelength(150 * u.keV)
)

# SDO_AIA query
result_aia = Fido.search(
    a.Time("2021-11-01 23:05", "2021-11-02 01:05"),
    a.Instrument("AIA"),
    a.Wavelength(1600 * u.Angstrom) | a.Wavelength(304 * u.Angstrom) | a.Wavelength(94 * u.Angstrom) | a.Wavelength(211 * u.Angstrom)
)

# STEREO_A_EUVI query
result_euvi = Fido.search(
    a.Time("2021-11-01 23:05", "2021-11-02 01:05"),
    a.Instrument("EUVI")
)

# SOHO_LASCO query
result_lasco = Fido.search(
    a.Time("2021-11-02 02:00", "2021-11-02 04:23"),
    a.Instrument("LASCO")
)

# STEREO_A_SECCHI query
result_secchi = Fido.search(
    a.Time("2021-11-02 01:31", "2021-11-02 04:23"),
    a.Instrument("SECCHI")
)

# Solar_Orbiter_MAG query
result_mag = Fido.search(
    a.Time("2021-11-03 14:30", "2021-11-04 07:00"),
    a.Instrument("MAG")
)

# Solar_Orbiter_SWA query
result_swa = Fido.search(
    a.Time("2021-11-03 14:30", "2021-11-04 07:00"),
    a.Instrument("SWA")
)

# ACE_Wind query
result_wind = Fido.search(
    a.Time("2021-11-03 21:30", "2021-11-04 13:00"),
    a.Instrument("WIND")
)

# Print all results at the end
print("Results for GOES_XRS:")
print(result_goes_xrs)

print("Results for Solar_Orbiter_STIX:")
print(result_stix)

print("Results for SDO_AIA:")
print(result_aia)

print("Results for STEREO_A_EUVI:")
print(result_euvi)

print("Results for SOHO_LASCO:")
print(result_lasco)

print("Results for STEREO_A_SECCHI:")
print(result_secchi)

print("Results for Solar_Orbiter_MAG:")
print(result_mag)

print("Results for Solar_Orbiter_SWA:")
print(result_swa)

print("Results for ACE_Wind:")
print(result_wind)

