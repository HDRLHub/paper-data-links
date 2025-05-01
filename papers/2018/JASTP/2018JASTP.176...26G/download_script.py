# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for SDO/AIA data 
in the 304 Å channel, matching the context criteria for EUV imaging of prominence eruptions. 
The AIA instrument data is available from 2010 onwards according to the VSO interface.
"""

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Define the time range for the query (from 2010-06-01 to 2010-06-02 as an example)
start_time = "2010-06-01"
end_time = "2010-06-02"
time_range = a.Time(start_time, end_time)

# Define the instrument attribute for SDO/AIA.
# According to the VSO interface, SDO/AIA data is available with wavelengths including 304 Å.
instrument_attribute = a.Instrument("AIA")

# Define the wavelength attribute.
# The wavelength is specified in Angstrom units in the VSO interface.
wavelength_attribute = a.Wave(304, 304)  # single 304 Å channel

# Combine all attributes into a query.
# This query is explicit and avoids nested calls by defining each attribute separately.
query_result = Fido.search(time_range, instrument_attribute, wavelength_attribute)

# Print out the query results.
print("Query Results:")
print(query_result)

# Uncomment the following lines to fetch the data (download not performed in this script).
# downloaded_files = Fido.fetch(query_result)
# print("Downloaded Files:")
# print(downloaded_files)

if __name__ == '__main__':
    # The script is executable and prints the VSO query results.
    pass
