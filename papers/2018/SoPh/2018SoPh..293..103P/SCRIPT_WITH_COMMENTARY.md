# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query LASCO coronagraph data from the Virtual Solar Observatory (VSO) using SunPy.
In our VSO interface, we have LASCO observations from SOHO with available detectors C1, C2, and C3.
We choose LASCO C2 data for our query since it provides continuous observations from 1995/12/08 until the present.
Here, we query a sample time range. (Adjust the time range as needed.)
Note: The Fido.fetch call is provided as a comment so that the query results are not actually downloaded.
"""

import sys
from sunpy.net import Fido, attrs as a

def main():
    # Define the time range for the query.
    # We choose a sample period within LASCO C2's operational period.
    time_start = "2013-10-26"
    time_end = "2013-10-29"
    
    # Define the source, instrument, and detector for the query.
    # Our VSO interface shows:
    #   Source: SOHO
    #   Instrument: LASCO
    #   Detector: C2 (available from 1995/12/08 to present)
    source_attr = a.Source("SOHO")
    instrument_attr = a.Instrument("LASCO")
    detector_attr = a.Detector("C2")
    
    # (Optional) Specify the physical observable if desired.
    # In this case, intensity is the observable for LASCO, though it is not required.
    physobs_attr = a.Physobs("intensity")
    
    # Building the query using explicit attribute calls without nesting.
    time_attr = a.Time(time_start, time_end)
    
    # Print the query details for clarity.
    print("Querying VSO for data with the following parameters:")
    print("Time Range:", time_start, "to", time_end)
    print("Source: SOHO")
    print("Instrument: LASCO")
    print("Detector: C2")
    print("Physical Observable: intensity")
    
    # Perform the VSO query.
    query_result = Fido.search(time_attr, source_attr, instrument_attr, detector_attr, physobs_attr)
    print("\nQuery Results:")
    print(query_result)
    
    # Uncomment the line below to fetch the data after inspecting the query results.
    # files = Fido.fetch(query_result)
    
if __name__ == "__main__":
    main()
