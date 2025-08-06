# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
SunPy VSO Query Script for SOHO LASCO-C2 and LASCO-C3 Data
Time Range: 1997-07-31 to 2014-03-31
"""

import sunpy.net
from sunpy.net import Fido, attrs as a

def main():
    # -------------------------------------------------------------------------
    # Define the time interval for the CME study (Solar Cycles 23 & 24)
    # -------------------------------------------------------------------------
    time_range = a.Time('1997-07-31', '2014-03-31')
    
    # -------------------------------------------------------------------------
    # Query 1: SOHO LASCO-C2 coronagraph data (white-light intensity)
    # -------------------------------------------------------------------------
    c2_query = Fido.search(
        time_range,
        a.Source('SOHO'),
        a.Instrument('LASCO'),
        a.Detector('C2'),
        a.Physobs('intensity')
    )
    print("=== LASCO-C2 Search Results ===")
    print(c2_query)
    
    # To download the data, uncomment the following line:
    # Fido.fetch(c2_query)
    
    # -------------------------------------------------------------------------
    # Query 2: SOHO LASCO-C3 coronagraph data (white-light intensity)
    # -------------------------------------------------------------------------
    c3_query = Fido.search(
        time_range,
        a.Source('SOHO'),
        a.Instrument('LASCO'),
        a.Detector('C3'),
        a.Physobs('intensity')
    )
    print("\n=== LASCO-C3 Search Results ===")
    print(c3_query)
    
    # To download the data, uncomment the following line:
    # Fido.fetch(c3_query)

if __name__ == "__main__":
    main()
