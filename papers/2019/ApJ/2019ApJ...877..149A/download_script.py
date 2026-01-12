# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script creates SunPy VSO queries for downloading observational data used in the study.
The paper focuses on analyzing CME kinematics with LASCO/SOHO white-light coronagraph data 
(from the C2 and C3 detectors, used exclusively since LASCO/C1 is disabled) as well as 
complementary EUV imaging from AIA/SDO to investigate CME initiation and related phenomena.

The selected time range is 2010-01-01 to 2017-12-31 to match the observational period (first 8 years of the SDO era).
"""

from sunpy.net import Fido, attrs as a

# Define the common time range for the queries: 2010 - 2017.
time_range = a.Time("2010-01-01", "2017-12-31")

# -------------------------------
# Query 1: LASCO/SOHO Data (C2 detector)
# -------------------------------
# LASCO is used to track CME height-time profiles in white light. The C2 detector provides
# observations that are part of the study's uniform data collection.
query_lasco_c2 = Fido.search(
    time_range,
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print the query results for LASCO/C2.
print("Query Results for LASCO/SOHO - C2 Detector:")
print(query_lasco_c2)

# Uncomment the following line to fetch the LASCO/C2 data once you are ready.
# files_lasco_c2 = Fido.fetch(query_lasco_c2)

# -------------------------------
# Query 2: LASCO/SOHO Data (C3 detector)
# -------------------------------
# The C3 detector onboard LASCO provides complementary observations in white light,
# covering larger fields-of-view useful to trace CME propagation.
query_lasco_c3 = Fido.search(
    time_range,
    a.Instrument("LASCO"),
    a.Detector("C3")
)

# Print the query results for LASCO/C3.
print("\nQuery Results for LASCO/SOHO - C3 Detector:")
print(query_lasco_c3)

# Uncomment the following line to fetch the LASCO/C3 data once you are ready.
# files_lasco_c3 = Fido.fetch(query_lasco_c3)

# -------------------------------
# Query 3: AIA/SDO Data
# -------------------------------
# AIA on SDO offers high-cadence EUV imaging essential for detecting EUV dimming and early CME
# initiation signatures. We query AIA data over the same period.
query_aia = Fido.search(
    time_range,
    a.Instrument("AIA")
)

# Print the query results for AIA.
print("\nQuery Results for AIA/SDO:")
print(query_aia)

# Uncomment the following line to fetch the AIA data once you are ready.
# files_aia = Fido.fetch(query_aia)

if __name__ == '__main__':
    # The script prints the query details for LASCO (C2 and C3) and AIA.
    # The Fido.fetch commands are commented out to prevent automatic downloading.
    print("\nSunPy VSO queries have been constructed as per the scientific instrumentation requirements.")
