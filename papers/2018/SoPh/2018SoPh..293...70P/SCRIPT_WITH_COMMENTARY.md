# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the data for SOHO/ERNE using SunPy’s VSO client.
According to the study context, we are interested in the SOHO/ERNE data
collected during the intercalibration period “from the noon on 15 December 2006 to 20:00 UT on 16 December 2006.”
The query uses only the required values: the time range and the instrument.
Note: Although the context also refers to STEREO/HET, it is not available in the provided VSO interface.
"""

from sunpy.net import Fido, attrs as a

def main():
    # Define the time range for the intercalibration study
    start_time = "2006-12-15T12:00:00"
    end_time   = "2006-12-16T20:00:00"
    
    # Define the instrument parameters based on the context and VSO interface
    # We use the 'ERNE' instrument onboard SOHO.
    query = Fido.search(
        a.Time(start_time, end_time),
        a.Instrument("ERNE"),
        a.Source("SOHO")
    )
    
    # Print out the search query results
    print("Query Results for SOHO/ERNE:")
    print(query)
    
    # Uncomment the following line to fetch the data (this is commented to avoid unwanted downloads)
    # downloaded_files = Fido.fetch(query)
    # print("Downloaded files:", downloaded_files)

if __name__ == "__main__":
    main()
