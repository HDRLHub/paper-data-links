# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses the SunPy VSO client to query solar data for a multi-wavelength analysis of the 
X-class flares observed on 2017 September 6 in active region NOAA 12673 as described in the paper.
The data sources include:
  1. SDO/AIA: Used to study the coronal evolution, flare ribbon dynamics, and plasma heating.
     Available wavelengths include 94 Å, 131 Å, 171 Å, 193 Å, 211 Å, 304 Å, 335 Å, 1600 Å, 1700 Å, and 4500 Å.
  2. SDO/HMI: Provides photospheric intensity and magnetogram observations (LOS magnetic field) for 
     analyzing the evolution of the δ-sunspot configuration.
     
The time interval chosen is from 08:00 UT to 14:00 UT on 2017-09-06 according to the observations in the paper.
"""

# Import required SunPy modules for querying the Virtual Solar Observatory (VSO)
from sunpy.net import Fido, attrs as a

def main():
    # Define the time range of interest (2017 September 6, from 08:00 UT to 14:00 UT)
    time_range = a.Time("2017-09-06T08:00:00", "2017-09-06T14:00:00")
    
    # Query for SDO/AIA data.
    # AIA provides multi-wavelength full-disk images. The available channels in this study include:
    # 94 Å, 131 Å, 171 Å, 193 Å, 211 Å, 304 Å, 335 Å for EUV and 1600 Å, 1700 Å (UV), plus 4500 Å (white light).
    # Here, we query SDO as source and AIA as instrument.
    aia_query = Fido.search(
        time_range,
        a.Source("SDO"),
        a.Instrument("AIA")
        # Additional filters such as wavelength specification can be added if needed.
    )
    
    # Print the AIA query results.
    print("SDO/AIA Query Results:")
    print(aia_query)
    
    # The following command would fetch the AIA data files if uncommented:
    # aia_files = Fido.fetch(aia_query)
    
    # Query for SDO/HMI data.
    # HMI data include high-resolution photospheric observations. In this study, intensity images and
    # LOS magnetograms are used to study the magnetic field evolution in AR NOAA 12673.
    # We perform a query using SDO as source and HMI as instrument.
    hmi_query = Fido.search(
        time_range,
        a.Source("SDO"),
        a.Instrument("HMI")
        # You may add additional filters if specific physical observables (e.g. LOS_magnetic_field or intensity) are desired.
    )
    
    # Print the HMI query results.
    print("\nSDO/HMI Query Results:")
    print(hmi_query)
    
    # The following command would fetch the HMI data files if uncommented:
    # hmi_files = Fido.fetch(hmi_query)

# Execute the main function when running the script.
if __name__ == "__main__":
    main()
