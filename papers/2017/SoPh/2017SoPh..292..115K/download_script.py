# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query 1: SDO/AIA 171 Å data around the first neutron event at 03:52 UT on 2012-03-05
time1_start = "2012-03-05 03:52:00"
time1_end   = "2012-03-05 03:53:00"
instrument  = a.Instrument('AIA')
wavelength1 = a.Wavelength(171 * u.angstrom)

print(f"Querying SDO/AIA 171 Å data from {time1_start} to {time1_end}")
query1 = Fido.search(a.Time(time1_start, time1_end), instrument, wavelength1)
print(query1)
# files1 = Fido.fetch(query1)  # Uncomment to download data

# Query 2: SDO/AIA 171 Å data around the second neutron event at 04:38 UT on 2012-03-05
time2_start = "2012-03-05 04:38:00"
time2_end   = "2012-03-05 04:39:00"
wavelength2 = a.Wavelength(171 * u.angstrom)

print(f"\nQuerying SDO/AIA 171 Å data from {time2_start} to {time2_end}")
query2 = Fido.search(a.Time(time2_start, time2_end), instrument, wavelength2)
print(query2)
# files2 = Fido.fetch(query2)  # Uncomment to download data
