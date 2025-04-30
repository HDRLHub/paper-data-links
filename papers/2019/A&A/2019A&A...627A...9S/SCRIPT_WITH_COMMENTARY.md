# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy's VSO client to query white–light coronagraph data
for constructing a near‐synchronic Carrington map from CR 2091. The data
are taken from:
    1. SOHO LASCO–C2 (white–light coronagraph on SOHO)
    2. STEREO-A SECCHI–COR1 (white–light coronagraph on STEREO-A)
    3. STEREO-B SECCHI–COR1 (white–light coronagraph on STEREO-B)

The observation time range is from 2009 December 07 to 2010 January 03,
as specified in the paper. Note that even though additional instrument
options exist in the VSO interface, we select only those used in the study.
"""

from sunpy.net import Fido, attrs as a

# Define the observation time range for Carrington Rotation (CR 2091)
start_time = "2009-12-07"
end_time = "2010-01-03"

# -----------------------------------------------------------------------------
# Query 1: SOHO LASCO-C2 white-light coronagraph data
# -----------------------------------------------------------------------------
# The LASCO-C2 data are used as a central reference for the Carrington map.
query_result_lascoC2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Physobs("intensity")
)

print("Query result for SOHO LASCO-C2 data:")
print(query_result_lascoC2)

# Uncomment the following line to download the data
# downloaded_files_lascoC2 = Fido.fetch(query_result_lascoC2)

# -----------------------------------------------------------------------------
# Query 2: STEREO-A SECCHI-COR1 white-light coronagraph data
# -----------------------------------------------------------------------------
# STEREO-A's COR1 data provide a different vantage point to complement LASCO-C2.
query_result_stereoA_COR1 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR1"),
    a.Physobs("intensity polarization_vector")
)

print("\nQuery result for STEREO-A SECCHI-COR1 data:")
print(query_result_stereoA_COR1)

# Uncomment the following line to download the data
# downloaded_files_stereoA_COR1 = Fido.fetch(query_result_stereoA_COR1)

# -----------------------------------------------------------------------------
# Query 3: STEREO-B SECCHI-COR1 white-light coronagraph data
# -----------------------------------------------------------------------------
# STEREO-B's COR1 data are also used to build the near-synchronic Carrington map.
query_result_stereoB_COR1 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR1"),
    a.Physobs("intensity polarization_vector")
)

print("\nQuery result for STEREO-B SECCHI-COR1 data:")
print(query_result_stereoB_COR1)

# Uncomment the following line to download the data
# downloaded_files_stereoB_COR1 = Fido.fetch(query_result_stereoB_COR1)

if __name__ == "__main__":
    # Main block can be used to add additional processing if needed.
    pass
