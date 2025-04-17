# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses sunpy to query SDO/AIA, SDO/HMI, and SOHO/LASCO data from the VSO.
It is designed to capture data relevant to the coronal dimming event associated with the 2012 September 27 halo CME.
The queries are based on the following observations:
  • SDO/AIA: Full-disk EUV images around the impulsive phase of the event (pre-event at 23:06 UT to onset at ~23:50 UT on 2012-09-27).
  • SDO/HMI: A snapshot magnetogram at 23:45 UT on 2012-09-27.
  • SOHO/LASCO: White-light coronagraph images (using the C2 detector) capturing the CME on 2012-09-28.
Note: The script only constructs the queries and prints the query result summaries.
The actual data download commands (Fido.fetch) are provided in comments.
"""

# Import necessary modules from SunPy and Astropy units
from sunpy.net import Fido, attrs as a
from astropy import units as u

# ---------------------------
# Query 1: SDO/AIA EUV Observations
# ---------------------------
# Define the time range for the AIA data: covers pre-event and impulsive onset phase.
time_aia_start = "2012-09-27T23:06:00"
time_aia_end   = "2012-09-27T23:50:00"

# For this query we select SDO/AIA observations.
# Additionally, we limit the wavelength to 171 Å,
# one of the characteristic EUV passbands used to study the coronal dimming evolution.
query_aia = Fido.search(
    a.Time(time_aia_start, time_aia_end),
    a.Instrument("AIA"),
    a.Wavelength(171*u.AA, 171*u.AA)
)

# Print the query results for AIA
print("SDO/AIA Query Results:")
print(query_aia)

# Uncomment the following line to download the AIA data
# downloaded_files_aia = Fido.fetch(query_aia)

# ---------------------------
# Query 2: SDO/HMI Magnetogram
# ---------------------------
# Define the time range for the HMI observation: a single snapshot near the event at 23:45 UT.
time_hmi_start = "2012-09-27T23:45:00"
time_hmi_end   = "2012-09-27T23:46:00"

# Query for SDO/HMI magnetogram data.
query_hmi = Fido.search(
    a.Time(time_hmi_start, time_hmi_end),
    a.Instrument("HMI")
)

# Print the query results for HMI
print("\nSDO/HMI Query Results:")
print(query_hmi)

# Uncomment the following line to download the HMI data
# downloaded_files_hmi = Fido.fetch(query_hmi)

# ---------------------------
# Query 3: SOHO/LASCO White-Light Coronagraph (C2)
# ---------------------------
# Define the time range for LASCO C2 images capturing the CME on 2012-09-28.
time_lasco_start = "2012-09-28T00:00:00"
time_lasco_end   = "2012-09-28T00:40:00"

# Query for SOHO LASCO data with the C2 detector.
# Note: a.Source is specified as "SOHO" based on the vso_interface details.
query_lasco = Fido.search(
    a.Time(time_lasco_start, time_lasco_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print the query results for LASCO
print("\nSOHO/LASCO Query Results (C2 Detector):")
print(query_lasco)

# Uncomment the following line to download the LASCO data
# downloaded_files_lasco = Fido.fetch(query_lasco)

if __name__ == '__main__':
    print("\nQueries completed. Check above for query results.")
