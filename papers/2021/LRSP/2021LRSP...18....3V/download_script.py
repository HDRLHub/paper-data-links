# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query data from the Virtual Solar Observatory (VSO)
using SunPy’s Fido interface for the Helioseismic Magnetic Imager (HMI) instrument on board SDO.
Based on the context provided, we focus on HMI data spanning the period from 2010.5 to 2019.5.
In this example, we use an approximate time range from July 1, 2010 to July 1, 2019.
The script prints the query results to the console.
Note: The Fido.fetch command is included but commented out to prevent actual data download.
"""

from sunpy.net import Fido, attrs as a

def main():
    # Define the time range based on the context (approximately the midpoints of the years)
    start_time = "2010-07-01"
    end_time = "2019-07-01"

    # Define the instrument and source for the query.
    # The VSO interface shows available data for SDO/HMI.
    # We are querying the Helioseismic Magnetic Imager (HMI) on board SDO.
    instrument = a.Instrument("HMI")
    source = a.Source("SDO")
    
    # Additional attribute for the observable may be considered,
    # however the only required values are the time range and the instrument.
    # Our query is based solely on time and instrument per the directive.
    
    # Construct the VSO query using Fido.search.
    query_result = Fido.search(a.Time(start_time, end_time), source, instrument)
    
    # Print the query result.
    print("Query Result:")
    print(query_result)
    
    # To fetch the data, uncomment the following line:
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:", downloaded_files)

if __name__ == "__main__":
    main()
