# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query solar data that corresponds to observations used in the study.
It is based on the following instruments and time ranges as described in the paper:

1. SDO/AIA: EUV imaging at 193 Å (capturing the coronal magnetic configuration and filament details)
   - Query Time: 04:00 UT on 2018 August 20
   - Note: Although 193 Å is not explicitly listed in the available wavelengths,
           it lies within the 191.0-195.0 Å range available for AIA.

2. SDO/HMI: Photospheric magnetograms (used to map the filament channel)
   - Query Time: 08:00 UT on 2018 August 20

3. SOHO/LASCO (C2): White-light coronagraph imaging (observing the CME onset)
   - Query Time: 21:00 UT on 2018 August 20
   - Detector used: C2

The script creates separate, explicit queries for each dataset.
The Fido.fetch commands are provided as comments so that retrieval may be enabled if desired.
"""

# Import necessary modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

def query_sdo_aia():
    # Query details for SDO/AIA data at roughly 04:00 UT on 2018-08-20 in the 193 Å channel.
    # The wavelength 193 Å falls within the "191.0-195.0" range available.
    time_start = '2018-08-20T04:00:00'
    time_end = '2018-08-20T04:00:30'
    
    # Set up the query for SDO AIA with the specific wavelength.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Source('SDO'),
        a.Instrument('AIA'),
        a.Wavelength(193*u.AA)
    )
    print("SDO/AIA Query Result:")
    print(query_result)
    
    # Uncomment the following line to fetch the data:
    # downloaded_files = Fido.fetch(query_result)
    
def query_sdo_hmi():
    # Query details for SDO/HMI magnetogram data at around 08:00 UT on 2018-08-20.
    time_start = '2018-08-20T08:00:00'
    time_end = '2018-08-20T08:00:30'
    
    # Set up the query for SDO HMI magnetogram data.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Source('SDO'),
        a.Instrument('HMI')
    )
    print("\nSDO/HMI Query Result:")
    print(query_result)
    
    # Uncomment the following line to fetch the data:
    # downloaded_files = Fido.fetch(query_result)
    
def query_soho_lasco_c2():
    # Query details for SOHO LASCO C2 coronagraph data at around 21:00 UT on 2018-08-20.
    time_start = '2018-08-20T21:00:00'
    time_end = '2018-08-20T21:01:00'
    
    # Set up the query for SOHO LASCO data using the C2 detector.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Source('SOHO'),
        a.Instrument('LASCO'),
        a.Detector('C2')
    )
    print("\nSOHO/LASCO (C2) Query Result:")
    print(query_result)
    
    # Uncomment the following line to fetch the data:
    # downloaded_files = Fido.fetch(query_result)

def main():
    # Execute the queries for each instrument.
    query_sdo_aia()
    query_sdo_hmi()
    query_soho_lasco_c2()

if __name__ == "__main__":
    main()
