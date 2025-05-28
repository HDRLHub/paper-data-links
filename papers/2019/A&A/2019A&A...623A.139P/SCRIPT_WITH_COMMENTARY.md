# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query CME observation data as described in the paper.
The primary instrument of interest is the SECCHI/COR2 coronagraph onboard both the STEREO-A and STEREO-B spacecraft.
The data collection period for SECCHI/COR2 is from January 2007 to December 2013.
Additionally, a complementary query is provided for the SOHO/LASCO C3 instrument,
which is used in the study to validate the CME propagation direction and mass estimation.
Note: The Fido.fetch() calls are commented out to prevent accidental data downloads.
"""

from sunpy.net import Fido, attrs as a

# ---------------------------
# Query for STEREO-A SECCHI/COR2 data
# ---------------------------

# Define the time range for the CME observations (January 2007 – December 2013)
time_range_secchi = a.Time("2007-01-01", "2013-12-31")

# Define the instrument attributes for SECCHI and COR2 on STEREO-A
source_stereo_a = a.Source("STEREO_A")
instrument_secchi = a.Instrument("SECCHI")
detector_cor2 = a.Detector("COR2")

# Construct the query for STEREO-A SECCHI/COR2
query_result_stereo_a = Fido.search(time_range_secchi, source_stereo_a, instrument_secchi, detector_cor2)
print("Query result for STEREO-A SECCHI/COR2:")
print(query_result_stereo_a)

# Uncomment the following line to download data for STEREO-A SECCHI/COR2
# files_stereo_a = Fido.fetch(query_result_stereo_a)


# ---------------------------
# Query for STEREO-B SECCHI/COR2 data
# ---------------------------

# Define the instrument attributes for SECCHI and COR2 on STEREO-B
source_stereo_b = a.Source("STEREO_B")
# The time range, instrument, and detector remain the same as for STEREO-A
query_result_stereo_b = Fido.search(time_range_secchi, source_stereo_b, instrument_secchi, detector_cor2)
print("\nQuery result for STEREO-B SECCHI/COR2:")
print(query_result_stereo_b)

# Uncomment the following line to download data for STEREO-B SECCHI/COR2
# files_stereo_b = Fido.fetch(query_result_stereo_b)


# ---------------------------
# Optional: Query for SOHO/LASCO C3 data (for CME comparative confirmation)
# ---------------------------

# Define a specific event date (e.g., CME on September 22, 2011) for LASCO C3 observation.
# This query is used to complement the SECCHI/COR2 observations.
time_range_lasco = a.Time("2011-09-22T00:00:00", "2011-09-22T23:59:59")

# Define the source, instrument, and detector for SOHO/LASCO C3
source_soho = a.Source("SOHO")
instrument_lasco = a.Instrument("LASCO")
detector_c3 = a.Detector("C3")

# Construct the query for SOHO/LASCO C3 for the given event date
query_result_lasco = Fido.search(time_range_lasco, source_soho, instrument_lasco, detector_c3)
print("\nQuery result for SOHO/LASCO C3 on September 22, 2011:")
print(query_result_lasco)

# Uncomment the following line to download data for SOHO/LASCO C3
# files_lasco = Fido.fetch(query_result_lasco)


if __name__ == "__main__":
    print("\nSunPy VSO queries executed. Please review the printed query results.")
