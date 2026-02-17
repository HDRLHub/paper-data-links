# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
#!/usr/bin/env python3
"""
SunPy VSO Query Script for Helioseismic and Irradiance Data

This script searches and prints out available data for:
  1. SoHO/MDI f‐mode frequency observations (Ni I 6768 Å proxy)
  2. SDO/HMI f‐mode frequency observations (Fe I 6173 Å)
  3. SoHO/VIRGO Total Solar Irradiance (TSI) measurements

Time ranges are defined based on the study periods:
  - MDI: 1996-05-01 to 2011-04-24
  - HMI: 2010-04-30 to 2017-06-03
  - VIRGO: 1996-05-01 to 2017-06-03
"""

from sunpy.net import Fido
from sunpy.net.attrs import Time, Instrument, Source

# -----------------------------------------------------------------------------
# 1. SoHO / MDI Data (Medium-ℓ f-mode frequency sets)
# -----------------------------------------------------------------------------
mdi_start = '1996-05-01'
mdi_end   = '2011-04-24'

mdi_search = Fido.search(
    Time(mdi_start, mdi_end),
    Source('SOHO'),
    Instrument('MDI')
)

# Print out the MDI search results
print("SoHO/MDI Search Results:")
print(mdi_search)

# To download the files, uncomment the following line:
# Fido.fetch(mdi_search)

# -----------------------------------------------------------------------------
# 2. SDO / HMI Data (f-mode frequency sets)
# -----------------------------------------------------------------------------
hmi_start = '2010-04-30'
hmi_end   = '2017-06-03'

hmi_search = Fido.search(
    Time(hmi_start, hmi_end),
    Source('SDO'),
    Instrument('HMI')
)

# Print out the HMI search results
print("\nSDO/HMI Search Results:")
print(hmi_search)

# To download the files, uncomment the following line:
# Fido.fetch(hmi_search)

# -----------------------------------------------------------------------------
# 3. SoHO / VIRGO Data (Total Solar Irradiance)
# -----------------------------------------------------------------------------
virgo_start = '1996-05-01'
virgo_end   = '2017-06-03'

virgo_search = Fido.search(
    Time(virgo_start, virgo_end),
    Source('SOHO'),
    Instrument('VIRGO')
)

# Print out the VIRGO search results
print("\nSoHO/VIRGO Search Results:")
print(virgo_search)

# To download the files, uncomment the following line:
# Fido.fetch(virgo_search)
```
