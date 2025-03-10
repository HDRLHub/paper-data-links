# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client (via Fido) to query LASCO C2 white-light coronagraph data from SOHO.
The query is based on the scientific context from the CAMEL paper, which analyzes LASCO C2 data for CME detection.
Here we query the training dataset covering the period January 2011 to October 2011.
Note: Although the full available time range for LASCO C2 on SOHO is "1995/12/08 - present",
we restrict the query as per the paper's training dataset time period.
"""

# Import necessary SunPy modules
from sunpy.net import Fido, attrs as a

def main():
    # Define the time range for the training dataset: January 2011 to October 2011.
    start_time = '2011-01-01'
    end_time = '2011-10-31'
    
    # Define the query attributes:
    # - Source: SOHO
    # - Instrument: LASCO
    # - Detector: C2 (available in VSO interface)
    # We use these parameters because the CAMEL method uses LASCO C2 data.
    query_attrs = [a.Time(start_time, end_time),
                   a.Source('SOHO'),
                   a.Instrument('LASCO'),
                   a.Detector('C2')]
    
    # Perform the query using Fido.search with the specified attributes.
    print("Performing VSO query for LASCO C2 data from SOHO...")
    query_result = Fido.search(*query_attrs)
    
    # Print the query result summary
    print("Query Results:")
    print(query_result)
    
    # The following line would fetch the data based on the query if uncommented.
    # Please note that Fido.fetch downloads the actual data files.
    # Uncomment the line below to perform the download.
    # downloaded_files = Fido.fetch(query_result)
    
if __name__ == '__main__':
    main()
