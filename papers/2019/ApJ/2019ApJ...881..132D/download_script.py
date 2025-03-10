# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query solar data relevant to the study of a twin CME event.
Two queries are constructed:
  1. An SDO/AIA query in the 304 Å channel from 03:30 UT to 04:10 UT on 2015 August 23,
     corresponding to the filament activation and eruption phase.
  2. An SDO/HMI query for line-of-sight magnetograms from 02:58 UT to 07:58 UT on 2015 August 23,
     corresponding to the magnetic flux evolution during the event.
Note: The Fido.fetch commands are provided in the code as comments.
"""

# Import necessary modules from sunpy and astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

def query_aia_data():
    # Define the observation time range for AIA (filament activation and eruption phase)
    time_start = "2015-08-23T03:30:00"
    time_end   = "2015-08-23T04:10:00"

    # Construct the query for SDO/AIA data in the 304 Å channel;
    # The AIA instrument on board SDO provides full-disk solar images in multiple wavelengths.
    # Here we query for AIA 304 Å images that capture the cool plasma evolution of the filament.
    aia_query = Fido.search(
        a.Time(time_start, time_end),
        a.Source("SDO"),
        a.Instrument("AIA"),
        a.Wavelength(304*u.AA)
    )

    # Print the AIA query results
    print("AIA Query Results:")
    print(aia_query)

    # Uncomment the line below to download the data (if desired)
    # aia_files = Fido.fetch(aia_query)

def query_hmi_data():
    # Define the observation time range for HMI (magnetic flux evolution)
    time_start = "2015-08-23T02:58:00"
    time_end   = "2015-08-23T07:58:00"

    # Construct the query for SDO/HMI data for line-of-sight magnetograms.
    # HMI provides observations of the photospheric magnetic field which are critical for studying flux cancellation.
    hmi_query = Fido.search(
        a.Time(time_start, time_end),
        a.Source("SDO"),
        a.Instrument("HMI"),
        a.Physobs("LOS_magnetic_field")
    )

    # Print the HMI query results
    print("HMI Query Results:")
    print(hmi_query)

    # Uncomment the line below to download the data (if desired)
    # hmi_files = Fido.fetch(hmi_query)

def main():
    # Query AIA and HMI data based on the scientific observation details provided.
    query_aia_data()
    query_hmi_data()

if __name__ == '__main__':
    main()
