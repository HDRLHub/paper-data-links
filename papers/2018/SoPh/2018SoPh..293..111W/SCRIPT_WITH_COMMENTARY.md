# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query solar observational data from the SOHO spacecraft,
specifically from the GOLF instrument. The available data range is from 1996-01-01 to the present,
and the query filters by:
  - Source: SOHO
  - Instrument: GOLF
  - Detector: Fsmain
  - Physical Observable: LOS_velocity
  - Wavelength range: 5884.0 to 5902.0 Angstrom

This query matches the information provided in the VSO interface.
"""

import datetime
from sunpy.net import Fido, attrs as a

# Define the time range for the search.
# Note: VSO "Available Full Time Range" lists "1996/01/01 - present",
# so we set the start time to 1996-01-01 and use the current date for the end time.
start_time = "1996-01-01"
end_time = datetime.datetime.now().strftime("%Y-%m-%d")  # Using today's date as "present"

# Set up the query parameters based on the VSO interface details.
time_attr = a.Time(start_time, end_time)
source_attr = a.Source("SOHO")
instrument_attr = a.Instrument("GOLF")
detector_attr = a.Detector("Fsmain")
physobs_attr = a.Physobs("LOS_velocity")
wavelength_attr = a.Wavelength(5884.0, 5902.0)  # Wavelength in Angstrom

# Execute the search query on the Virtual Solar Observatory using Fido.
query = Fido.search(time_attr, source_attr, instrument_attr, detector_attr, physobs_attr, wavelength_attr)

# Print out the query results.
print("VSO Query Results for SOHO/GOLF instrument:")
print(query)

# To fetch the data files from the returned query (commented out as per instruction).
# downloaded_files = Fido.fetch(query)
  
if __name__ == "__main__":
    # Running the main block to show the query result on execution.
    pass
