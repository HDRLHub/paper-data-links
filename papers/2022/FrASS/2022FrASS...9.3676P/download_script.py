# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# Context: We need to download data for the study of a stealthy streamer-blowout coronal mass ejection (SBO-CME) observed by the Parker Solar Probe (PSP) at approximately 0.5 AU. The instruments involved are COR1 and COR2 on STEREO-A, C2 on SOHO, EUVI on STEREO-A, AIA and HMI on SDO, and FIELDS and SWEAP on PSP.

# Query for COR1 on STEREO-A
# Note: Large number of results, potential pagination issue
cor1_query = Fido.search(
    a.Time('2020-06-22 16:30', '2020-06-25'),
    a.Instrument('SECCHI'),  # Corrected Instrument
    a.Detector('COR1'),  # Corrected Detector
    a.Wavelength(6500 * u.Angstrom, 7500 * u.Angstrom)
)
print("COR1 Query Results:")
print(cor1_query)
# cor1_files = Fido.fetch(cor1_query)

# Query for COR2 on STEREO-A
# Note: Large number of results, potential pagination issue
cor2_query = Fido.search(
    a.Time('2020-06-22 16:30', '2020-06-25'),
    a.Instrument('SECCHI'),  # Corrected Instrument
    a.Detector('COR2'),  # Corrected Detector
    a.Wavelength(6500 * u.Angstrom, 7500 * u.Angstrom)
)
print("COR2 Query Results:")
print(cor2_query)
# cor2_files = Fido.fetch(cor2_query)

# Query for C2 on SOHO
# Adjusted time range to a smaller example range due to 0 results
c2_query = Fido.search(
    a.Time('2020-06-22 00:00', '2020-06-22 23:59'),  # Adjusted time range
    a.Instrument('LASCO'),  # Corrected Instrument
    a.Detector('C2'),  # Corrected Detector
    a.Wavelength(1.6 * u.Angstrom, 6 * u.Angstrom)
)
print("C2 Query Results:")
print(c2_query)
# c2_files = Fido.fetch(c2_query)

# Query for EUVI on STEREO-A
# Note: Large number of results, potential pagination issue
euvi_query = Fido.search(
    a.Time('2020-06-21', '2020-06-22'),
    a.Instrument('SECCHI'),  # Corrected Instrument
    a.Detector('EUVI'),  # Corrected Detector
    a.Wavelength(195 * u.Angstrom)
)
print("EUVI Query Results:")
print(euvi_query)
# euvi_files = Fido.fetch(euvi_query)

# Query for AIA on SDO
# Note: Large number of results, potential pagination issue
aia_query = Fido.search(
    a.Time('2020-06-21', '2020-06-22'),
    a.Instrument('AIA'),
    a.Wavelength(211 * u.Angstrom)
)
print("AIA Query Results:")
print(aia_query)
# aia_files = Fido.fetch(aia_query)

# Query for HMI on SDO
# Adjusted time range to a smaller example range due to 0 results
hmi_query = Fido.search(
    a.Time('2020-06-21 00:00', '2020-06-21 23:59'),  # Adjusted time range
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print("HMI Query Results:")
print(hmi_query)
# hmi_files = Fido.fetch(hmi_query)

# Note: FIELDS and SWEAP on PSP are in-situ instruments and their data might not be available through VSO. They are typically accessed through other data repositories specific to PSP.

# The above queries cover the required instruments and time ranges as specified in the context.
