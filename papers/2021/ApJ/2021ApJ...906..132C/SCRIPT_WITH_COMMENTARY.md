# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses sunpy.net.vso (Virtual Solar Observatory) to query solar observational data.
We perform two separate queries based on the provided context and available VSO interface:

1. Query SDO/AIA for a representative EUV image. We choose the AIA 171 Å channel,
   which is used for contextual imaging of the quiet Sun and coronal structures.
   For the purpose of this query, we select a short time interval on 2015 September 20.
   (Note: Although the paper uses SDO/AIA primarily as a reference image, any short interval
   within the available time range is acceptable.)

2. Query SOHO/LASCO-C2 for white‐light coronagraph data.
   The LASCO-C2 white-light CME observations for 2015 September 20 are reported to run
   from 18:12 UT to 19:12 UT.
   
Note: We explicitly comment out the Fido.fetch calls. The script prints query results.

Requirements:
- sunpy version with sunpy.net.vso module installed.
- Internet access to reach the VSO service (when not in offline mode).
"""

import datetime
from sunpy.net import Fido, attrs as a

def main():
    # -------------------------
    # 1. Query SDO/AIA Data
    # -------------------------
    # We choose a representative 2-minute interval for SDO/AIA around 18:00 UT on 2015-09-20.
    # The selected wavelength is 171 Å (which is available in SDO/AIA as per the VSO interface).
    aia_start = datetime.datetime(2015, 9, 20, 18, 0, 0)
    aia_end   = datetime.datetime(2015, 9, 20, 18, 2, 0)
    # Set instrument attribute to 'AIA'. We also set the wavelength to 171 Å.
    # The physical observable is intensity (which is the default for AIA in our interface).
    aia_query = Fido.search(a.Time(aia_start, aia_end),
                            a.Instrument('AIA'),
                            a.Wavelength(171*u.AA))
    
    # Print out AIA query results.
    print("SDO/AIA Query Results:")
    print(aia_query)

    # Uncomment the following line to fetch the AIA data:
    # aia_files = Fido.fetch(aia_query)
    
    # ---------------------------
    # 2. Query SOHO/LASCO-C2 Data
    # ---------------------------
    # For white-light white-light coronagraph data from LASCO-C2, we use the following time interval:
    # 2015 September 20 from 18:12 UT to 19:12 UT.
    lasco_start = datetime.datetime(2015, 9, 20, 18, 12, 0)
    lasco_end   = datetime.datetime(2015, 9, 20, 19, 12, 0)
    # Set instrument attribute to 'LASCO', and specify the 'C2' detector.
    lasco_query = Fido.search(a.Time(lasco_start, lasco_end),
                              a.Instrument('LASCO'),
                              a.Detector('C2'))
    
    # Print out LASCO-C2 query results.
    print("\nSOHO/LASCO-C2 Query Results:")
    print(lasco_query)
    
    # Uncomment the following line to fetch the LASCO-C2 data:
    # lasco_files = Fido.fetch(lasco_query)

if __name__ == "__main__":
    # Import astropy units here since it is needed for wavelength units
    import astropy.units as u
    main()
