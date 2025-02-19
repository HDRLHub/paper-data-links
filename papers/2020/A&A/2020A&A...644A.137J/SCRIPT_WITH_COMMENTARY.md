# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Query Script for Downloading Data from Multiple Instruments

This script creates separate queries for:
1. SDO/AIA – used to capture the hot coronal observations in the 131 Å channel during the 13 March 2012 event.
2. SDO/HMI – used to study the photospheric magnetic field evolution around the same active region (NOAA AR 11429) between 5 and 15 March 2012.
3. SOHO LASCO/C2 – used to observe the associated CME in white‐light around 17:36 UT on 13 March 2012.

Note:
  The actual data download commands (Fido.fetch) are provided but commented out.
  Ensure that SunPy and its dependencies (e.g., astropy) are installed in your Python environment.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# -------------------------------
# Query 1: SDO/AIA (131 Å) Data
# -------------------------------
# Data Collection Period: 13 March 2012 event capturing pre-eruptive EUV signatures.
# Time range: 2012-03-13 16:30:00 to 2012-03-13 16:47:00
start_aia = '2012-03-13T16:30:00'
end_aia   = '2012-03-13T16:47:00'
query_aia = Fido.search(
    a.Time(start_aia, end_aia),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(131 * u.AA)
)

print("Query Results for SDO/AIA (131 Å):")
print(query_aia)

# To download the queried data, uncomment the line below:
# downloads_aia = Fido.fetch(query_aia)


# -------------------------------
# Query 2: SDO/HMI (6173 Å) Data
# -------------------------------
# Data Collection: Tracking the evolution of the photospheric magnetic field in NOAA AR 11429.
# Time range: 2012-03-05 00:00:00 to 2012-03-15 23:59:59
start_hmi = '2012-03-05T00:00:00'
end_hmi   = '2012-03-15T23:59:59'
query_hmi = Fido.search(
    a.Time(start_hmi, end_hmi),
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Wavelength(6173 * u.AA)
)

print("\nQuery Results for SDO/HMI (6173 Å):")
print(query_hmi)

# To download the queried data, uncomment the line below:
# downloads_hmi = Fido.fetch(query_hmi)


# -------------------------------
# Query 3: SOHO LASCO/C2 Data
# -------------------------------
# Data Collection: CME observation associated with the 13 March 2012 event.
# Time range: 2012-03-13 17:36:00 to 2012-03-13 17:45:00
start_lasco = '2012-03-13T17:36:00'
end_lasco   = '2012-03-13T17:45:00'
query_lasco = Fido.search(
    a.Time(start_lasco, end_lasco),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)

print("\nQuery Results for SOHO LASCO/C2:")
print(query_lasco)

# To download the queried data, uncomment the line below:
# downloads_lasco = Fido.fetch(query_lasco)


if __name__ == "__main__":
    print("\nSunpy VSO queries are complete. Check the printed query results for details on available data.")
