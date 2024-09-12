# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# Context: We are interested in observing standing slow magnetoacoustic waves in coronal loops.
# Instruments: SOHO/SUMER, Yohkoh/BCS, Hinode/EIS, SDO/AIA
# Physical Observable: Doppler shift for SOHO/SUMER, Yohkoh/BCS, Hinode/EIS; Imaging data for SDO/AIA
# Time Range: Not explicitly provided in the context, so we will use the full available time range for each instrument.

# Query for SOHO/SUMER
print("Querying SOHO/SUMER data...")
sumer_query = Fido.search(
    a.Time('1996-01-22', '2017-04-04'),  # Full available time range for SOHO/SUMER
    a.Instrument('SUMER'),
    a.Physobs('intensity')
)
print(sumer_query)
# Uncomment the following line to fetch the data
# sumer_files = Fido.fetch(sumer_query)
# Note: The result set is large and may be paginated.

# Query for Yohkoh/BCS
print("Querying Yohkoh/BCS data...")
bcs_query = Fido.search(
    a.Time('1991-09-01', '2001-12-14'),  # Full available time range for Yohkoh/BCS
    a.Instrument('BCS'),
    a.Physobs('intensity')
)
print(bcs_query)
# Uncomment the following line to fetch the data
# bcs_files = Fido.fetch(bcs_query)
# Note: The result set is large and may be paginated.

# Query for Hinode/EIS
print("Querying Hinode/EIS data...")
eis_query = Fido.search(
    a.Time('2006-10-21', '2023-10-01'),  # Full available time range for Hinode/EIS, replaced 'present' with a valid date
    a.Instrument('EIS'),
    a.Physobs('intensity')
)
print(eis_query)
# Uncomment the following line to fetch the data
# eis_files = Fido.fetch(eis_query)
# Note: The result set is large and may be paginated.

# Query for SDO/AIA
print("Querying SDO/AIA data...")
# Using a smaller example time range due to potential issue with broad time range
aia_query = Fido.search(
    a.Time('2010-05-12', '2010-05-19'),  # Example time range within the full available time range for SDO/AIA
    # Full available time range: a.Time('2010-05-12', '2023-10-01')
    a.Instrument('AIA'),
    a.Physobs('intensity')
)
print(aia_query)
# Uncomment the following line to fetch the data
# aia_files = Fido.fetch(aia_query)
# Note: The result set is large and may be paginated.
