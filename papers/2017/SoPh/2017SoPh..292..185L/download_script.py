# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Script to search and (optionally) fetch SDO/AIA 211 Å data
for the period 2010-06-12 to 2015-09-17 using SunPy's Fido.
"""

# Import necessary modules
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the time range for the AIA data of interest
start_time = "2010-06-12 00:00:00"
end_time   = "2015-09-17 23:59:59"

# Define the AIA passband wavelength we require (211 Å)
wavelength = 211 * u.Angstrom

# Construct the VSO search query
search_results = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Wavelength(wavelength)
)

# Print out the search results
print("Search Results for SDO/AIA 211 Å data from {} to {}:".format(start_time, end_time))
print(search_results)

# The following line would download the files matching the search query.
# It is commented out to prevent accidental execution.
# downloaded_files = Fido.fetch(search_results)

# If you wish to fetch the data, uncomment the line above.
