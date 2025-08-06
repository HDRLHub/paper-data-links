# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.attrs as a
from sunpy.net import Fido
from astropy import units as u

# ------------------------------------------------------------------
# 1. SOHO/MDI: Carrington Rotation 1965 synoptic map (2000-07-10 to 2000-08-06)
# ------------------------------------------------------------------
search_cr = Fido.search(
    a.Time('2000-07-10', '2000-08-06'),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field')
)
print("MDI Carrington map search result:")
print(search_cr)
# To download these files, uncomment the line below:
# Fido.fetch(search_cr)

# ------------------------------------------------------------------
# 2. SOHO/MDI: Full-disk LOS magnetogram at 2000-07-14 09:35 UT
# ------------------------------------------------------------------
search_magnetogram = Fido.search(
    a.Time('2000-07-14T09:35', '2000-07-14T09:35'),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field')
)
print("\nMDI full-disk LOS magnetogram search result:")
print(search_magnetogram)
# To download this magnetogram, uncomment the line below:
# Fido.fetch(search_magnetogram)

# ------------------------------------------------------------------
# 3. SOHO/EIT: EUV image at 195 Å at 2000-07-14 09:36 UT
# ------------------------------------------------------------------
search_eit = Fido.search(
    a.Time('2000-07-14T09:36', '2000-07-14T09:36'),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(195 * u.Angstrom)
)
print("\nEIT 195 Å image search result:")
print(search_eit)
# To download the EIT data, uncomment the line below:
# Fido.fetch(search_eit)

# ------------------------------------------------------------------
# 4. SOHO/LASCO C2: White-light coronagraph images from 10:10 to 13:00 UT on 2000-07-14
# ------------------------------------------------------------------
search_lasco_c2 = Fido.search(
    a.Time('2000-07-14T10:10', '2000-07-14T13:00'),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("\nLASCO C2 white-light coronagraph search result:")
print(search_lasco_c2)
# To download LASCO C2 data, uncomment the line below:
# Fido.fetch(search_lasco_c2)

# ------------------------------------------------------------------
# 5. Yohkoh/SXT: Soft X-ray image near pre-flare time 09:30–09:40 UT on 2000-07-14
# ------------------------------------------------------------------
search_sxt = Fido.search(
    a.Time('2000-07-14T09:30', '2000-07-14T09:40'),
    a.Source('YOHKOH'),
    a.Instrument('SXT')
)
print("\nYohkoh/SXT soft X-ray image search result:")
print(search_sxt)
# To download the SXT data, uncomment the line below:
# Fido.fetch(search_sxt)

# ------------------------------------------------------------------
# 6. TRACE: EUV imaging of the flare arcade and filament eruption from 10:00 to 11:00 UT on 2000-07-14
# ------------------------------------------------------------------
search_trace = Fido.search(
    a.Time('2000-07-14T10:00', '2000-07-14T11:00'),
    a.Source('TRACE'),
    a.Instrument('TRACE'),
    a.Wavelength(171 * u.Angstrom)
)
print("\nTRACE 171 Å image sequence search result:")
print(search_trace)
# To download TRACE data, uncomment the line below:
# Fido.fetch(search_trace)

# ------------------------------------------------------------------
# Note: ACE and WIND in situ datasets are not available via the VSO interface.
# These must be retrieved from their respective data archives.
# ------------------------------------------------------------------
