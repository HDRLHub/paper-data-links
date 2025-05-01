# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query SDO/AIA data using SunPy's VSO client.
The query is based on the January 27, 2012 solar eruption event as described in the paper,
where SDO/AIA was used for EUV wave tracking in the lower corona at 211 Å.
Note:
 - We use the SDO/AIA instrument record that is valid for the January 27 event (available from 2010/05/12).
 - The query time range is chosen to cover the period around the EUV wave observation (roughly 18:00 UT to 18:40 UT on 2012-01-27).
 - The wavelength is set to 211 Å (from the available wavelengths in the VSO interface).
 - We only print the query results. The Fido.fetch command is shown but commented out.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range corresponding to the EUV wave tracking period on January 27, 2012.
start_time = "2012-01-27T18:00:00"
end_time   = "2012-01-27T18:40:00"

# Define the wavelength for which we want to query (211 Å as mentioned in the study).
wavelength = 211 * u.Angstrom

# Build the query using SunPy's VSO client.
# We specify:
#   - Time range: 2012-01-27T18:00:00 to 2012-01-27T18:40:00
#   - Source: SDO
#   - Instrument: AIA
#   - Wavelength: 211 Å
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Wavelength(wavelength, wavelength)
)

# Print the query result details.
print("VSO Query Result for SDO/AIA (211 Å) on 2012-01-27:")
print(query_result)

# Uncomment the following line to fetch the data:
# downloaded_files = Fido.fetch(query_result)

if __name__ == "__main__":
    pass
