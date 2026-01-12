# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido
import sunpy.net.attrs as a

# ------------------------------------------------------------------------------
# Query 1: RHESSI X-ray Data for SOL2005-08-20T08:09 Flare
# Time range covers the precursor and main phases (including the night gap).
# Energy range selected: 6 keV to 25 keV, as emphasized in the study.
# ------------------------------------------------------------------------------
time_rhessi = a.Time('2005-08-20T06:00:00', '2005-08-20T08:27:00')
instrument_rhessi = a.Instrument('RHESSI')
energy_band = a.Wavelength(6 * u.keV, 25 * u.keV)

search_rhessi = Fido.search(time_rhessi, instrument_rhessi, energy_band)
print("RHESSI search results:")
print(search_rhessi)

# To download the RHESSI data, uncomment the following line:
# result_rhessi = Fido.fetch(search_rhessi)

# ------------------------------------------------------------------------------
# Query 2: SOHO/EIT 195 Å EUV Images
# Time range covers the precursor and main phases with 12-minute cadence.
# Wavelength fixed at 195 Angstrom.
# ------------------------------------------------------------------------------
time_eit = a.Time('2005-08-20T06:00:00', '2005-08-20T09:00:00')
instrument_eit = a.Instrument('EIT')
wavelength_eit = a.Wavelength(195 * u.Angstrom)

search_eit = Fido.search(time_eit, instrument_eit, wavelength_eit)
print("\nSOHO/EIT 195 Å search results:")
print(search_eit)

# To download the EIT data, uncomment the following line:
# result_eit = Fido.fetch(search_eit)

# ------------------------------------------------------------------------------
# Query 3: SOHO/MDI Line-of-Sight Magnetograms
# Time range spans 05:00–10:00 UT for high-cadence magnetogram analysis.
# Physical observable: LOS magnetic field.
# ------------------------------------------------------------------------------
time_mdi_mag = a.Time('2005-08-20T05:00:00', '2005-08-20T10:00:00')
instrument_mdi = a.Instrument('MDI')
physobs_mdi_mag = a.Physobs('LOS_magnetic_field')

search_mdi_mag = Fido.search(time_mdi_mag, instrument_mdi, physobs_mdi_mag)
print("\nSOHO/MDI LOS magnetic field search results:")
print(search_mdi_mag)

# To download the MDI magnetograms, uncomment the following line:
# result_mdi_mag = Fido.fetch(search_mdi_mag)

# ------------------------------------------------------------------------------
# Query 4: SOHO/MDI Continuum Image for Spatial Alignment
# Single time at 06:24:00 UT used for cross-checking coordinate alignment.
# Physical observable: intensity (continuum).
# ------------------------------------------------------------------------------
time_mdi_cont = a.Time('2005-08-20T06:24:00', '2005-08-20T06:24:00')
physobs_mdi_cont = a.Physobs('intensity')

search_mdi_cont = Fido.search(time_mdi_cont, instrument_mdi, physobs_mdi_cont)
print("\nSOHO/MDI continuum (intensity) search results:")
print(search_mdi_cont)

# To download the MDI continuum image, uncomment the following line:
# result_mdi_cont = Fido.fetch(search_mdi_cont)

# End of script
