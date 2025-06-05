# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client (Fido) to query solar data relevant to the 
plasmoid event observed during the total solar eclipse of 11 July 2010.
We perform three separate queries:
  1. PROBA2/SWAP: EUV images at 174 Å covering the period from 06:24 UT to 23:57 UT on 11 July 2010.
  2. SDO/AIA: High-resolution full-disk EUV images in the 171 Å channel from 10 July 2010 (early motion).
  3. SOHO/LASCO (C2): White‐light coronagraph images capturing coronal flows after 12 UT on 11 July 2010.

Note:
 - We only print the query results.
 - The Fido.fetch calls are commented out since we are not actually downloading any data.
 - The queries use only the required time range and instrument information as specified.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs as a
import astropy.units as u

def main():
    # ------------------------------
    # Query 1: PROBA2/SWAP (EUV at 174 Å)
    # ------------------------------
    # Data collection details:
    # Time Range: 11 July 2010, 06:24 UT – 11 July 2010, 23:57 UT
    # Instrument: SWAP on board PROBA2 operating near 174 Å.
    swap_time_start = "2010-07-11T06:24:00"
    swap_time_end   = "2010-07-11T23:57:00"
    
    # Build the query for PROBA2 SWAP
    # We specify the source, instrument, detector, and wavelength (174 Å)
    swap_query = Fido.search(
        a.Time(swap_time_start, swap_time_end),
        a.Source("PROBA2"),
        a.Instrument("SWAP"),
        a.Detector("SWAP"),
        a.Wavelength(174*u.AA, 174*u.AA)
    )
    
    # Print the query results for PROBA2/SWAP data
    print("Query Results for PROBA2/SWAP (174 Å):")
    print(swap_query)
    
    # Uncomment the next line to fetch the PROBA2/SWAP data
    # swap_files = Fido.fetch(swap_query)
    
    # ------------------------------
    # Query 2: SDO/AIA (EUV at 171 Å)
    # ------------------------------
    # Data collection details:
    # Time Range: 10 July 2010, starting at 12:00 UT (to capture material in motion)
    # Instrument: AIA on board SDO imaging in the 171 Å channel.
    aia_time_start = "2010-07-10T12:00:00"
    aia_time_end   = "2010-07-10T12:30:00"
    
    # Build the query for SDO/AIA 171 Å
    # We use a wavelength range that brackets 171 Å (using a narrow range for specificity)
    aia_query = Fido.search(
        a.Time(aia_time_start, aia_time_end),
        a.Source("SDO"),
        a.Instrument("AIA"),
        a.Wavelength(171*u.AA, 171*u.AA)
    )
    
    # Print the query results for SDO/AIA data
    print("\nQuery Results for SDO/AIA (171 Å):")
    print(aia_query)
    
    # Uncomment the next line to fetch the SDO/AIA data
    # aia_files = Fido.fetch(aia_query)
    
    # ------------------------------
    # Query 3: SOHO/LASCO C2 (White-light coronagraph)
    # ------------------------------
    # Data collection details:
    # Time Range: 11 July 2010, 12:00 UT – 11 July 2010, 19:00 UT
    # Instrument: LASCO onboard SOHO with Detector 'C2' capturing white-light coronal images.
    lasco_time_start = "2010-07-11T12:00:00"
    lasco_time_end   = "2010-07-11T19:00:00"
    
    # Build the query for SOHO LASCO C2 data.
    # No wavelength is specified, since LASCO observes in white light.
    lasco_query = Fido.search(
        a.Time(lasco_time_start, lasco_time_end),
        a.Source("SOHO"),
        a.Instrument("LASCO"),
        a.Detector("C2")
    )
    
    # Print the query results for SOHO/LASCO C2 data
    print("\nQuery Results for SOHO/LASCO C2 (White-light):")
    print(lasco_query)
    
    # Uncomment the next line to fetch the SOHO/LASCO data
    # lasco_files = Fido.fetch(lasco_query)
    
if __name__ == "__main__":
    main()
