# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import vso
import astropy.units as u

# Initialize the VSO client
client = vso.VSOClient()

# Define the time range for SUMER quiet-Sun atlas data
# Based on Curdt et al. (2001): data acquired primarily between 1996-01-22 and 1998-12-31
time_start = "1996-01-22"
time_end = "1998-12-31"

# Define the wavelength range used in the analysis (1205–1550 Å)
wave_start = 1205.0 * u.Angstrom
wave_end = 1550.0 * u.Angstrom

# Build the query for SOHO/SUMER data
sumer_query = client.search(
    vso.attrs.Time(time_start, time_end),
    vso.attrs.Source('SOHO'),
    vso.attrs.Instrument('SUMER'),
    vso.attrs.Wavelength(wave_start, wave_end)
)

# Print out the query results
print("SUMER quiet-Sun atlas search results:")
print(sumer_query)

# Uncomment the following line to download the data when ready
# client.fetch(sumer_query)
