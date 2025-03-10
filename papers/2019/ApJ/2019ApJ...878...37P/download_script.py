# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query solar data using SunPy's VSO interface.
We use instruments mentioned in the study:
  1. PROBA2/SWAP for EUV imaging of CME signatures at four specific times.
  2. SDO/AIA for high-resolution EUV images (e.g., 304 Å channel) around CME4.
  3. SDO/HMI for photospheric magnetograms spanning the CME events.

Note: The time ranges and instrument names are taken directly from the context.
The Fido.fetch lines are commented out so that data are not actually downloaded.
"""

# Import the required modules from sunpy.net
from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

def query_proba2_swap():
    """
    Query PROBA2/SWAP data for four specific observation periods.
    These times correspond to CME observations:
      - CME1: 21 May 2013 at ~02:00 UT
      - CME2: 22 May 2013 at ~11:00 UT
      - CME3: 22 May 2013 at ~13:00 UT
      - CME4: 23 May 2013 at ~20:00 UT
    """
    # Define a list of time ranges (each with a short duration of 10 minutes)
    time_ranges = [
        TimeRange("2013-05-21T02:00", "2013-05-21T02:10"),
        TimeRange("2013-05-22T11:00", "2013-05-22T11:10"),
        TimeRange("2013-05-22T13:00", "2013-05-22T13:10"),
        TimeRange("2013-05-23T20:00", "2013-05-23T20:10")
    ]
    
    # Loop over each time range and query PROBA2/SWAP data
    for tr in time_ranges:
        print(f"Querying PROBA2/SWAP data for time range: {tr.start} to {tr.end}")
        query_result = Fido.search(
            a.Time(tr.start.isoformat(), tr.end.isoformat()),
            a.Source("PROBA2"),
            a.Instrument("SWAP")
        )
        # Print the query results summary
        print(query_result)
        print("-"*80)
        # Uncomment the following line to download the data
        # files = Fido.fetch(query_result)
        
def query_sdo_aia():
    """
    Query SDO/AIA data around the eruption of CME4 on 23 May 2013.
    Although AIA has multiple channels, here we request data in general for the event time.
    """
    # Define a time range of 10 minutes around CME4 (using same nominal time as PROBA2 CME4 query)
    time_range = TimeRange("2013-05-23T20:00", "2013-05-23T20:10")
    print(f"Querying SDO/AIA data for time range: {time_range.start} to {time_range.end}")
    query_result = Fido.search(
        a.Time(time_range.start.isoformat(), time_range.end.isoformat()),
        a.Source("SDO"),
        a.Instrument("AIA")
    )
    print(query_result)
    print("-"*80)
    # Uncomment the following line to download the data
    # files = Fido.fetch(query_result)

def query_sdo_hmi():
    """
    Query SDO/HMI magnetogram data that cover the period of the CME events.
    The data here span from 21 May 2013 to 24 May 2013 to capture the evolution of the photospheric magnetic field.
    """
    # Define a time range covering the CME period
    time_range = TimeRange("2013-05-21T00:00", "2013-05-24T00:00")
    print(f"Querying SDO/HMI data for time range: {time_range.start} to {time_range.end}")
    query_result = Fido.search(
        a.Time(time_range.start.isoformat(), time_range.end.isoformat()),
        a.Source("SDO"),
        a.Instrument("HMI")
    )
    print(query_result)
    print("-"*80)
    # Uncomment the following line to download the data
    # files = Fido.fetch(query_result)

def main():
    # Query PROBA2/SWAP data for CME observations
    query_proba2_swap()
    
    # Query SDO/AIA data around CME4 eruption
    query_sdo_aia()
    
    # Query SDO/HMI magnetogram data during the CME period
    query_sdo_hmi()
    
if __name__ == "__main__":
    main()
