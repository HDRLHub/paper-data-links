# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for SOHO/SWAN data.
The SOHO/SWAN instrument observes backscattered Lyman‑α emission, which is used 
to infer information about the solar wind and interstellar hydrogen. The VSO interface 
provided specifies SWAN on SOHO with a wavelength of 1215.6 Å. The time range will be set 
from January 12, 1996 to a recent date (example used here: October 3, 2023), which aligns 
with the instrument's availability as described in the VSO interface.
"""

# Import necessary modules
import astropy.units as u
from sunpy.net import Fido, attrs

# Define the observation time range based on the VSO interface.
start_time = "1996-01-12"  # Start date from available full time range in the VSO interface.
end_time = "2023-10-03"    # Example end date (can be updated to a current date).

# Define the time attribute for the query.
time_query = attrs.Time(start_time, end_time)

# Define the source attribute (SOHO) based on the VSO interface.
source_query = attrs.Source("SOHO")

# Define the instrument attribute (SWAN) based on the VSO interface.
instrument_query = attrs.Instrument("SWAN")

# Define the wavelength attribute for Lyman-alpha (1215.6 Å).
wavelength_query = attrs.Wavelength(1215.6 * u.AA)

# Construct the query using Fido.search with explicit and separate arguments.
query_result = Fido.search(time_query, source_query, instrument_query, wavelength_query)

# Print the query results.
print("Query Results:")
print(query_result)

# To download the data, uncomment the following line:
# downloaded_files = Fido.fetch(query_result)

if __name__ == "__main__":
    pass
