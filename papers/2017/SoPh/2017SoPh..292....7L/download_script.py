# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
import astropy.units as u
from sunpy.net import Fido, attrs as a

# ----------------------------------------------------------------------
# Query 1: SOHO/EIT 195 Å data covering 1997–2013 (historical EIT-wave observations)
# ----------------------------------------------------------------------
time_eit_start = '1997-01-01'
time_eit_end   = '2013-12-31'
wavelength_eit = 195.0 * u.Angstrom

print(f"Querying SOHO/EIT data for EIT waves (195 Å) from {time_eit_start} to {time_eit_end}")
results_eit = Fido.search(
    a.Time(time_eit_start, time_eit_end),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(wavelength_eit)
)
print(results_eit)
# To download, uncomment the following line:
# downloaded_eit = Fido.fetch(results_eit)

# ----------------------------------------------------------------------
# Query 2: SDO/AIA 171, 193, 211 Å data for the 15 February 2011 EIT-wave event
# ----------------------------------------------------------------------
time_aia_start = '2011-02-15 00:00:00'
time_aia_end   = '2011-02-15 23:59:59'
wavelengths_aia = [171.0, 193.0, 211.0] * u.Angstrom

print(f"\nQuerying SDO/AIA data for 15 February 2011 EIT-wave event at wavelengths {wavelengths_aia}")
results_aia = Fido.search(
    a.Time(time_aia_start, time_aia_end),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(wavelengths_aia)
)
print(results_aia)
# To download, uncomment the following line:
# downloaded_aia = Fido.fetch(results_aia)

print("\nSearch complete. Review the above tables for available files and metadata.")
