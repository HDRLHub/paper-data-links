# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) using SunPy for LASCO C2 coronagraph data 
taken by the SOHO spacecraft. In the context of the paper, LASCO C2 images were used to visually 
compare the observed solar corona with numerical electron density models (e.g., AWSoM). 

We query for two specific dates corresponding to the AUSTRAL program sessions:
    - AUA020 session: May 1, 2017
    - AOV022 session: May 1, 2018

The VSO interface confirms that the LASCO instrument on SOHO has data available for detector C2
from December 8, 1995 to the present.
"""

import datetime
from sunpy.net import Fido, attrs as a

def query_lasco_c2(time_start, time_end):
    # Build a query for LASCO C2 images.
    # We use the time range, instrument 'LASCO', and detector 'C2' as required.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Instrument("lasco"),
        a.Detector("C2")
    )
    print("Query results for LASCO C2 from {} to {}:".format(time_start, time_end))
    print(query_result)
    # To actually download the data, uncomment the following line:
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:")
    # print(downloaded_files)

if __name__ == "__main__":
    # Query for AUA020 session data on May 1, 2017.
    query_lasco_c2("2017-05-01", "2017-05-02")
    
    # Query for AOV022 session data on May 1, 2018.
    query_lasco_c2("2018-05-01", "2018-05-02")
    
    print("Queries completed.")
