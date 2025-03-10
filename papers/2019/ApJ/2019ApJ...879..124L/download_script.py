# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query UVCS data from the SOHO mission.
The query is based on the available full time range for UVCS given in the VSO interface:
    Start time: 1996-01-20
    End time: (present) - here we set an example end date.
We use the instrument "UVCS" on board SOHO, which is one of the primary instruments discussed
in the paper for UV spectroscopy of the corona.
"""

# Import necessary modules. We only use Fido from sunpy.net along with attributes.
from sunpy.net import Fido, attrs as a

def main():
    # Define the time range for the query.
    # The available full time range for UVCS is from "1996-01-20" to "present".
    # Here we choose an example current end date. Adjust as necessary.
    time_start = "1996-01-20"
    time_end = "2023-10-04"  # Example present date
    
    # Define the source and instrument attributes.
    # For UVCS, the source is SOHO and the instrument is UVCS.
    source_attr = a.Source("SOHO")
    instrument_attr = a.Instrument("UVCS")
    
    # Build the query using the time range, source, and instrument.
    # This query will look for UVCS data in the specified time range.
    query_result = Fido.search(a.Time(time_start, time_end), source_attr, instrument_attr)
    
    # Print out the query results.
    print("Query Results:")
    print(query_result)
    
    # To download the data, you can fetch the data with Fido.
    # The following command is commented out for safety.
    # files = Fido.fetch(query_result)

if __name__ == "__main__":
    main()
