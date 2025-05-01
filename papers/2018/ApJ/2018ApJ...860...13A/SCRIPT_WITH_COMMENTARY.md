# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This Python script uses SunPy's VSO module to query SOHO/LASCO data.
In this example, we query data from the SOHO spacecraft with the LASCO instrument,
specifically using the C2 detector. This is because the context of the paper
utilizes SOHO/LASCO observations to record ECME eruption times over the period 2000 to 2009.
The selected time range is 2000-01-01 to 2009-12-31.
Note: The query results will be printed, and the actual data download command (Fido.fetch)
is commented out.
"""

from sunpy.net import Fido, attrs as a

# Define the time range based on the paper's focus (2000-2009)
time_range = a.Time("2000-01-01", "2009-12-31")

# Define the instrument attributes for SOHO/LASCO
source = a.Source("SOHO")        # Source: SOHO spacecraft
instrument = a.Instrument("LASCO")  # Instrument: LASCO coronagraph
detector = a.Detector("C2")      # Choose detector C2 since it is available from 1995/12/08 - present

# Build the query with explicit parameters
print("Querying VSO for SOHO/LASCO (Detector C2) data from 2000 to 2009...")
query_result = Fido.search(time_range, source, instrument, detector)

# Print the query result summary
print(query_result)

# Uncomment the following line to fetch data (this step downloads the data files)
# data_files = Fido.fetch(query_result)
 
if __name__ == "__main__":
    print("Script completed. Check the printed query result for details.")
