# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# Query for SDO/AIA data
print("Querying SDO/AIA data...")
aia_query = Fido.search(
    a.Time('2021-10-28T15:00', '2021-10-28T15:50'),
    a.Instrument('AIA'),
    a.Wavelength(94 * u.Angstrom) | a.Wavelength(131 * u.Angstrom) | a.Wavelength(171 * u.Angstrom) | a.Wavelength(193 * u.Angstrom) | a.Wavelength(211 * u.Angstrom) | a.Wavelength(335 * u.Angstrom)
)
print(aia_query)
# Uncomment the following line to fetch the data
# aia_download = Fido.fetch(aia_query)

# Query for STEREO-A/EUVI data
print("Querying STEREO-A/EUVI data...")
euvi_query = Fido.search(
    a.Time('2021-10-28T15:00', '2021-10-28T15:46'),
    a.Instrument('EUVI'),
    a.Wavelength(195 * u.Angstrom),
    a.Source('STEREO_A')
)
print(euvi_query)
# Uncomment the following line to fetch the data
# euvi_download = Fido.fetch(euvi_query)

# Query for STEREO-A/COR1 data
print("Querying STEREO-A/COR1 data...")
cor1_query = Fido.search(
    a.Time('2021-10-28T15:31', '2021-10-28T15:46'),
    a.Instrument('COR1'),
    a.Source('STEREO_A')
)
print(cor1_query)
# Uncomment the following line to fetch the data
# cor1_download = Fido.fetch(cor1_query)

# Query for SOHO/LASCO C2 data
print("Querying SOHO/LASCO C2 data...")
lasco_c2_query = Fido.search(
    a.Time('2021-10-28T15:48', '2021-10-28T16:24'),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Source('SOHO')
)
print(lasco_c2_query)
# Uncomment the following line to fetch the data
# lasco_c2_download = Fido.fetch(lasco_c2_query)

# Query for SOHO/LASCO C3 data
print("Querying SOHO/LASCO C3 data...")
lasco_c3_query = Fido.search(
    a.Time('2021-10-28T16:06', '2021-10-28T23:59'),  # Assuming we want data from 16:06 UT onwards
    a.Instrument('LASCO'),
    a.Detector('C3'),
    a.Source('SOHO')
)
print(lasco_c3_query)
# Uncomment the following line to fetch the data
# lasco_c3_download = Fido.fetch(lasco_c3_query)
```
