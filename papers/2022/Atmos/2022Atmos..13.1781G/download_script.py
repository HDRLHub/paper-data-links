# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Context: We want to construct queries to download data for the following instruments:
# 1. LASCO on SOHO for CME observations
# 2. EIT on SOHO for early CME development
# 3. Nobeyama Radioheliograph (NoRH) for filament eruptions and CME core observations
# 4. SDO/AIA for active region eruptions and flare observations
# 5. Wind/WAVES for radio bursts during solar eruptions
# 6. Parker Solar Probe and Solar Orbiter for ongoing observations

# 1. LASCO on SOHO for CME observations
print("Querying LASCO on SOHO for CME observations...")
lasco_query = Fido.search(
    a.Time('1996-01-01', '2021-11-30'),
    a.Instrument('LASCO'),
    a.Physobs('intensity')
)
print(lasco_query)
# Note: The query returns 10000 rows, indicating potential pagination issues.
# Uncomment the following line to fetch the data
# lasco_files = Fido.fetch(lasco_query)

# 2. EIT on SOHO for early CME development
print("Querying EIT on SOHO for early CME development...")
eit_query = Fido.search(
    a.Time('1996-01-01', '1998-06-30'),
    a.Instrument('EIT'),
    a.Physobs('intensity')
)
print(eit_query)
# Note: The query returns 10000 rows, indicating potential pagination issues.
# Uncomment the following line to fetch the data
# eit_files = Fido.fetch(eit_query)

# 3. Nobeyama Radioheliograph (NoRH) for filament eruptions and CME core observations
print("Querying Nobeyama Radioheliograph (NoRH) for filament eruptions and CME core observations...")
norh_query = Fido.search(
    a.Time('1997-10-06', '1997-10-06'),
    a.Instrument('NoRH'),
    a.Wavelength(17 * u.GHz)
)
print(norh_query)
# Uncomment the following line to fetch the data
# norh_files = Fido.fetch(norh_query)

# 4. SDO/AIA for active region eruptions and flare observations
print("Querying SDO/AIA for active region eruptions and flare observations...")
aia_query = Fido.search(
    a.Time('2011-08-04', '2011-08-05'),  # Using smaller example time range
    a.Instrument('AIA'),
    a.Wavelength(193 * u.Angstrom)
)
print(aia_query)
# Uncomment the following line to fetch the data
# aia_files = Fido.fetch(aia_query)

# 5. Wind/WAVES for radio bursts during solar eruptions
print("Querying Wind/WAVES for radio bursts during solar eruptions...")
waves_query = Fido.search(
    a.Time('2005-01-01', '2005-01-31'),  # Using broader example time range
    a.Instrument('WAVES'),
    a.Wavelength(0.01 * u.MHz, 14 * u.MHz)
)
print(waves_query)
# Uncomment the following line to fetch the data
# waves_files = Fido.fetch(waves_query)

# 6. Parker Solar Probe and Solar Orbiter for ongoing observations
print("Querying Parker Solar Probe and Solar Orbiter for ongoing observations...")
psp_query = Fido.search(
    a.Time('2018-10-31', '2018-11-01'),  # Using smaller example time range
    a.Instrument('WISPR')
)
print(psp_query)
# Uncomment the following line to fetch the data
# psp_files = Fido.fetch(psp_query)

so_query = Fido.search(
    a.Time('2020-05-12', '2020-05-13'),  # Using smaller example time range
    a.Instrument('EUI')
)
print(so_query)
# Uncomment the following line to fetch the data
# so_files = Fido.fetch(so_query)
