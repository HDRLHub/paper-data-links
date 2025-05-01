# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use SunPy's VSO interface to query data from the SOHO/GOLF instrument.
The query is built with the time range available from the VSO interface (from 1996-01-01 to present)
and specifies the instrument "GOLF" on board SOHO, as described in the provided context.
Note: The query result is printed out, and the actual data download (Fido.fetch) call is commented out.
"""

from datetime import datetime
from sunpy.net import Fido, attrs as a

def main():
    # Define the time range for the query:
    # Start time from the vso_interface (1996-01-01) and end time as the current date.
    start_time = '1996-01-01'
    end_time = datetime.now().strftime('%Y-%m-%d')  # Present date
    
    # Construct the query for the SOHO/GOLF instrument.
    # From the vso_interface:
    #   Source: "SOHO"
    #   Instrument: "GOLF"
    query = Fido.search(
        a.Time(start_time, end_time),
        a.Source('SOHO'),
        a.Instrument('GOLF')
    )
    
    # Print the search results to review available data.
    print("Query Results from SOHO/GOLF:")
    print(query)
    
    # Uncomment the following line to download the data if desired.
    # download_files = Fido.fetch(query)
    # print("Download completed. Files saved:", download_files)

if __name__ == "__main__":
    main()
