# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the SUMER instrument on SOHO
source = a.Source('SOHO')
instrument = a.Instrument('SUMER')

# Define the specific wavelengths (in Angstrom) for the high-temperature lines
wavelengths = [943.59 * u.Angstrom,   # Ca XIV
               974.86 * u.Angstrom,   # Fe XVIII
               1118.06 * u.Angstrom,  # Fe XIX
               1153.1653 * u.Angstrom]  # Fe XVII

################################################################################
# Inner Slit Position Queries (Slit Position 1, off-limb AR core observation)
################################################################################

# Segment 1: 2012-04-27T16:00:53 – 2012-04-27T18:47:11
time_inner_1 = a.Time('2012-04-27T16:00:53', '2012-04-27T18:47:11')
print("Querying SUMER Inner Slit Position 1, Segment 1")
result_inner_1 = Fido.search(time_inner_1, source, instrument, a.Wavelength(wavelengths))
print(result_inner_1)
# Uncomment to download: 
# files_inner_1 = Fido.fetch(result_inner_1)

# Segment 2: 2012-04-27T18:51:49 – 2012-04-27T21:38:05
time_inner_2 = a.Time('2012-04-27T18:51:49', '2012-04-27T21:38:05')
print("Querying SUMER Inner Slit Position 1, Segment 2")
result_inner_2 = Fido.search(time_inner_2, source, instrument, a.Wavelength(wavelengths))
print(result_inner_2)
# files_inner_2 = Fido.fetch(result_inner_2)

# Segment 3: 2012-04-27T21:42:39 – 2012-04-28T00:28:58
time_inner_3 = a.Time('2012-04-27T21:42:39', '2012-04-28T00:28:58')
print("Querying SUMER Inner Slit Position 1, Segment 3")
result_inner_3 = Fido.search(time_inner_3, source, instrument, a.Wavelength(wavelengths))
print(result_inner_3)
# files_inner_3 = Fido.fetch(result_inner_3)

################################################################################
# Outer Slit Position Queries (Slit Position 2, further off-limb observation)
################################################################################

# Segment 1: 2012-04-28T00:34:40 – 2012-04-28T03:29:55
time_outer_1 = a.Time('2012-04-28T00:34:40', '2012-04-28T03:29:55')
print("Querying SUMER Outer Slit Position 2, Segment 1")
result_outer_1 = Fido.search(time_outer_1, source, instrument, a.Wavelength(wavelengths))
print(result_outer_1)
# files_outer_1 = Fido.fetch(result_outer_1)

# Segment 2: 2012-04-28T03:34:57 – 2012-04-28T06:30:12
time_outer_2 = a.Time('2012-04-28T03:34:57', '2012-04-28T06:30:12')
print("Querying SUMER Outer Slit Position 2, Segment 2")
result_outer_2 = Fido.search(time_outer_2, source, instrument, a.Wavelength(wavelengths))
print(result_outer_2)
# files_outer_2 = Fido.fetch(result_outer_2)

# Segment 3: 2012-04-28T06:35:07 – 2012-04-28T09:30:23
time_outer_3 = a.Time('2012-04-28T06:35:07', '2012-04-28T09:30:23')
print("Querying SUMER Outer Slit Position 2, Segment 3")
result_outer_3 = Fido.search(time_outer_3, source, instrument, a.Wavelength(wavelengths))
print(result_outer_3)
# files_outer_3 = Fido.fetch(result_outer_3)

# Note:
# The Hinode/EIS instrument is not listed in the provided VSO interface,
# so no VSO queries for EIS data can be performed here.
# EIS data must be obtained through other means or interfaces.

print("All SUMER queries completed.")
