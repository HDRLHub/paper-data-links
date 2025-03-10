# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the Virtual Solar Observatory (VSO)
for data from two instruments that are used in the study:
  1. The Helioseismic Magnetic Imager (HMI) onboard SDO, which provides
     full-disk vector magnetograms used to calculate magnetic polarity inversion
     line properties.
  2. The Large Angle and Spectrometric Coronagraph (LASCO) onboard SOHO, which
     supplies white-light coronagraph images to study CME kinematics.

In this example:
  - For HMI, we query a 24-hour period preceding a hypothetical eruptive event.
    (Example event: 7 March 2012, hence query from 2012-03-06T00:00:00 to 2012-03-07T00:00:00)
  - For LASCO, we query a shorter time window around a CME observation (example:
    event on 15 February 2011 between 01:30:00 and 02:00:00).
    
Note: The Fido.fetch commands are commented out to avoid immediate download.
"""

from sunpy.net import Fido, attrs as a

def main():
    # ----------------------------
    # Query for SDO/HMI Vector Magnetograms
    # ----------------------------
    # Define the start and end times for a 24-hour window preceding the CME-associated flare.
    hmi_start_time = "2012-03-06T00:00:00"
    hmi_end_time   = "2012-03-07T00:00:00"
    
    # Query parameters: SDO as the source, HMI as the instrument, and vector_magnetic_field as the physical observable.
    hmi_query_result = Fido.search(
        a.Time(hmi_start_time, hmi_end_time),
        a.Source('SDO'),
        a.Instrument('HMI'),
        a.Physobs('vector_magnetic_field')
    )
    
    # Print out the query results for HMI data.
    print("HMI Query Results:")
    print(hmi_query_result)
    
    # To download the HMI data, uncomment the following line:
    # hmi_files = Fido.fetch(hmi_query_result)
    
    # ----------------------------
    # Query for SOHO/LASCO White-Light Coronagraph Data
    # ----------------------------
    # Define the start and end times for a CME event observation.
    # Example: For the event on 15 February 2011, choose a time window that covers the CME appearance.
    lasco_start_time = "2011-02-15T01:30:00"
    lasco_end_time   = "2011-02-15T02:00:00"
    
    # Query parameters: SOHO as the source, LASCO as the instrument, using detector 'C2'
    # and 'intensity' as the physical observable (white-light observations).
    lasco_query_result = Fido.search(
        a.Time(lasco_start_time, lasco_end_time),
        a.Source('SOHO'),
        a.Instrument('LASCO'),
        a.Detector('C2'),
        a.Physobs('intensity')
    )
    
    # Print out the query results for LASCO data.
    print("\nLASCO Query Results:")
    print(lasco_query_result)
    
    # To download the LASCO data, uncomment the following line:
    # lasco_files = Fido.fetch(lasco_query_result)

if __name__ == '__main__':
    main()
