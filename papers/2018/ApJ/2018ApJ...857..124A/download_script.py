# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
SunPy VSO Query Script for 2015 June 22 C1.1-class Flare Event
Data sources: SDO/AIA, SDO/HMI, RHESSI, IRIS, SOHO/LASCO C2
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ---------------------------------------------------------------------
# 1. SDO/AIA EUV imaging for flare precursor and main phase
#    Time: 2015-06-22 16:18 UT to 2015-06-22 16:45 UT
#    Passbands: 94, 131, 171, 193, 211, 335 Å
# ---------------------------------------------------------------------
time_aia = a.Time('2015-06-22 16:18', '2015-06-22 16:45')
instrument_aia = a.Instrument('AIA')
physobs_intensity = a.Physobs('intensity')
wavelengths_aia = a.Wavelength([94, 131, 171, 193, 211, 335] * u.angstrom)

query_aia = Fido.search(time_aia, instrument_aia, physobs_intensity, wavelengths_aia)
print("AIA Query Results:")
print(query_aia)
# Fido.fetch(query_aia)  # Uncomment to download AIA data

# ---------------------------------------------------------------------
# 2. SDO/HMI vector magnetograms for NLFFF extrapolation
#    Times: 2015-06-22 16:34:25 UT (pre-flare) and 17:22:25 UT (post-flare)
#    Observable: vector magnetic field (hmi.sharp_cea series)
# ---------------------------------------------------------------------
instrument_hmi = a.Instrument('HMI')
physobs_vector = a.Physobs('vector_magnetic_field')

# Pre-flare
time_hmi_pre = a.Time('2015-06-22 16:34:25', '2015-06-22 16:34:25')
query_hmi_pre = Fido.search(time_hmi_pre, instrument_hmi, physobs_vector)
print("\nHMI Vector Pre-flare Query Results:")
print(query_hmi_pre)
# Fido.fetch(query_hmi_pre)  # Uncomment to download pre-flare HMI data

# Post-flare
time_hmi_post = a.Time('2015-06-22 17:22:25', '2015-06-22 17:22:25')
query_hmi_post = Fido.search(time_hmi_post, instrument_hmi, physobs_vector)
print("\nHMI Vector Post-flare Query Results:")
print(query_hmi_post)
# Fido.fetch(query_hmi_post)  # Uncomment to download post-flare HMI data

# ---------------------------------------------------------------------
# 3. RHESSI hard X-ray imaging and spectroscopy
#    Time: 2015-06-22 16:29 UT to 16:52 UT
#    Energy bands: 6–12 keV and 12–25 keV
# ---------------------------------------------------------------------
instrument_rhessi = a.Instrument('RHESSI')
time_rhessi = a.Time('2015-06-22 16:29', '2015-06-22 16:52')

# 6–12 keV band
energy_low = a.Wavelength(6 * u.keV, 12 * u.keV)
query_rhessi_low = Fido.search(time_rhessi, instrument_rhessi, energy_low)
print("\nRHESSI 6-12 keV Query Results:")
print(query_rhessi_low)

# 12–25 keV band
energy_high = a.Wavelength(12 * u.keV, 25 * u.keV)
query_rhessi_high = Fido.search(time_rhessi, instrument_rhessi, energy_high)
print("\nRHESSI 12-25 keV Query Results:")
print(query_rhessi_high)
# Fido.fetch(query_rhessi_low, query_rhessi_high)  # Uncomment to download RHESSI data

# ---------------------------------------------------------------------
# 4. IRIS slit-jaw images at 1400 Å for transition-region response
#    Time: 2015-06-22 16:29 UT to 16:31 UT
#    Detector: SJI, Wavelength: 1400 Å
# ---------------------------------------------------------------------
instrument_iris = a.Instrument('IRIS')
detector_sji = a.Detector('SJI')
wavelength_iris = a.Wavelength(1400 * u.angstrom)
time_iris = a.Time('2015-06-22 16:29', '2015-06-22 16:31')

query_iris = Fido.search(time_iris, instrument_iris, detector_sji, physobs_intensity, wavelength_iris)
print("\nIRIS 1400 Å SJI Query Results:")
print(query_iris)
# Fido.fetch(query_iris)  # Uncomment to download IRIS data

# ---------------------------------------------------------------------
# 5. SOHO/LASCO C2 white-light coronagraph for CME observation
#    Time: 2015-06-22 17:45 UT to 18:45 UT (approx. 1 hr after flare peak)
#    Detector: C2
# ---------------------------------------------------------------------
instrument_lasco = a.Instrument('LASCO')
detector_c2 = a.Detector('C2')
time_lasco = a.Time('2015-06-22 17:45', '2015-06-22 18:45')

query_lasco_c2 = Fido.search(time_lasco, instrument_lasco, physobs_intensity, detector_c2)
print("\nLASCO C2 Query Results:")
print(query_lasco_c2)
# Fido.fetch(query_lasco_c2)  # Uncomment to download LASCO C2 data

# ---------------------------------------------------------------------
# Note: Hinode/SOT is not available via the provided VSO interface.
# ---------------------------------------------------------------------
