# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the Virtual Solar Observatory (VSO)
using SunPy for a multi-instrument study associated with the EUV wave event
from 2012 May 14. The event was observed with SDO/AIA and SDO/HMI. For AIA,
we focus on the 171 Å channel (which shows the EUV wavefronts) and the 304 Å
channel (which displays the jets). For HMI we query line-of-sight magnetograms
that are used to study the underlying magnetic field evolution.

The script sets the time range and instrument for each query. 
Note: The Fido.fetch() commands are provided as comments and are not executed.
"""

# Import necessary modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time interval for the event: 2012 May 14, from 08:45:00 to 09:45:00 UT.
start_time = "2012-05-14T08:45:00"
end_time = "2012-05-14T09:45:00"

# ---------------------------
# Query 1: SDO/AIA Data
# ---------------------------
# We query SDO/AIA for the EUV observations.
# According to the paper, the AIA observations of interest are in the 171 Å channel
# (showing the running-difference images for EUV wavefronts) and in the 304 Å channel
# (displaying the jets).
#
# The VSO interface lists AIA with available wavelengths including 171.0 - 175.0 and 304.0 Å.
# Here, we set our queries for approximately 171 Å and 304 Å.
query_aia_171 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("AIA"),
    a.Wavelength(171*u.AA)
)

query_aia_304 = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("AIA"),
    a.Wavelength(304*u.AA)
)

# Print the query results for AIA 171 and 304.
print("Query Results for SDO/AIA 171 Å:")
print(query_aia_171)
print("Query Results for SDO/AIA 304 Å:")
print(query_aia_304)

# Uncomment the following lines to fetch AIA data:
# files_aia_171 = Fido.fetch(query_aia_171)
# files_aia_304 = Fido.fetch(query_aia_304)

# ---------------------------
# Query 2: SDO/HMI Data
# ---------------------------
# We also query SDO/HMI to obtain line-of-sight (LOS) magnetograms,
# which were used to monitor the photospheric magnetic flux changes
# in the active region during the event.
#
# The VSO interface provides multiple HMI entries;
# here we use the one with physobs "LOS_magnetic_field".
query_hmi = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")
)

# Print the query results for HMI LOS magnetograms.
print("Query Results for SDO/HMI LOS Magnetograms:")
print(query_hmi)

# Uncomment the following line to fetch HMI data:
# files_hmi = Fido.fetch(query_hmi)

if __name__ == "__main__":
    # Running the queries above will print out the search results.
    # This script is structured to show how one would set up the queries.
    # Further data processing and analysis would follow after data retrieval.
    pass
