# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates a Sunpy VSO query to download data from SOHO instruments, 
specifically using data from the EIT and LASCO instruments in the year 2002.
The query parameters are chosen based on the context provided. The time range is set 
to cover the entire year 2002, which was critical for the study, and the instruments selected 
are SOHO/EIT (to detect solar disk features in extreme ultraviolet) and SOHO/LASCO (to track CMEs).
Note: The script prints out the query results. Data download commands (Fido.fetch) are commented out.
"""

from sunpy.net import Fido, attrs as a
from datetime import datetime

def main():
    # Define the time range for the queries (the year 2002)
    start_time = '2002-01-01'
    end_time = '2002-12-31'

    # --- Query SOHO/EIT Data ---
    # SOHO/EIT provides EUV images at multiple wavelengths (171, 195, 284, 304 Å) 
    # and was used throughout 2002 for identifying CME onsets.
    eit_query = Fido.search(
        a.Time(start_time, end_time),
        a.Instrument('EIT'),
        a.Source('SOHO')
    )
    print("SOHO/EIT Query Results:")
    print(eit_query)
    
    # Uncomment the following line to fetch SOHO/EIT data after verifying the query output.
    # eit_files = Fido.fetch(eit_query)
    
    # --- Query SOHO/LASCO Data ---
    # LASCO on board SOHO is used to track the evolution of CMEs.
    # Although LASCO data from detectors C1, C2, and C3 are available, 
    # data from C2 and C3 provide continuous coverage into 2002.
    lasco_query = Fido.search(
        a.Time(start_time, end_time),
        a.Instrument('LASCO'),
        a.Source('SOHO')
    )
    print("\nSOHO/LASCO Query Results:")
    print(lasco_query)
    
    # Uncomment the following line to fetch SOHO/LASCO data after verifying the query output.
    # lasco_files = Fido.fetch(lasco_query)

if __name__ == '__main__':
    main()
