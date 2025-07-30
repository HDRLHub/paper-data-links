# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO interface to create two queries based on the context provided in the paper.
The paper details a multi-wavelength analysis of the SOL2014-02-16T064600 solar flare.
We query for:
  1. IRIS data covering the full raster scan (06:16–07:19 UT on 2014-02-16).
  2. RHESSI data covering the decay phase (06:45:06–06:53:10 UT on 2014-02-16).
Note: The only required query parameters are the time range and the instrument.
The Fido.fetch commands are provided but commented out.
"""

# Import necessary modules from SunPy and astropy
import astropy.units as u
from sunpy.net import Fido, attrs as a

#---------------------------
# Query for IRIS Data
#---------------------------
# The IRIS spectrograph performed a 400-step raster scan from 06:16 UT to 07:19 UT on February 16, 2014.
# Here we query for IRIS data regardless of the specific detector (SJI, FUV, or NUV) since the available
# VSO interface shows multiple IRIS detectors and the context only requires instrument and time range.
iris_start_time = "2014-02-16T06:16:00"
iris_end_time = "2014-02-16T07:19:00"
iris_time = a.Time(iris_start_time, iris_end_time)
iris_instrument = a.Instrument("IRIS")

# Execute IRIS query
iris_query = Fido.search(iris_time, iris_instrument)
print("IRIS Query Results:")
print(iris_query)

# Optional: Download IRIS data (commented out as per instruction)
# iris_files = Fido.fetch(iris_query)

#---------------------------
# Query for RHESSI Data
#---------------------------
# The paper reports RHESSI data during the decay phase, from approximately 06:45:06 UT to 06:53:10 UT.
# This query uses the instrument 'RHESSI' from the VSO interface.
rhessi_start_time = "2014-02-16T06:45:06"
rhessi_end_time = "2014-02-16T06:53:10"
rhessi_time = a.Time(rhessi_start_time, rhessi_end_time)
rhessi_instrument = a.Instrument("RHESSI")

# Execute RHESSI query
rhessi_query = Fido.search(rhessi_time, rhessi_instrument)
print("\nRHESSI Query Results:")
print(rhessi_query)

# Optional: Download RHESSI data (commented out as per instruction)
# rhessi_files = Fido.fetch(rhessi_query)

if __name__ == "__main__":
    print("SunPy VSO queries executed. Review the printed query results for details.")
