# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses Sunpy's VSO interface to query for SOHO/MDI continuum images.
The query is specific for the "intensity" observable which corresponds to the 
continuum images used to validate the sunspot umbra detection technique in the study.
The VSO interface indicates that SOHO/MDI "intensity" data is available from 
1996/05/19 to 2011/04/12. Here, we restrict the query to the science window of 
1996 to 2010 as described in the paper.
"""

from sunpy.net import Fido, attrs as a

def main():
    # Define the time range based on the observational period from the paper (1996-2010).
    # Note the available VSO data starts from 1996/05/19, so that is used as the start.
    time_start = "1996-05-19"
    time_end = "2010-12-31"
    
    # Create the query using Sunpy's VSO interface.
    # We are querying SOHO data from the MDI instrument with the physical observable "intensity"
    # which corresponds to continuum (white-light) images.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Source("SOHO"),
        a.Instrument("MDI"),
        a.Physobs("intensity")
    )
    
    # Print the query result to review available data.
    print("Query Results:")
    print(query_result)
    
    # To fetch the data, uncomment the following lines. This would download the matching files.
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:")
    # print(downloaded_files)

if __name__ == "__main__":
    main()
