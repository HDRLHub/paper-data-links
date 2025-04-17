# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query SOHO/LASCO data for a study-specific epoch (2009–2013).
For this period, the LASCO detectors C2 and C3 (which have data available from 1995/12/08 to present)
are used to gather white–light coronagraph images that can be later analyzed to derive CME height–time profiles.
Note: Although the paper also describes overall operational and in-situ measurements, this query focuses on
the SOHO/LASCO white–light observations for the 2009 to 2013 time range.
"""

# Import SunPy's VSO client and attribute helper
from sunpy.net import Fido, attrs as a

# Define the query time range for the study-specific epoch (2009–2013)
time_range = a.Time("2009-01-01", "2013-12-31")

# Define the source and instrument as given in the paper
source = a.Source("SOHO")
instrument = a.Instrument("LASCO")

# For LASCO, data from detectors C2 and C3 are available over the desired time range.
# Query 1: SOHO/LASCO data using Detector C2
detector_C2 = a.Detector("C2")
query_result_C2 = Fido.search(time_range, source, instrument, detector_C2)
print("Query Results for SOHO/LASCO Detector C2 (2009–2013):")
print(query_result_C2)

# Uncomment the following line to fetch the data for Detector C2 if desired.
# downloaded_files_C2 = Fido.fetch(query_result_C2)

# Query 2: SOHO/LASCO data using Detector C3
detector_C3 = a.Detector("C3")
query_result_C3 = Fido.search(time_range, source, instrument, detector_C3)
print("Query Results for SOHO/LASCO Detector C3 (2009–2013):")
print(query_result_C3)

# Uncomment the following line to fetch the data for Detector C3 if desired.
# downloaded_files_C3 = Fido.fetch(query_result_C3)

if __name__ == "__main__":
    print("SOHO/LASCO VSO query script executed successfully.")
