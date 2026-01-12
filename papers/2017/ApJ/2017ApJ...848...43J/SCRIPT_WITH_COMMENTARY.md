# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the SUMER observation on SOHO
time_start = "1997-04-20 00:00"
time_end   = "1997-04-20 23:59"

# Construct a VSO query for SOHO/SUMER data on 1997-04-20
# We restrict the wavelength range to 117–140 nm (i.e. 1170–1400 Å)
sumer_query = Fido.search(
    a.Time(time_start, time_end),
    a.vso.Source("SOHO"),
    a.vso.Instrument("SUMER"),
    a.Wavelength(1170, 1400) * u.Angstrom
)

# Print out the query results
print(sumer_query)

# To download the data, uncomment the following line:
# sumer_files = Fido.fetch(sumer_query)
