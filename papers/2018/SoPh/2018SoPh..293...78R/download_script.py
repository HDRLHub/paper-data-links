# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) using SunPy
for data related to solar eruptions during the ICME study period.
It constructs three separate queries:
    1. SDO/AIA data (available from 2010-05-12 onward) for EUV imaging
       of the solar corona used in the study.
    2. SOHO/EIT data for early 2010 (January to May 2010) which complements the AIA data.
    3. SOHO/LASCO data using the C2 detector for white-light coronagraph observations
       during the same period as the AIA data.
Note: The script prints the query results and the Fido.fetch commands are commented out.
"""

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a

# Define time ranges based on the context of the paper.
# For SDO/AIA, even though the study period is January 2010 to August 2011,
# AIA data are available from 2010-05-12 hence we choose that as the start time.
aia_start = "2010-05-12T00:00:00"
aia_end   = "2011-08-31T23:59:59"

# For SOHO/EIT, the useful period in the study (from January to May 2010)
eit_start = "2010-01-01T00:00:00"
eit_end   = "2010-05-01T23:59:59"

# For SOHO/LASCO (using the C2 detector as it is available during the required period),
# we use the same time range as AIA.
lasco_start = "2010-05-12T00:00:00"
lasco_end   = "2011-08-31T23:59:59"

# ------------------ Query for SDO/AIA ------------------
# Querying the VSO for SDO/AIA data in the EUV wavelengths.
query_aia = Fido.search(
    a.Time(aia_start, aia_end),
    a.Source('SDO'),
    a.Instrument('AIA')
)
print("SDO/AIA Query Results:")
print(query_aia)

# Uncomment the following line to fetch the SDO/AIA data:
# files_aia = Fido.fetch(query_aia)

# ------------------ Query for SOHO/EIT ------------------
# Querying the VSO for SOHO/EIT data for the period January to May 2010.
query_eit = Fido.search(
    a.Time(eit_start, eit_end),
    a.Source('SOHO'),
    a.Instrument('EIT')
)
print("\nSOHO/EIT Query Results:")
print(query_eit)

# Uncomment the following line to fetch the SOHO/EIT data:
# files_eit = Fido.fetch(query_eit)

# ------------------ Query for SOHO/LASCO (Detector: C2) ------------------
# Querying the VSO for SOHO/LASCO data using the C2 detector.
query_lasco = Fido.search(
    a.Time(lasco_start, lasco_end),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("\nSOHO/LASCO Query Results (Detector: C2):")
print(query_lasco)

# Uncomment the following line to fetch the SOHO/LASCO data:
# files_lasco = Fido.fetch(query_lasco)

if __name__ == '__main__':
    print("\nQueries completed. Data download commands are provided as commented code.")
