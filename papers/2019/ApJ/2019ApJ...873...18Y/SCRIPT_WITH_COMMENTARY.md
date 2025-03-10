# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses the SunPy VSO client to query SOHO/MDI data that have been widely used 
in helioseismic studies such as comparing the solar sound-speed and density profiles.
In the context of the referenced paper, the Michelson Doppler Imager (MDI) on board SOHO 
provides Doppler measurements (LOS_velocity) which are employed to infer solar interior properties.
The query uses the available time range provided in the VSO interface for the MDI instrument.
"""

# Import necessary SunPy modules
from sunpy.net import Fido, attrs as a

def main():
    # Define the time range based on the available full time range for MDI LOS_velocity
    # For MDI LOS_velocity, the available range is from 1996/03/03 to 2011/04/12.
    start_time = "1996-03-03T00:00:00"
    end_time = "2011-04-12T23:59:59"

    # Construct the query using the SunPy VSO client with explicit parameters:
    # a.Time: Time range of observation
    # a.Instrument: "MDI" (Michelson Doppler Imager), as referenced in the paper.
    # a.Source: "SOHO", since MDI is on board the SOHO spacecraft.
    # a.Detector: "MDI", as specified in the VSO interface.
    # a.Physobs: "LOS_velocity" to retrieve the velocity measurements used in helioseismic analysis.
    query_result = Fido.search(
        a.Time(start_time, end_time),
        a.Instrument("MDI"),
        a.Source("SOHO"),
        a.Detector("MDI"),
        a.Physobs("LOS_velocity")
    )

    # Print out the details of the query results (file list, metadata, etc.)
    print("Query Results:")
    print(query_result)

    # To fetch data based on the query, uncomment the following lines:
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:")
    # print(downloaded_files)

if __name__ == "__main__":
    main()
