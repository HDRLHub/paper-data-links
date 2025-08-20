# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the common time range for all queries: from pre-event to event time on 2000-08-02
time_range = a.Time('2000-08-02T16:04', '2000-08-02T19:30')

# -----------------------------------------------------------------------------
# Query 1: UVCS Lyman-alpha line (1215.67 Å) observations
# -----------------------------------------------------------------------------
# Instrument: UVCS (on SOHO)
# Wavelength: H I Lyman-alpha at 1215.67 Å
query_uvcs_lya = Fido.search(
    time_range,
    a.Instrument('UVCS'),
    a.Wavelength(1215.67 * u.Angstrom)
)
print("UVCS Lyman-alpha query results:")
print(query_uvcs_lya)
# To download the data, uncomment the line below:
# Fido.fetch(query_uvcs_lya)

# -----------------------------------------------------------------------------
# Query 2: UVCS Lyman-beta line (1025.72 Å) observations
# -----------------------------------------------------------------------------
# Instrument: UVCS (on SOHO)
# Wavelength: H I Lyman-beta at 1025.72 Å
query_uvcs_lyb = Fido.search(
    time_range,
    a.Instrument('UVCS'),
    a.Wavelength(1025.72 * u.Angstrom)
)
print("\nUVCS Lyman-beta query results:")
print(query_uvcs_lyb)
# To download the data, uncomment the line below:
# Fido.fetch(query_uvcs_lyb)

# -----------------------------------------------------------------------------
# Query 3: LASCO-C2 visible-light observations
# -----------------------------------------------------------------------------
# Instrument: LASCO with Detector C2 (on SOHO)
# Observable: total and excess-brightness white-light images
query_lasco_c2 = Fido.search(
    time_range,
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("\nLASCO-C2 white-light query results:")
print(query_lasco_c2)
# To download the data, uncomment the line below:
# Fido.fetch(query_lasco_c2)
