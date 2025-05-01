# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries SOHO LASCO data from the VSO using SunPy.
We choose the LASCO instrument with detector "C2" because its available time range 
("1995/12/08 - present") covers the period of interest derived from the SEP paper (2006–2014).
The query is set from 2006-07-01 to 2014-09-30 to match the SEP event observational period.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the query; this is the period during which PAMELA detected SEP events,
# and LASCO observations are used to determine related CME properties.
start_time = '2006-07-01'
end_time = '2014-09-30'

# Define the query attributes:
# - Source: SOHO, as LASCO is on board the SOHO mission.
# - Instrument: LASCO.
# - Detector: C2, as it covers the required time span.
# Additional wavelength filtering is not applied since LASCO C2 does not specify wavelength ranges.
time_attr = a.Time(start_time, end_time)
source_attr = a.Source('SOHO')
instrument_attr = a.Instrument('LASCO')
detector_attr = a.Detector('C2')

# Perform the query using Fido with explicit and clear attribute settings.
query_result = Fido.search(time_attr, source_attr, instrument_attr, detector_attr)

# Print the summary of query results.
print("Query Results for SOHO LASCO (Detector: C2) data from {} to {}:".format(start_time, end_time))
print(query_result)

# To download the data, one would normally use:
# downloaded_files = Fido.fetch(query_result)
# However, the fetch command is commented out to avoid downloading data when executing the script.
# Uncomment the next line to perform the data download.
# downloaded_files = Fido.fetch(query_result)

if __name__ == "__main__":
    # This section allows the script to be run as a standalone script.
    # Running the script will print the query result summary.
    pass
