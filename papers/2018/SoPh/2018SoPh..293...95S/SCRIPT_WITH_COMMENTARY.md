# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs a SunPy VSO query to download the solar global velocity observations
from the GOLF instrument onboard SOHO. The query is based on the provided VSO interface
and context, which details a 16.5-year time series analysis using GOLF data.
"""

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a

def main():
    # Define the time range for the GOLF data.
    # Although the paper mentions a 16.5-year long time series,
    # here we use an example time range starting from the available 
    # start time (1996-01-01) up to a date that approximates the 16.5 years.
    start_time = "1996-01-01"
    end_time = "2012-07-01"  # Approximately 16.5 years later
    
    # Create the query attributes from the VSO interface for the GOLF instrument.
    # According to the interface, the GOLF data is from SOHO with the Fsmain detector
    # and LOS_velocity observable.
    time_attr = a.Time(start_time, end_time)
    instrument_attr = a.Instrument("GOLF")
    source_attr = a.Source("SOHO")
    detector_attr = a.Detector("Fsmain")
    physobs_attr = a.Physobs("LOS_velocity")
    
    # Construct the search query with all the attributes
    # This query will search for data matching the time range and instrument specifics.
    query_result = Fido.search(time_attr, source_attr, instrument_attr, detector_attr, physobs_attr)
    
    # Print out the query result details; this will show what data files match the criteria.
    print("Query Result for GOLF instrument data:")
    print(query_result)
    
    # To actually download the data, you could use Fido.fetch.
    # The following command is provided as a guideline and is commented out.
    # Uncomment it to run the download.
    #
    # downloaded_files = Fido.fetch(query_result)
    # print("Data successfully downloaded:")
    # print(downloaded_files)

if __name__ == "__main__":
    main()
