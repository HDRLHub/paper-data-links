# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query for SDO/AIA EUV data.
The query is designed based on the instrumentation context provided in the paper,
which uses SDO/AIA 211 Å imagery to track the evolution of a coronal mass ejection (CME)
observed on 22 May 2013. The selected time range captures the period from approximately 12:46 UT to 12:50 UT,
when running-difference images at 211 Å were employed to correlate radio source positions with the evolving CME structure.

Note:
- SDO/AIA is available in the VSO interface.
- The wavelength query is set to 211 Å (which is provided in the available wavelengths list).
- Only the query is performed here. The actual data download (using Fido.fetch) is commented out.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the query.
# According to the context, SDO/AIA data were used from 12:46 UT to 12:50 UT on 22 May 2013.
time_range = a.Time("2013-05-22 12:46:00", "2013-05-22 12:50:00")

# Define the instrument attribute.
# We employ SDO/AIA, which is available via the VSO interface.
instrument = a.Instrument("AIA")

# Define the wavelength attribute.
# The context specifies the use of 211 Å images (EUV) used for tracking the CME evolution.
wavelength = a.Wave(211*u.AA, 211*u.AA)

# Construct the query using the defined attributes.
# The query will search for SDO/AIA data in the specified time range and wavelength.
query_result = Fido.search(time_range, instrument, wavelength)

# Print the query result to show what has been found.
print("Query Results for SDO/AIA 211 Å data on 22 May 2013 from 12:46 UT to 12:50 UT:")
print(query_result)

# To download the data, one would typically use Fido.fetch().
# The command below is provided for reference and is commented out.
# downloaded_files = Fido.fetch(query_result)
  
if __name__ == '__main__':
    # Execute the query printing routine.
    pass
