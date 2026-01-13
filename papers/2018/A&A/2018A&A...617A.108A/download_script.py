# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range covering the primary GOLF calibration period
time_range = a.Time('1996-04-11', '2018-04-10')

# ------------------------------------------------------------------
# Query 1: SOHO/GOLF data (Global Oscillations at Low Frequencies)
# ------------------------------------------------------------------
# We specify:
#   - Source: SOHO
#   - Instrument: GOLF
#   - Detector: Fsmain (primary photomultiplier)
#   - Physical observable: LOS_velocity
#   - Wavelength range: 5884 – 5902 Å (Sodium D‐line wing)
golf_query = Fido.search(
    time_range,
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain'),
    a.Physobs('LOS_velocity'),
    a.Wavelength(5884 * u.Angstrom, 5902 * u.Angstrom)
)

print("SOHO/GOLF Query Results:")
print(golf_query)

# To download the data, uncomment the following line:
# Fido.fetch(golf_query)

# ------------------------------------------------------------------
# Query 2: SOHO/VIRGO SPM data (Sun Photometer Monitor)
# ------------------------------------------------------------------
# We specify:
#   - Source: SOHO
#   - Instrument: VIRGO
#   - Detector: SPM
#   - Physical observable: intensity
# Note: No wavelength filter is applied here; all SPM channels will be returned.
virgo_spm_query = Fido.search(
    time_range,
    a.Source('SOHO'),
    a.Instrument('VIRGO'),
    a.Detector('SPM'),
    a.Physobs('intensity')
)

print("SOHO/VIRGO SPM Query Results:")
print(virgo_spm_query)

# To download the data, uncomment the following line:
# Fido.fetch(virgo_spm_query)
