# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client to query data from the SOHO MDI instrument.
According to the context (STARA sunspot catalogue from MDI images) and the available
VSO interface information, we are interested in MDI intensity images taken by SOHO 
(and recorded at 6768.0 Angstrom) within the period May 1996 to October 2010.
Note that the available data in the VSO records have a full time range that
includes this period. The query below explicitly sets the instrument, source, 
physical observable, wavelength, and the time range.
"""

# Import required modules from sunpy.net
from sunpy.net import Fido, attrs as a

# Define the query parameters
# Time range is set to cover May 1, 1996 to October 31, 2010 as per the context.
start_time = "1996-05-01"
end_time = "2010-10-31"

# Build the query for SOHO/MDI intensity images.
# We choose "intensity" as the physical observable because the STARA sunspot 
# catalogue is derived from MDI images. The wavelength is given as 6768.0 Angstrom.
query = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Physobs("intensity"),
    a.Wavelength(6768.0, 6768.0),
    a.WavelengthUnits("Angstrom")
)

# Print out summary information about the query results
print("Query Results:")
print(query)

# To download the data, you can uncomment the following fetch command.
# files = Fido.fetch(query)
# print("Downloaded files:", files)

if __name__ == '__main__':
    pass
