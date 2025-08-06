# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script searches the Virtual Solar Observatory (VSO) for CDS/SOHO data
covering the quiet Sun transition region observations between 1996-03-01
and 1998-06-30, focusing on the NIS1 and NIS2 wavelength bands.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the CDS observations
time_start = "1996-03-01 00:00"
time_end = "1998-06-30 23:59"
time_attr = a.Time(time_start, time_end)

# Define the instrument and source
source_attr = a.Source('SOHO')
instr_attr = a.Instrument('CDS')

# Define the two CDS/NIS wavelength bands used in the study
# NIS1 band: Magnesium lines (308 – 379 Å)
nis1_wave = a.Wavelength(308 * u.Angstrom, 379 * u.Angstrom)

# NIS2 band: Neon and Oxygen lines (513 – 633 Å)
nis2_wave = a.Wavelength(513 * u.Angstrom, 633 * u.Angstrom)

# Perform the first search for the NIS1 band
search_nis1 = Fido.search(
    source_attr,
    instr_attr,
    time_attr,
    nis1_wave
)
print("Search results for NIS1 band (308-379 Å):")
print(search_nis1)

# Uncomment the following line to download the NIS1 data
# files_nis1 = Fido.fetch(search_nis1)

# Perform the second search for the NIS2 band
search_nis2 = Fido.search(
    source_attr,
    instr_attr,
    time_attr,
    nis2_wave
)
print("\nSearch results for NIS2 band (513-633 Å):")
print(search_nis2)

# Uncomment the following line to download the NIS2 data
# files_nis2 = Fido.fetch(search_nis2)

if __name__ == "__main__":
    # This script is not downloading data by default.
    # The printout above shows available records.
    pass
