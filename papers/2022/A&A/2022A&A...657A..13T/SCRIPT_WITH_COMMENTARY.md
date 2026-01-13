# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query observations from the RHESSI instrument.
According to the provided VSO interface, the instrument is "RHESSI" with a time range
from "2002/02/12" to "present". In this script, we will set the start time as specified and
use the current date as the end time to approximate "present". The query is constructed 
explicitly with these details.

Note: The script prints out the query result details. The actual data fetching via Fido.fetch 
is provided as a commented-out command, following the directive.
"""

from sunpy.net import Fido, attrs as a
import datetime

def main():
    # Define the time range for the query.
    # Start time is provided by the VSO interface.
    start_time = "2002-02-12"
    # For "present", we use the current UTC time.
    end_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    
    # Print the time range being used for clarity.
    print("Querying RHESSI data from", start_time, "to", end_time)
    
    # Construct the query:
    # a.Time: Defines the time interval for the observation.
    # a.Instrument: Specifies the instrument to query; here, it is "RHESSI".
    # The VSO interface also mentions the source and detector as RHESSI, but these are
    # implicitly handled by specifying the instrument in this case.
    query_result = Fido.search(a.Time(start_time, end_time), a.Instrument("RHESSI"))
    
    # Print out the query result information
    print("Query Results:")
    print(query_result)
    
    # If you wish to download the data, you can use the following command.
    # However, it is commented out as per the directive.
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:", downloaded_files)

if __name__ == "__main__":
    main()
