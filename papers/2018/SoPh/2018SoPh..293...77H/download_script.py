# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for STEREO-A HI-1 data
using SunPy. The query uses the STEREO_A source, SECCHI instrument, and HI1 detector.
Two separate time ranges are considered:
    1. Nominal operations from 1 April 2007 to 18 August 2014.
    2. Post-superior conjunction phase from 17 November 2015 onward (here we use an example end date).
The VSO interface confirms that data for STEREO_A SECCHI HI1 is available from 2006/11/06 onward.
"""

from sunpy.net import Fido, attrs as a

def query_stereo_hi1_nominal():
    # Define the time range for nominal operations
    time_range = a.Time("2007-04-01", "2014-08-18")
    # Define the query parameters: Source, Instrument, and Detector
    source = a.Source("STEREO_A")
    instrument = a.Instrument("SECCHI")
    detector = a.Detector("HI1")
    
    # Perform the query for nominal operations
    query_results = Fido.search(time_range, source, instrument, detector)
    print("Query Results for STEREO-A HI-1 during Nominal Operations (2007-04-01 to 2014-08-18):")
    print(query_results)
    
    # Uncomment the following line to fetch the data
    # downloaded_files = Fido.fetch(query_results)
    
def query_stereo_hi1_post_superior():
    # Define the time range for the post-superior conjunction phase.
    # Since the data collection is continuous from 17 November 2015 onward,
    # we use an example short period (e.g., until 31 December 2015) for demonstration.
    time_range = a.Time("2015-11-17", "2015-12-31")
    source = a.Source("STEREO_A")
    instrument = a.Instrument("SECCHI")
    detector = a.Detector("HI1")
    
    # Perform the query for the post-superior conjunction phase
    query_results = Fido.search(time_range, source, instrument, detector)
    print("Query Results for STEREO-A HI-1 during Post-Superior Conjunction Phase (2015-11-17 to 2015-12-31):")
    print(query_results)
    
    # Uncomment the following line to fetch the data
    # downloaded_files = Fido.fetch(query_results)

if __name__ == '__main__':
    query_stereo_hi1_nominal()
    query_stereo_hi1_post_superior()
