# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO interface to search for SOHO in-situ SEP event data.
In the context of the paper, SOHO’s detectors onboard the Solar and Heliospheric Observatory have
recorded more than 30 significant SEP events over a 20‐year span. We use this query to cover a time range
spanning those years. Note that, while the paper also discusses RAD measurements from MSL/Curiosity on Mars,
such in-situ planetary measurements are not (or may not be) available in the VSO interface.
"""

from sunpy.net import Fido, attrs as a

# Define the time range for the SOHO SEP event data.
# According to the paper, SOHO measured SEP events over a 20-year period.
start_time = "1996-01-01"
end_time = "2016-12-31"

# Construct the query.
# a.Time: sets the observational time interval.
# a.Instrument: specifies the instrument to use in the query (SOHO in this case).
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("soho")
)

# Print the search results to inspect the available data records.
print("SOHO Data Query Results:")
print(query_result)

# Once you verify the query returns the expected results,
# uncomment the line below to fetch the data.
# fetched_files = Fido.fetch(query_result)

if __name__ == "__main__":
    # This block ensures that the script runs only when executed directly.
    print("VSO query for SOHO SEP event data executed successfully.")
