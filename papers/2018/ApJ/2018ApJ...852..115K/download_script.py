# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Query Script for SOHO/SUMER Full‐Disk Lyman-α Profiles
Based on observations between May 1996 and April 2009.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# -----------------------------------------------------------------------------
# 1. Define the time interval for the SUMER observations
#    These dates bracket the 43 full-disk Lyman-α profiles analyzed in Lemaire et al. (2015).
start_time = "1996-05-01"
end_time   = "2009-04-30"
time_range = a.Time(start_time, end_time)

# -----------------------------------------------------------------------------
# 2. Specify the data source and instrument
#    We want SUMER data from the SOHO spacecraft.
source     = a.Source('SOHO')
instrument = a.Instrument('SUMER')

# -----------------------------------------------------------------------------
# 3. (Optional) Constrain the wavelength range around the Lyman-α line
#    Central λ = 121.567 nm ± 0.15 nm → 121.417 nm to 121.717 nm
#    Convert to Angstrom, since VSO expects wavelengths in u.Angstrom.
wvl_min = 121.417 * u.nm.to(u.Angstrom)  # 1214.17 Å
wvl_max = 121.717 * u.nm.to(u.Angstrom)  # 1217.17 Å
wavelength_range = a.Wavelength(wvl_min * u.Angstrom, wvl_max * u.Angstrom)

# -----------------------------------------------------------------------------
# 4. Build and execute the VSO query
#    We explicitly include Time, Source, Instrument, and Wavelength.
query = Fido.search(
    time_range,
    source,
    instrument,
    wavelength_range
)

# -----------------------------------------------------------------------------
# 5. Display the search results
print("VSO Query Results for SOHO/SUMER Lyman-α Profiles:")
print(query)

# -----------------------------------------------------------------------------
# 6. (Commented Out) Fetch the data if desired
# files = Fido.fetch(query)
# print("Downloaded files:")
# print(files)
# -----------------------------------------------------------------------------
