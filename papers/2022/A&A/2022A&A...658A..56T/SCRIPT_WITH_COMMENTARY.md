# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO interface to query data for two different STEREO-B SECCHI instruments.
One query fetches EUVI (Extreme UV Imager) data corresponding to the observation of the eruptive prominence on 21 September 2009.
The other query fetches COR1 data corresponding to the detection of the second CME on 22 September 2009.
Note: In both cases, only the time range and instrument/detector have been used, as instructed.
Fido.fetch commands are commented out.
"""

# Import necessary modules from sunpy and astropy
from sunpy.net import Fido, attrs as a
from astropy import units as u

def main():
    # ----------------------------------------------
    # Query 1: STEREO-B SECCHI/EUVI: Eruptive prominence observation
    # Data Collection Period: 21 September 2009 from 16:36 UT to 19:37 UT
    # Wavelength: 304 Å (Extreme UV)
    # Source: STEREO_B, Instrument: SECCHI, Detector: EUVI
    # ----------------------------------------------
    time_start_euvi = '2009-09-21T16:36:00'
    time_end_euvi = '2009-09-21T19:37:00'
    # Build the query attributes
    query_euvi = Fido.search(
        a.Time(time_start_euvi, time_end_euvi),
        a.Instrument('SECCHI'),
        a.Detector('EUVI'),
        a.Source('STEREO_B'),
        a.Wavelength(304*u.AA, 304*u.AA)
    )
    # Print the query results for EUVI data
    print("EUVI Query Results:")
    print(query_euvi)

    # Fetching of data is commented out as per instructions.
    # data_euvi = Fido.fetch(query_euvi)
    # print("Fetched EUVI Data:")
    # print(data_euvi)

    # ----------------------------------------------
    # Query 2: STEREO-B SECCHI/COR1: Coronagraph observation of CME2 onset
    # Data Collection Time: Around 04:05 UT on 22 September 2009 (using a short interval)
    # No wavelength filter applied (white-light observation typical for coronagraphs)
    # Source: STEREO_B, Instrument: SECCHI, Detector: COR1
    # ----------------------------------------------
    # Here we query a short window (04:00 UT to 04:10 UT) to capture the event.
    time_start_cor1 = '2009-09-22T04:00:00'
    time_end_cor1 = '2009-09-22T04:10:00'
    # Build the query attributes for COR1 data
    query_cor1 = Fido.search(
        a.Time(time_start_cor1, time_end_cor1),
        a.Instrument('SECCHI'),
        a.Detector('COR1'),
        a.Source('STEREO_B')
    )
    # Print the query results for COR1 data
    print("\nCOR1 Query Results:")
    print(query_cor1)

    # Fetching of data is commented out as per instructions.
    # data_cor1 = Fido.fetch(query_cor1)
    # print("Fetched COR1 Data:")
    # print(data_cor1)

if __name__ == "__main__":
    main()
