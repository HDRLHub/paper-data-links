# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client to query PROBA2/LYRA data corresponding to the solar flare event on 6 September 2017.
The study focuses on two LYRA channels:
    - Channel 1 (Lyα): wavelength range 120.0 - 123.0 nm
    - Channel 2 (MUV Balmer continuum): wavelength range 190.0 - 222.0 nm
The time range for the observations is from 11:55:07 UT to 12:03:27 UT.
Note: The script shows the query results but the actual download call (Fido.fetch) is commented out.
"""

# Import required packages from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

def main():
    # Define the observation time interval
    time_start = "2017-09-06T11:55:07"
    time_end = "2017-09-06T12:03:27"
    
    # Query 1: PROBA2/LYRA Channel 1 (Lyα) with wavelength range 120.0 - 123.0 nm
    query_lyalpha = Fido.search(
        a.Time(time_start, time_end),
        a.Instrument("LYRA"),
        a.Source("PROBA2"),
        a.Wavelength(120.0 * u.nm, 123.0 * u.nm)
    )
    
    # Print out the search result for LYRA Channel 1 (Lyα)
    print("=== Query Results for PROBA2/LYRA Channel 1 (Lyα; 120.0-123.0 nm) ===")
    print(query_lyalpha)
    
    # Uncomment the following line to fetch the data for Channel 1
    # downloaded_files_lyalpha = Fido.fetch(query_lyalpha)
    
    # Query 2: PROBA2/LYRA Channel 2 (MUV Balmer Continuum) with wavelength range 190.0 - 222.0 nm
    query_muv = Fido.search(
        a.Time(time_start, time_end),
        a.Instrument("LYRA"),
        a.Source("PROBA2"),
        a.Wavelength(190.0 * u.nm, 222.0 * u.nm)
    )
    
    # Print out the search result for LYRA Channel 2 (MUV)
    print("\n=== Query Results for PROBA2/LYRA Channel 2 (MUV; 190.0-222.0 nm) ===")
    print(query_muv)
    
    # Uncomment the following line to fetch the data for Channel 2
    # downloaded_files_muv = Fido.fetch(query_muv)

if __name__ == "__main__":
    main()
