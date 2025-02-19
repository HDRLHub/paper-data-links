# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses Sunpy's VSO interface to query data from the Michelson Doppler Imager (MDI)
on board SoHO for a study focused on the evolution of emerging magnetic flux regions.
The query gathers MDI data measuring the line-of-sight (LOS) magnetic field observable.
The observations are selected for the coordinated campaign on October 15, 2007,
from 08:00 UT to 11:00 UT, which falls within the available time range for MDI.
The spectral line observed is Ni I at ~6768 Å.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the coordinated campaign on October 15, 2007.
start_time = '2007-10-15 08:00:00'
end_time = '2007-10-15 11:00:00'

# Define the instrument and observable parameters:
# - Source: SOHO
# - Instrument: MDI
# - Physical Observable: LOS_magnetic_field  (i.e., magnetograms)
# - Wavelength: 6768 Å (approximates the Ni I 6767.8 Å line used in context)
query_time = a.Time(start_time, end_time)
query_instrument = a.Instrument("MDI")
query_source = a.Source("SOHO")
query_physobs = a.Physobs("LOS_magnetic_field")
query_wavelength = a.Wavelength(6768.0 * u.Angstrom)

# Perform the query using Fido.search
# This will search the Virtual Solar Observatory for the matching data.
result = Fido.search(query_time, query_instrument, query_source, query_physobs, query_wavelength)

# Print the query results to examine the available data records.
print("Query Results:")
print(result)

# To download the data, you can use the Fido.fetch command.
# It is currently commented out as per instructions.
# Uncomment the following lines to fetch the data.
# downloaded_files = Fido.fetch(result)
# print("Downloaded files:")
# print(downloaded_files)

if __name__ == '__main__':
    pass
