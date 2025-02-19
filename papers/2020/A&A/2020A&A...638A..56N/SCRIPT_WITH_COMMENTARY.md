# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the VIRGO/SPM data from the Virtual Solar Observatory (VSO)
for the simulation interval used in the paper (JD 2456700 – 2456850, corresponding to 24 February 2014 – 11 July 2014).

The query is specifically for:
    - Source: SOHO
    - Instrument: VIRGO
    - Detector: SPM

The VIRGO/SPM instrument measures solar brightness in three narrow spectral channels (centered approximately at 402 nm, 500 nm, and 862 nm).
In the VSO interface, these wavelengths are given in Angstroms (4020, 5000, and 8570-8670).

Note: The Fido.fetch command is provided for completeness but is commented out so that the script only prints the query results.
"""

import sunpy.net.vso as vso
import sunpy.net.attrs as a

def main():
    # Define the time range as per the simulation interval for filter comparison.
    # JD 2456700 – 2456850 corresponds approximately to the calendar dates:
    # From 2014-02-24 to 2014-07-11.
    time_range = a.Time("2014-02-24", "2014-07-11")
    
    # Specify the source and instrument attributes.
    source = a.Source("soho")
    instrument = a.Instrument("virgo")
    detector  = a.Detector("SPM")
    
    # Query the VSO for VIRGO/SPM data within the specified time range.
    query_result = vso.Fido.search(time_range, source, instrument, detector)
    
    # Print out the query result
    print("Query Result for SOHO VIRGO/SPM from 2014-02-24 to 2014-07-11:")
    print(query_result)
    
    # To download the data, use the following command:
    # downloaded_files = vso.Fido.fetch(query_result)
    # print("Downloaded files:", downloaded_files)

if __name__ == "__main__":
    main()
