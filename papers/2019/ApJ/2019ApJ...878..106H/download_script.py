# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the VSO data archive for SDO/AIA observations during the primary EUV wave event
as described in the paper. We target the data recorded between 15:50 UT and 16:30 UT on 2017-09-10.

Instrument: SDO AIA
Time Range: 2017-09-10T15:50:00 to 2017-09-10T16:30:00

Note:
 - The query is constructed using sunpy.net.Fido with descriptive attributes.
 - The corresponding fetch command is included as a commented-out line.
 - The VSO interface confirms that SDO AIA observations (with appropriate EUV channels) are available.
"""

from sunpy.net import Fido, attrs as a
from sunpy.time import parse_time

def main():
    # Define the time range for the primary EUV wave observation: 15:50 UT to 16:30 UT on 2017-09-10.
    start_time = '2017-09-10T15:50:00'
    end_time = '2017-09-10T16:30:00'

    # Define the instrument and source parameters based on the VSO interface provided.
    # Here we use SDO as the source and AIA as the instrument, which is consistent with the paper’s analysis.
    time_attr = a.Time(start_time, end_time)
    instrument_attr = a.Instrument("AIA")
    source_attr = a.Source("SDO")
    
    # Construct the query using the defined attributes.
    # The query retrieves data with basic selection criteria.
    query_result = Fido.search(time_attr, instrument_attr, source_attr)
    
    # Print the query result summary.
    print("Query Result for SDO/AIA data during the primary EUV wave observation (2017-09-10 15:50 UT to 16:30 UT):")
    print(query_result)
    
    # To download the data uncomment the following line.
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:")
    # print(downloaded_files)

if __name__ == "__main__":
    main()
