# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query data for STEREO-A and STEREO-B
IMPACT instruments. The context provided by the paper specifies in situ measurements 
of the magnetic field (and plasma properties) during the interval 2007-01-01 to 2021-04-01.
Given the available VSO interface, we focus on the IMPACT instrument with the MAG detector 
(which measures vector magnetic field) on both STEREO-A and STEREO-B, as these best correspond 
to capturing the magnetic field information relevant for the predictive tool described in the paper.
"""

from sunpy.net import Fido, attrs as a

def main():
    # Define the time range for data query as specified in the study.
    start_time = "2007-01-01"
    end_time   = "2021-04-01"
    
    # Query for STEREO-A IMPACT instrument with the MAG detector
    query_sta = Fido.search(
        a.Time(start_time, end_time),
        a.Source("STEREO_A"),
        a.Instrument("IMPACT"),
        a.Detector("MAG")
    )
    
    # Print the query result for STEREO-A
    print("Query Result for STEREO-A IMPACT (MAG):")
    print(query_sta)
    
    # Query for STEREO-B IMPACT instrument with the MAG detector
    query_stb = Fido.search(
        a.Time(start_time, end_time),
        a.Source("STEREO_B"),
        a.Instrument("IMPACT"),
        a.Detector("MAG")
    )
    
    # Print the query result for STEREO-B
    print("\nQuery Result for STEREO-B IMPACT (MAG):")
    print(query_stb)
    
    # Uncomment the lines below to actually fetch the data once you have verified the query results.
    # files_sta = Fido.fetch(query_sta)
    # files_stb = Fido.fetch(query_stb)
    # print("\nDownloaded files for STEREO-A:", files_sta)
    # print("Downloaded files for STEREO-B:", files_stb)

if __name__ == '__main__':
    main()
