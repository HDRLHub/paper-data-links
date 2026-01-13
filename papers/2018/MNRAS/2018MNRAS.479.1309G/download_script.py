# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's Fido to query solar observation data relevant to the study on 
magnetic evolution during Carrington Rotations CR2119–CR2121 (2012 February 4–March 16, 2012).

Data are queried from:
  1. SDO/AIA (for EUV observations during two distinct periods:
       - Period I: February 5, 2012 – February 14, 2012 
       - Period III: February 22, 2012 – March 16, 2012)
  2. STEREO/EUVI (from STEREO_A and STEREO_B for Period II: February 15, 2012 – February 21, 2012)
  3. SDO/HMI (magnetograms over the full period February 4, 2012 – March 16, 2012)
  
Only the time range and the instrument are specified in the queries to reflect the available 
data details provided in the study.
  
Note: The Fido.fetch commands are commented out. They can be activated once the query results are verified.
"""

import sunpy.net.Fido as Fido
from sunpy.net import attrs as a
import astropy.units as u

# -------------------------------
# Query 1: SDO/AIA - EUV Observations (Period I)
# Time range: 2012-02-05 to 2012-02-14
# Wavelength filters in the context: 304 Å, 171 Å, 193 Å, 211 Å (observed with AIA)
start_period1 = '2012-02-05T00:00:00'
end_period1   = '2012-02-14T23:59:59'
query_aia_period1 = Fido.search(
    a.Time(start_period1, end_period1),
    a.Source('SDO'),
    a.Instrument('AIA')
)
print("Query Results for SDO/AIA (Period I: Feb 5, 2012 - Feb 14, 2012):")
print(query_aia_period1)
# Retrieve the data (uncomment after verifying query results)
# files_aia_period1 = Fido.fetch(query_aia_period1)


# -------------------------------
# Query 2: SDO/AIA - EUV Observations (Period III)
# Time range: 2012-02-22 to 2012-03-16
start_period3 = '2012-02-22T00:00:00'
end_period3   = '2012-03-16T23:59:59'
query_aia_period3 = Fido.search(
    a.Time(start_period3, end_period3),
    a.Source('SDO'),
    a.Instrument('AIA')
)
print("\nQuery Results for SDO/AIA (Period III: Feb 22, 2012 - Mar 16, 2012):")
print(query_aia_period3)
# Retrieve the data (uncomment after verifying query results)
# files_aia_period3 = Fido.fetch(query_aia_period3)


# -------------------------------
# Query 3: STEREO/EUVI - EUV Observations (Period II)
# Time range: 2012-02-15 to 2012-02-21
# Context indicates use of EUV filters 304 Å and 195 Å.
start_period2 = '2012-02-15T00:00:00'
end_period2   = '2012-02-21T23:59:59'

# STEREO_A EUVI Query
query_euvi_stereo_a = Fido.search(
    a.Time(start_period2, end_period2),
    a.Source('STEREO_A'),
    a.Instrument('SECCHI'),
    a.Detector('EUVI')
)
print("\nQuery Results for STEREO_A EUVI (Period II: Feb 15, 2012 - Feb 21, 2012):")
print(query_euvi_stereo_a)
# Retrieve the data (uncomment after verifying query results)
# files_euvi_stereo_a = Fido.fetch(query_euvi_stereo_a)

# STEREO_B EUVI Query
query_euvi_stereo_b = Fido.search(
    a.Time(start_period2, end_period2),
    a.Source('STEREO_B'),
    a.Instrument('SECCHI'),
    a.Detector('EUVI')
)
print("\nQuery Results for STEREO_B EUVI (Period II: Feb 15, 2012 - Feb 21, 2012):")
print(query_euvi_stereo_b)
# Retrieve the data (uncomment after verifying query results)
# files_euvi_stereo_b = Fido.fetch(query_euvi_stereo_b)


# -------------------------------
# Query 4: SDO/HMI - Magnetograms
# Time range: 2012-02-04 to 2012-03-16, capturing magnetic evolution over the Carrington Rotations
start_hmi = '2012-02-04T00:00:00'
end_hmi   = '2012-03-16T23:59:59'
query_hmi = Fido.search(
    a.Time(start_hmi, end_hmi),
    a.Source('SDO'),
    a.Instrument('HMI')
)
print("\nQuery Results for SDO/HMI Magnetograms (Feb 4, 2012 - Mar 16, 2012):")
print(query_hmi)
# Retrieve the data (uncomment after verifying query results)
# files_hmi = Fido.fetch(query_hmi)

# End of script
