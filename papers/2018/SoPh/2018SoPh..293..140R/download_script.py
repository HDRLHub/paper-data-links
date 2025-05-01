# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for complementary solar image data
from the SOHO/EIT instrument. According to the provided VSO interface, the EIT instrument
acquires full-disk solar images at 171 Å, 195 Å, 284 Å, and 304 Å.

In the scientific context, the EIT data complement Mg xii spectroheliograph observations
of hot plasma by characterizing the cooler plasma components through EUV emission. Although
the main focus of the paper is on hot plasma data from the Mg xii instrument (which is not
available in the VSO interface), we use SOHO/EIT data for the period of 18 February 2002
to 28 February 2002. In this time range, EIT data provide EUV images in the available wavelengths.
"""

# Import required modules from sunpy.net and astropy.units
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the observation time range as specified for the main study period.
start_time = "2002-02-18"
end_time = "2002-02-28"

# Define the wavelengths available for SOHO/EIT from the VSO interface.
# The available wavelengths are: 171 Å, 195 Å, 284 Å, and 304 Å.
wavelength_171 = a.Wavelength(171 * u.angstrom)
wavelength_195 = a.Wavelength(195 * u.angstrom)
wavelength_284 = a.Wavelength(284 * u.angstrom)
wavelength_304 = a.Wavelength(304 * u.angstrom)

# Construct the query using Fido by specifying the time range, source, instrument,
# and the wavelengths of interest. Each wavelength is queried using a logical OR operator.
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("EIT"),
    wavelength_171 | wavelength_195 | wavelength_284 | wavelength_304
)

# Print out the query results to review the available data records.
print("Query Results for SOHO/EIT data from {} to {}:".format(start_time, end_time))
print(query_result)

# If you wish to download the data after verifying the query results, you can uncomment the following line.
# Note: Downloading data may take some time depending on data volume and network speed.
# files_downloaded = Fido.fetch(query_result)
