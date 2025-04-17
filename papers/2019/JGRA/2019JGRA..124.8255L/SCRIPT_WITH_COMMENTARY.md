# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses sunpy’s VSO client (Fido) to query SDO data relevant for the study of a moderate C1.1 flare on 2013 September 24.
We are interested in:
    1. AIA EUV imaging in 304 Å and 171 Å channels for observing the filament dynamics and chromospheric response.
    2. HMI data for continuum intensity and LOS magnetograms to monitor pre-flare photospheric magnetic field evolution.
The time range for the observations is set from 21:00 UT to 22:56 UT on 2013 September 24.
Note: TIP-II data are not available in the VSO interface and are not queried here.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the observation time range
start_time = "2013-09-24T21:00:00"
end_time = "2013-09-24T22:56:00"
time_range = a.Time(start_time, end_time)

# -----------------------------------------------------------------------
# Query 1: SDO AIA data in the 304 Å channel.
# The AIA instrument on board SDO provides various channels.
# Here we request data corresponding to the 304 Å filter (He II emission)
# which is important for studying the chromospheric response during the flare.
# -----------------------------------------------------------------------

aia_304_query = Fido.search(time_range,
                            a.Instrument("AIA"),
                            a.Wavelength(304*u.AA, 304*u.AA))
print("AIA 304 Å Query Results:")
print(aia_304_query)

# -----------------------------------------------------------------------
# Query 2: SDO AIA data in the 171 Å channel.
# The 171 Å channel (Fe IX emission) helps in visualizing the coronal loops
# and the dynamics of the filament.
# -----------------------------------------------------------------------

aia_171_query = Fido.search(time_range,
                            a.Instrument("AIA"),
                            a.Wavelength(171*u.AA, 171*u.AA))
print("AIA 171 Å Query Results:")
print(aia_171_query)

# -----------------------------------------------------------------------
# Query 3: SDO HMI data.
# HMI provides photospheric observations such as continuum intensity and
# line-of-sight (LOS) magnetograms. These are used to track the evolving
# magnetic field and flux cancellation near the flare site.
# -----------------------------------------------------------------------

hmi_query = Fido.search(time_range,
                        a.Instrument("HMI"))
print("HMI Query Results:")
print(hmi_query)

# -----------------------------------------------------------------------
# Data fetching: Once the queries have been reviewed and confirmed, the
# Fido.fetch commands below can be used to download the data.
# They are commented out by default.
# -----------------------------------------------------------------------

# Fetch AIA 304 Å data
# aia_304_files = Fido.fetch(aia_304_query)

# Fetch AIA 171 Å data
# aia_171_files = Fido.fetch(aia_171_query)

# Fetch HMI data
# hmi_files = Fido.fetch(hmi_query)

if __name__ == "__main__":
    print("Sunpy VSO queries executed. Review the query results above.")
