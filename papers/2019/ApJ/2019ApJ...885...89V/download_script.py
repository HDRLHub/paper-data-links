# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query solar observation data relevant to the study 
of prominence eruptions, as described in the paper.

We will perform explicit queries for:
1. SDO/AIA observations in the 304 Å channel for two representative events:
   - Event P1: 07-Mar-2011 from 18:49 UT to 20:58 UT.
   - Event P3: 12-Jun-2011 from 12:30 UT to 13:34 UT.
2. STEREO-A SECCHI/EUVI observations in the 304 Å channel for Event P1 
   (which are used in conjunction with AIA for stereoscopic measurements).
   
Note:
- The VSO interface is used as provided.
- The Fido.fetch commands are commented out as per instructions.
- Additional query parameters (e.g., wavelength units) are set in accordance with the available VSO data.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

def query_sdo_aia_event(time_start, time_end, wavelength):
    # Query for SDO/AIA data in the specified time range and wavelength.
    # SDO/AIA offers the 304 Å channel among other wavelengths.
    print("Querying SDO/AIA data for event between {} and {} at wavelength {} ...".format(time_start, time_end, wavelength))
    
    # Build the query
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Instrument('AIA'),
        a.Source('SDO'),
        a.Wavelength(wavelength * u.AA)
    )
    
    print(query_result)
    # Uncomment the next line to fetch the data
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:", downloaded_files)

def query_stereo_euvi_event(time_start, time_end, wavelength):
    # Query for STEREO-A SECCHI EUVI data in the specified time range and wavelength.
    print("Querying STEREO-A SECCHI/EUVI data for event between {} and {} at wavelength {} ...".format(time_start, time_end, wavelength))
    
    # Build the query
    # For STEREO-A data, we set the instrument to 'SECCHI' and use the 'EUVI' detector.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Instrument('SECCHI'),
        a.Source('STEREO_A'),
        a.Detector('EUVI'),
        a.Wavelength(wavelength * u.AA)
    )
    
    print(query_result)
    # Uncomment the next line to fetch the data
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:", downloaded_files)

def main():
    # Event P1: SDO/AIA 304 Å observations (07-Mar-2011)
    event1_start = "2011-03-07T18:49:00"
    event1_end   = "2011-03-07T20:58:00"
    wavelength_304 = 304.0  # in Angstroms
    
    query_sdo_aia_event(event1_start, event1_end, wavelength_304)

    # Event P3: SDO/AIA 304 Å observations (12-Jun-2011)
    event3_start = "2011-06-12T12:30:00"
    event3_end   = "2011-06-12T13:34:00"
    
    query_sdo_aia_event(event3_start, event3_end, wavelength_304)
    
    # STEREO-A SECCHI/EUVI for Event P1 (simultaneous with AIA P1)
    query_stereo_euvi_event(event1_start, event1_end, wavelength_304)

if __name__ == '__main__':
    main()
