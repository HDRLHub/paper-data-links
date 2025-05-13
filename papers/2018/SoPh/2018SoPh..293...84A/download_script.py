# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy’s VSO client to query SDO data from the Atmospheric Imaging Assembly (AIA)
for the period during which NOAA AR 2371 was active (18–22 June 2015). The SDO/AIA instrument
provides high-resolution EUV images in multiple wavelengths. Here we query for observations
with the physical observable "intensity" to reflect the context provided.

Note: The Fido.fetch command is included as a comment and is not executed.
"""

from sunpy.net import Fido, attrs as a

def main():
    # Define the time range from 18 June 2015 to 22 June 2015
    time_range = a.Time("2015-06-18", "2015-06-22")
    
    # Specify the source to be SDO
    source = a.Source("SDO")
    
    # Specify the instrument to be AIA (as available in the VSO interface)
    instrument = a.Instrument("AIA")
    
    # Select the physical observable "intensity" (as per the VSO interface and context)
    physobs = a.Physobs("intensity")
    
    # Construct the query. All parameters are included explicitly for clarity.
    query_result = Fido.search(time_range, source, instrument, physobs)
    
    # Print the query results
    print("Query Results:")
    print(query_result)
    
    # To fetch the data, uncomment the following line:
    # files = Fido.fetch(query_result)
    # print("Fetched data files:", files)

if __name__ == '__main__':
    main()
