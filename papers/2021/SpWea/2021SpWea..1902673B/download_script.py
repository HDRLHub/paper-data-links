# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query solar data relevant to two observational data sets mentioned in the context:
1. X‐ray observations from NASA Skylab (taken during the 1970s).
2. OMNI Hourly Data Set measurements of the solar wind (with separate queries for a training period and a testing period).

Note:
- The required search parameters from the context are the time ranges and the instrument (or data set) names.
- The “vso_interface” provided is empty, so we assume that the instruments mentioned (NASA Skylab and OMNI) are intended.
- Fido.fetch commands are provided as comments and not executed.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs as a

# ---------------------------
# Query 1: NASA Skylab X‐ray Telescopes (1970s)
# ---------------------------
# The context specifies observations in the 1970s by the X‐ray telescopes aboard NASA Skylab.
# We choose an approximate time range from January 1, 1970 to December 31, 1979.
# Note: The exact instrument code may vary in the VSO. Here we use "Skylab" as the instrument name.
skylab_time_start = "1970-01-01"
skylab_time_end   = "1979-12-31"

# Build the query for Skylab X-ray data.
query_skylab = Fido.search(
    a.Time(skylab_time_start, skylab_time_end),
    a.Instrument("Skylab")
    # Additional attributes such as wavelength range could be added if known.
)

# Print out the query results for the Skylab query.
print("NASA Skylab X-ray Data Query Results:")
print(query_skylab)

# If desired, fetch the data using Fido.fetch (this command is commented out).
# data_skylab = Fido.fetch(query_skylab)


# ---------------------------
# Query 2: OMNI Hourly Data Set (Solar Wind Speed)
# ---------------------------
# The context provides two time ranges for the OMNI Hourly Data Set:
#  a) Training Period: May 1992 – October 2006
#  b) Testing Period: October 2006 – October 2017
# The instrument or data set is specified as "OMNI".

# Query for the training period.
omni_train_start = "1992-05-01"
omni_train_end   = "2006-10-31"

query_omni_train = Fido.search(
    a.Time(omni_train_start, omni_train_end),
    a.Instrument("OMNI")
)

print("\nOMNI Hourly Data Set - Training Period Query Results:")
print(query_omni_train)

# Commented out fetch command:
# data_omni_train = Fido.fetch(query_omni_train)


# Query for the testing period.
omni_test_start = "2006-10-01"
omni_test_end   = "2017-10-31"

query_omni_test = Fido.search(
    a.Time(omni_test_start, omni_test_end),
    a.Instrument("OMNI")
)

print("\nOMNI Hourly Data Set - Testing Period Query Results:")
print(query_omni_test)

# Commented out fetch command:
# data_omni_test = Fido.fetch(query_omni_test)


# End of script.
if __name__ == '__main__':
    # This script performs queries and prints out the results.
    # Data fetching is disabled as per instructions.
    pass
