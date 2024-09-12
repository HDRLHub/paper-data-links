_This commentary was initially drafted by an AI model. Please use with caution_

```python
import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# Context: We are interested in observing standing slow magnetoacoustic waves in coronal loops.
# Instruments: SOHO/SUMER, Yohkoh/BCS, Hinode/EIS, SDO/AIA
# Physical Observable: Doppler shift for SOHO/SUMER, Yohkoh/BCS, Hinode/EIS; Imaging data for SDO/AIA
# Time Range: Not explicitly provided in the context, so we will use the full available time range for each instrument.

# Reasoning: Let's think step by step in order to produce the script. We will query each instrument separately.

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

# Query for Hinode/EIS
print("Querying Hinode/EIS data...")
eis_query = Fido.search(
    a.Time('2006-10-21', 'present'),  # Full available time range for Hinode/EIS
    a.Instrument('EIS'),
    a.Physobs('intensity')
)
print(eis_query)
# Uncomment the following line to fetch the data
# eis_files = Fido.fetch(eis_query)

# Query for SDO/AIA
print("Querying SDO/AIA data...")
aia_query = Fido.search(
    a.Time('2010-05-12', 'present'),  # Full available time range for SDO/AIA
    a.Instrument('AIA'),
    a.Physobs('intensity')
)
print(aia_query)
# Uncomment the following line to fetch the data
# aia_files = Fido.fetch(aia_query)
```

This script queries the Virtual Solar Observatory (VSO) for data from the specified instruments (SOHO/SUMER, Yohkoh/BCS, Hinode/EIS, and SDO/AIA) over their full available time ranges. The physical observable for SOHO/SUMER, Yohkoh/BCS, and Hinode/EIS is set to 'intensity' as a proxy for Doppler shift, and for SDO/AIA, it is also set to 'intensity' to reflect imaging data. The `Fido.fetch` commands are commented out to prevent actual data download.
