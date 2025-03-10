# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use SunPy's VSO interface to query data from two instruments:
1. SOHO LASCO (specifically the C2 detector, which is available from 1995/12/08 to present).
2. SDO AIA (with multiple wavelengths available; here we query data around a CME event time).

The time range chosen corresponds to the training event example from the context,
around the event date 2010-04-03. The query uses explicit start and end times.
Note: The Fido.fetch commands are commented out to prevent automatic downloading.
"""

from sunpy.net import Fido, attrs as a

# Define the time range around the CME event (Event 1: 2010-04-03).
start_time = "2010-04-03T10:00:00"
end_time   = "2010-04-03T16:00:00"

# ---------------------------
# Query for SOHO LASCO data:
# ---------------------------

# Here, we query the LASCO instrument from SOHO.
# We select the C2 detector because its available time range covers 2010.
soho_lasco_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('LASCO'),
    a.Source('SOHO'),
    a.Detector('C2')
)

# Print the query results for SOHO LASCO data
print("SOHO LASCO (C2 detector) Query Results:")
print(soho_lasco_query)

# Uncomment the following line to fetch the LASCO data files:
# lasco_files = Fido.fetch(soho_lasco_query)
# print("Downloaded LASCO files:", lasco_files)

# ---------------------------
# Query for SDO AIA data:
# ---------------------------

# The SDO AIA instrument provides high-resolution EUV observations.
# Even though the available wavelengths include several channels,
# here we simply query using the required instrument and time range.
sdo_aia_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('AIA'),
    a.Source('SDO')
)

# Print the query results for SDO AIA data
print("\nSDO AIA Query Results:")
print(sdo_aia_query)

# Uncomment the following line to fetch the AIA data files:
# aia_files = Fido.fetch(sdo_aia_query)
# print("Downloaded AIA files:", aia_files)

if __name__ == "__main__":
    print("\nVSO queries completed. Review the printed query tables for details.")
