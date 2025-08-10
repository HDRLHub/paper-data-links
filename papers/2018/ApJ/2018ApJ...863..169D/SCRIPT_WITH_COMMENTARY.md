# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO interface to query data from the SDO instruments – AIA and HMI.
The observations are selected for a 12‐hour interval, typically starting 30 minutes before the flare.
For this example, we use the time interval from "2012-05-12T00:00:00" to "2012-05-12T12:00:00".
We query:
  1) SDO/AIA data in the extreme‐ultraviolet (EUV) channel at 211 Å,
     which is prominently used in statistical studies of coronal dimming.
  2) SDO/HMI data measuring the line-of-sight (LOS) magnetic field to study magnetic flux properties.
The Fido.fetch commands are provided but commented out.
Modify the time interval as appropriate for your event of interest.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

def main():
    # Define the 12-hour time range (example times that fall within instrument availability)
    start_time = "2012-05-12T00:00:00"  # 30 minutes before the associated flare would be chosen here
    end_time = "2012-05-12T12:00:00"    # Total duration of 12 hours

    # ----- Querying SDO/AIA Data -----
    # For the study of coronal dimming, we select the AIA 211 Å channel since it is used predominantly.
    # The query uses the time range, the instrument (AIA), and specifies the wavelength of 211 Å.
    query_aia = Fido.search(
        a.Time(start_time, end_time),
        a.Source('SDO'),
        a.Instrument('AIA'),
        a.Wavelength(211 * u.AA)
    )
    # Print the query results for SDO/AIA
    print("SDO/AIA Query Results:")
    print(query_aia)
    # To download the data, uncomment the following line:
    # downloaded_aia = Fido.fetch(query_aia)
    
    # ----- Querying SDO/HMI Data -----
    # To study the magnetic properties of the dimming regions, we query HMI data with line-of-sight (LOS)
    # magnetic field measurements which have a cadence of 720 seconds.
    query_hmi = Fido.search(
        a.Time(start_time, end_time),
        a.Source('SDO'),
        a.Instrument('HMI'),
        a.Physobs('LOS_magnetic_field')
    )
    # Print the query results for SDO/HMI
    print("\nSDO/HMI Query Results:")
    print(query_hmi)
    # To download the data, uncomment the following line:
    # downloaded_hmi = Fido.fetch(query_hmi)

if __name__ == "__main__":
    main()
