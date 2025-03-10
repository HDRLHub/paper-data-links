# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query SOHO LASCO C3 coronagraph data.
The query focuses on data obtained during the period 2017 September 04 to 2017 September 08,
which corresponds to the time when 'Oumuamua was inside the field-of-view of LASCO C3.
This query is based on the scientific context provided where the "clear" filter images are used.
Note: The VSO interface provided only lists the SOHO LASCO detectors.
In this case, we explicitly query for LASCO with Detector "C3" from the SOHO source.
"""

# Import necessary modules from sunpy.net
from sunpy.net import Fido, attrs as a

def main():
    # Define the observation time range for the query
    start_time = "2017-09-04"
    end_time = "2017-09-08"
    
    # Print the defined time range for clarity
    print("Querying SOHO LASCO C3 data from {} to {} ...".format(start_time, end_time))
    
    # Construct the query using SunPy's Fido and attribute classes.
    # Here, we use:
    # - Time: to specify the start and end of the observation period.
    # - Source: to specify "SOHO".
    # - Instrument: to specify "LASCO".
    # - Detector: to specify "C3".
    query_result = Fido.search(
        a.Time(start_time, end_time),
        a.Source("SOHO"),
        a.Instrument("LASCO"),
        a.Detector("C3")
    )
    
    # Print out the query results summary
    print("Query Results:")
    print(query_result)
    
    # If one wished to download the data, the following command could be used.
    # However, per instructions the fetch command is commented out.
    # Uncomment the next lines if data download is desired.
    
    # download_files = Fido.fetch(query_result)
    # print("Data downloaded:", download_files)

if __name__ == "__main__":
    main()
