# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script queries the SOHO/LASCO C3 data from the Virtual Solar Observatory (VSO).
Based on the context from the paper, the SOHO/LASCO C3 remote sensing observations 
(from 1999 to 2010) are used to support studies of the Parker spiral and gardenhose phenomena.
The VSO interface confirms that SOHO/LASCO C3 data are available from 1995/12/08 to present.
Here, we use a time range (1999-01-01 to 2010-12-31) to match the period of interest.
"""

# Import necessary modules from sunpy
import sunpy.net.vso as vso
from sunpy.net import attrs as a

def main():
    # Create a VSO client to connect to the Virtual Solar Observatory
    client = vso.VSOClient()

    # Define the query parameters:
    # - Time range: from January 1, 1999 to December 31, 2010 (as per the context for SOHO/LASCO C3 movies)
    # - Instrument: LASCO (with detector "C3")
    # - Source: SOHO
    time_range = a.Time("1999-01-01", "2010-12-31")
    source = a.Source("SOHO")
    instrument = a.Instrument("LASCO")
    detector = a.Detector("C3")

    # Build the query using the defined attributes
    query_result = client.search(time_range, source, instrument, detector)

    # Print the query results to inspect what data are available for download
    print("Query Result:")
    print(query_result)

    # To fetch the data, remove the comment from the following line:
    # files = client.fetch(query_result)

if __name__ == "__main__":
    main()
