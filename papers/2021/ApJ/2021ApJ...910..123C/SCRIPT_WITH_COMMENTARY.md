# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's Fido to query the Virtual Solar Observatory (VSO) for data corresponding
to a GOES M3.7-class solar flare observed on 04-Nov-2015. Two instruments are targeted based on
the context provided:

1. SDO/AIA: Query for extreme ultraviolet (EUV) imaging data in the 171 Å and 1600 Å passbands
   over the time period 13:34 – 13:54 UT on 04-Nov-2015. Although the passbands are not explicitly
   set in the query (only required values are the instrument and time range), these observations are
   known to have been used to study the flare’s coronal and upper photospheric/transition region emission.

2. RHESSI: Query for hard X-ray (HXR) imaging data from RHESSI over a slightly shorter time window,
   from 13:35 UT to 13:43 UT on the same day, which covers the period before the spacecraft entered
   night, capturing key non-thermal flare emissions.

Note:
- The queries are printed to the console.
- The Fido.fetch commands are provided as comments and can be activated for actual data retrieval.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time ranges based on the observation intervals mentioned:
# SDO/AIA observation from 13:34 to 13:54 UT on 04-Nov-2015.
sdo_start_time = "2015-11-04T13:34:00"
sdo_end_time   = "2015-11-04T13:54:00"

# RHESSI observation from 13:35 to 13:43 UT on 04-Nov-2015.
rhessi_start_time = "2015-11-04T13:35:00"
rhessi_end_time   = "2015-11-04T13:43:00"

# Query for SDO/AIA observations.
# Since the required values are only the time range and the instrument, we use these directly.
# Note: SDO/AIA provides multiple wavelengths (including 171 Å and 1600 Å) as per the context,
# and while the specific wavelength channels are not set in the query, they can be filtered later if needed.
sdo_query = Fido.search(a.Time(sdo_start_time, sdo_end_time),
                        a.Instrument('AIA'))
print("SDO/AIA Query Results:")
print(sdo_query)

# Uncomment the following line to actually fetch the SDO/AIA data.
# sdo_files = Fido.fetch(sdo_query)

# Query for RHESSI hard X-ray observations.
# The RHESSI instrument data is available via the VSO with the instrument name "RHESSI".
rhessi_query = Fido.search(a.Time(rhessi_start_time, rhessi_end_time),
                           a.Instrument('RHESSI'))
print("\nRHESSI Query Results:")
print(rhessi_query)

# Uncomment the following line to actually fetch the RHESSI data.
# rhessi_files = Fido.fetch(rhessi_query)

if __name__ == "__main__":
    print("\nQueries completed. Review the printed query results above.")
