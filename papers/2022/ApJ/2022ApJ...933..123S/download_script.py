# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Query for SECCHI/Cor2 on STEREO A
# Note: COR2 is a detector of the SECCHI instrument
stereo_a_cor2_query = Fido.search(
    a.Time('2012-07-12 16:24', '2012-07-12 18:54'),
    a.Instrument('SECCHI'), a.Detector('COR2'), a.Source('stereo_a')
)
print("SECCHI/Cor2 on STEREO A Query Results:")
print(stereo_a_cor2_query)

# Query for SECCHI/Cor2 on STEREO B
# Note: COR2 is a detector of the SECCHI instrument
stereo_b_cor2_query = Fido.search(
    a.Time('2012-07-12 16:24', '2012-07-12 18:54'),
    a.Instrument('SECCHI'), a.Detector('COR2'), a.Source('stereo_b')
)
print("SECCHI/Cor2 on STEREO B Query Results:")
print(stereo_b_cor2_query)

# Query for LASCO/C2 on SOHO
# Warning: Large number of results may indicate pagination
soho_lasco_c2_query = Fido.search(
    a.Time('2012-07-12 16:24', '2012-07-12 17:18'),
    a.Instrument('c2'), a.Source('soho')
)
print("LASCO/C2 on SOHO Query Results:")
print(soho_lasco_c2_query)

# Query for LASCO/C3 on SOHO
# Warning: Large number of results may indicate pagination
soho_lasco_c3_query = Fido.search(
    a.Time('2012-07-12 16:24', '2012-07-12 17:18'),
    a.Instrument('c3'), a.Source('soho')
)
print("LASCO/C3 on SOHO Query Results:")
print(soho_lasco_c3_query)

# Query for AIA on SDO
sdo_aia_query = Fido.search(
    a.Time('2012-07-12 22:30', '2012-07-12 22:31'),
    a.Instrument('aia'),
    a.Wavelength(94 * u.Angstrom, 94 * u.Angstrom) |
    a.Wavelength(131 * u.Angstrom, 131 * u.Angstrom) |
    a.Wavelength(193 * u.Angstrom, 193 * u.Angstrom),
    a.Source('sdo')
)
print("AIA on SDO Query Results:")
print(sdo_aia_query)

# Query for HMI on SDO
# Note: Negative size in results may indicate an issue with the data
sdo_hmi_query = Fido.search(
    a.Time('2012-07-12 16:10', '2012-07-12 16:11'),
    a.Instrument('hmi'), a.Source('sdo')
)
print("HMI on SDO Query Results:")
print(sdo_hmi_query)

# Uncomment the following lines to fetch the data
# stereo_a_cor2_download = Fido.fetch(stereo_a_cor2_query)
# stereo_b_cor2_download = Fido.fetch(stereo_b_cor2_query)
# soho_lasco_c2_download = Fido.fetch(soho_lasco_c2_query)
# soho_lasco_c3_download = Fido.fetch(soho_lasco_c3_query)
# sdo_aia_download = Fido.fetch(sdo_aia_query)
# sdo_hmi_download = Fido.fetch(sdo_hmi_query)
