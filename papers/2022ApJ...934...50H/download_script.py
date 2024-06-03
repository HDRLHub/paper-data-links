# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a

# Define the time range for the Wind spacecraft observations
wind_start_time = '2012-06-16T00:00:00'
wind_end_time = '2012-06-17T23:59:59'
wind_time_range = a.Time(wind_start_time, wind_end_time)

# Define the time range for the Venus Express (VEX) spacecraft observations
vex_start_time = '2012-06-15T00:00:00'
vex_end_time = '2012-06-16T23:59:59'
vex_time_range = a.Time(vex_start_time, vex_end_time)

# Query for Wind spacecraft data
wind_query = Fido.search(wind_time_range, a.Instrument("WIND"))

# Query for Venus Express (VEX) spacecraft data
vex_query = Fido.search(vex_time_range, a.Instrument("VEX"))

# Display the query results
print("Query for Wind spacecraft data:")
print(wind_query)
print("Query for Venus Express (VEX) spacecraft data:")
print(vex_query)

# Uncomment the lines below to download the data
# wind_files = Fido.fetch(wind_query)
# vex_files = Fido.fetch(vex_query)
