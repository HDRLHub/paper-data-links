# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client (Fido) to query LASCO C1 data from the SOHO mission.
Based on the provided VSO interface and the context of the paper, we query data from the
SOHO LASCO C1 coronagraph. The query is limited by the available time range for LASCO C1
(1995-12-08 to 2000-08-09) as specified in the interface.
"""

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the query according to the available full time range for LASCO C1
# Note: LASCO C1 is known to have provided data until it failed. The available range from the VSO is used.
time_range = a.Time("1995-12-08", "2000-08-09")

# Define additional query attributes based on the VSO interface:
# a.Source: "SOHO"
# a.Instrument: "LASCO"
# a.Detector: "C1" (for LASCO C1 coronagraph)
# a.Physobs: "intensity" (indicating white-light intensity observations for coronal imaging)
source = a.Source("SOHO")
instrument = a.Instrument("LASCO")
detector = a.Detector("C1")
physobs = a.Physobs("intensity")

# Construct and execute the query using Fido search.
# Each attribute is explicitly provided and no nested loops or calls are used.
result = Fido.search(time_range, source, instrument, detector, physobs)

# Print the query result details (this shows a summary of available files and metadata).
print("Query Result Summary:")
print(result)

# Fetching the data is commented out to avoid running the fetch command.
# To download the queried data, uncomment the following line:
# data_files = Fido.fetch(result)

if __name__ == "__main__":
    # This main block allows the script to be executed directly.
    print("VSO Query for SOHO LASCO C1 data completed.")
