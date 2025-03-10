# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs two separate Sunpy VSO queries:
1. For RHESSI data during the impulsive phase of the flare on 20 September 2002.
   Time Range: 09:25:00 to 09:30:00 UT on 20 September 2002.
2. For SOHO/EIT data in the 195 Å band used for contextual imaging.
   Time Range: 09:45:00 to 09:50:00 UT on 20 September 2002.

Note: The available VSO interface only includes RHESSI and SOHO/EIT.
The Fido.fetch commands are provided but commented out since we are only printing the query results.
"""

# Import necessary modules from sunpy.net
from sunpy.net import vso
from sunpy.net import attrs as a

def main():
    # Create a VSO client instance
    client = vso.VSOClient()

    # -----------------------------
    # Query 1: RHESSI Data Query
    # -----------------------------
    # We define the time range based on the flare impulsive phase
    time_rhessi_start = '2002-09-20T09:25:00'
    time_rhessi_end   = '2002-09-20T09:30:00'
    
    # Build the query by specifying the time range and the RHESSI instrument
    rhessi_query = client.search(
        a.Time(time_rhessi_start, time_rhessi_end),
        a.Instrument('RHESSI')
    )
    
    # Print the output of the RHESSI query
    print("RHESSI Query Result:")
    print(rhessi_query)
    print("\n")
    
    # Uncomment the following line to download RHESSI data if required.
    # data_files = client.fetch(rhessi_query)
    
    # -----------------------------
    # Query 2: SOHO/EIT Data Query
    # -----------------------------
    # We define the time range based on the SOHO/EIT imaging observations designated for loop geometry context.
    time_eit_start = '2002-09-20T09:45:00'
    time_eit_end   = '2002-09-20T09:50:00'
    
    # Build the query by specifying the time range, instrument, and source for SOHO/EIT.
    eit_query = client.search(
        a.Time(time_eit_start, time_eit_end),
        a.Instrument('EIT'),
        a.Source('SOHO')
    )
    
    # Print the output of the SOHO/EIT query
    print("SOHO/EIT Query Result:")
    print(eit_query)
    print("\n")
    
    # Uncomment the following line to download EIT data if required.
    # data_files = client.fetch(eit_query)

if __name__ == '__main__':
    main()
