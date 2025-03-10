# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query SDO AIA data for synthesizing CME observations.
We focus on the Atmospheric Imaging Assembly (AIA) onboard SDO during the interval
23 May 2010 to 17 April 2012. According to the scientific context, we are interested in three
EUV passbands: 171 Å (Fe ix), 193 Å (Fe xii/Fe xxiv, queried here as 191-195 Å which includes 193 Å),
and 211 Å (Fe xiv).

Note: The VSO interface confirms that SDO AIA data are available with a wavelength range that
covers these channels. This script prints out the query results. 
To actually download the data, uncomment the Fido.fetch() commands.
"""

# Import necessary modules
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the query: 23 May 2010 to 17 April 2012.
time_range = a.Time("2010-05-23", "2012-04-17")

# Query for AIA 171 channel:
# The VSO interface indicates that the AIA wavelength band “171.0 - 175.0” can be used.
# We set a narrow wavelength range around 171 Å.
wave_171 = a.Wavelength(170*u.angstrom, 175*u.angstrom)
result_aia_171 = Fido.search(time_range, a.Instrument("AIA"), a.Source("SDO"), wave_171)

# Print out the query result for the AIA 171 channel.
print("SDO AIA 171 channel query results:")
print(result_aia_171)

# Query for AIA 193 channel:
# The available wavelength specification "191.0 - 195.0" in the VSO interface covers the 193 Å channel.
wave_193 = a.Wavelength(191*u.angstrom, 195*u.angstrom)
result_aia_193 = Fido.search(time_range, a.Instrument("AIA"), a.Source("SDO"), wave_193)

# Print out the query result for the AIA 193 channel.
print("\nSDO AIA 193 channel query results:")
print(result_aia_193)

# Query for AIA 211 channel:
# The channel is centered around 211 Å; we use a narrow range to isolate it.
wave_211 = a.Wavelength(210.5*u.angstrom, 211.5*u.angstrom)
result_aia_211 = Fido.search(time_range, a.Instrument("AIA"), a.Source("SDO"), wave_211)

# Print out the query result for the AIA 211 channel.
print("\nSDO AIA 211 channel query results:")
print(result_aia_211)

# Uncomment the lines below to fetch the data locally if desired.
# fetched_files_171 = Fido.fetch(result_aia_171)
# fetched_files_193 = Fido.fetch(result_aia_193)
# fetched_files_211 = Fido.fetch(result_aia_211)
