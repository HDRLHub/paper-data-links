# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the SOHO/MDI instrument data available via the Virtual Solar Observatory (VSO).
According to the context, we wish to obtain a snapshot of the SOHO/MDI LOS magnetic field observations 
on 14 April 2010 at around 11:00 UT. 

Note:
- Although the paper also refers to Hinode data and simulation results, only SOHO/MDI data are available 
  in the provided VSO interface.
- We define a one‐minute time interval (from 11:00 UT to 11:01 UT) representing the snapshot.
- The query specifies source, instrument and the observable (LOS_magnetic_field) for clarity.
- The Fido.fetch command is provided but commented out to avoid immediate downloading.
  
Make sure you have SunPy installed (pip install sunpy) and an active internet connection to run the query.
"""

from sunpy.net import Fido, attrs

def main():
    # Define the time range for the observation: 14 April 2010 from 11:00:00 to 11:01:00 UT
    time_range = attrs.Time("2010-04-14 11:00:00", "2010-04-14 11:01:00")
    
    # Define the source as SOHO and the instrument as MDI (Michelson Doppler Imager)
    source = attrs.Source("SOHO")
    instrument = attrs.Instrument("MDI")
    
    # The physical observable is the longitudinal magnetic field
    physobs = attrs.Physobs("LOS_magnetic_field")
    
    # Construct the full query with the specified time range and instrument parameters.
    # This query will look for SOHO/MDI magnetogram data.
    result = Fido.search(time_range, source, instrument, physobs)
    
    # Print out the query results.
    print("Query Results from VSO for SOHO/MDI LOS Magnetic Field Data:")
    print(result)
    
    # To download the data, uncomment the following lines:
    # downloaded_files = Fido.fetch(result)
    # print("Downloaded Files:")
    # print(downloaded_files)

if __name__ == "__main__":
    main()
