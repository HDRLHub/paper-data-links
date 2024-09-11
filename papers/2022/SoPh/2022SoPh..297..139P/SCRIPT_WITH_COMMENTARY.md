# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Wind/WAVES: DH type II radio bursts from 1994 to present
print("Querying Wind/WAVES data...")
wind_waves_query = Fido.search(
    a.Time('1994-01-01', '2023-12-31'),
    a.Instrument('WAVES'),
    a.Wavelength(14 * u.MHz, 20 * u.kHz)
)
print(wind_waves_query)
# wind_waves_data = Fido.fetch(wind_waves_query)

# STEREO/SWAVES: DH type II radio bursts from 2006 to present
print("Querying STEREO/SWAVES data...")
stereo_swaves_query = Fido.search(
    a.Time('2006-01-01', '2023-12-31'),
    a.Instrument('SWAVES'),
    a.Wavelength(10 * u.Angstrom, 16075 * u.kHz)
)
print(stereo_swaves_query)
# stereo_swaves_data = Fido.fetch(stereo_swaves_query)

# SOHO/LASCO: CME observations from 1996 to present
print("Querying SOHO/LASCO data...")
soho_lasco_query = Fido.search(
    a.Time('1996-01-01', '2023-12-31'),
    a.Instrument('LASCO'),
    a.Wavelength(5294 * u.Angstrom, 6576 * u.Angstrom)
)
print(soho_lasco_query)
# soho_lasco_data = Fido.fetch(soho_lasco_query)

# In-situ Probes: ICME parameters from May 1996 to December 2019
# Note: In-situ probes data is not directly available in VSO, so this part is illustrative.
print("Querying In-situ Probes data (illustrative)...")
in_situ_query = Fido.search(
    a.Time('1996-05-01', '2019-12-31'),
    a.Instrument('In-situ')
)
print(in_situ_query)
# in_situ_data = Fido.fetch(in_situ_query)

print("Queries completed. Uncomment the fetch commands to download the data.")
```
