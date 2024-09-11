# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# Query for EIS onboard Hinode
# Note: EIS is not listed in the provided VSO interface, so we will skip this query.

# Query for EUNIS sounding rocket
# Time Range: 2006/04/12
# Wavelength: 300 to 370 Å
# Note: Adjusting the time range to a slightly broader example time range due to potential issues with too specific time ranges
eunis_query = Fido.search(
    a.Time('2006-04-12 18:00', '2006-04-12 19:00'),  # Using a slightly broader example time range
    a.Instrument('EUNIS'),
    a.Wavelength(300 * u.Angstrom, 370 * u.Angstrom)
)
print("EUNIS Query Results:")
print(eunis_query)
# eunis_files = Fido.fetch(eunis_query)

# Query for SUMER onboard SOHO
# Time Range: Not specified, so we will use the full available range
# Wavelength: 470 to 1609 Å
# Note: The query returns 10,000 results, indicating pagination might be in effect
sumer_query = Fido.search(
    a.Time('1996-01-22', '2017-04-04'),
    a.Instrument('SUMER'),
    a.Wavelength(470 * u.Angstrom, 1609 * u.Angstrom)
)
print("SUMER Query Results:")
print(sumer_query)
# sumer_files = Fido.fetch(sumer_query)
