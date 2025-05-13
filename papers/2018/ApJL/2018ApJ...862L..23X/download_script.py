# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the Virtual Solar Observatory (VSO) for magnetogram data 
from two spaceborne instruments: the Helioseismic and Magnetic Imager (HMI) onboard SDO and 
the Michelson Doppler Imager (MDI) onboard SOHO. 

The queries reflect the instrumentation details mentioned in the study, where HMI is used 
for modern vector magnetic field measurements (available from 2010 March 29 to present) and 
MDI provides line-of-sight (LOS) magnetic field data (available roughly from 1996 to 2011).

Note: The Fido.fetch commands are commented out to avoid actual data downloads.
"""

# Import necessary modules from sunpy
from sunpy.net import vso
from sunpy.net import attrs as a

def main():
    # Create a VSO client instance.
    client = vso.VSOClient()

    # Query 1: HMI data (vector magnetic field) from SDO.
    # We choose a sample time interval within the available range (e.g., 2015-06-01 to 2015-06-02).
    # The query explicitly sets the time, source, instrument, and physical observable (vector magnetic field).
    hmi_query = client.search(
        a.Time("2015-06-01", "2015-06-02"),
        a.Source("SDO"),
        a.Instrument("HMI"),
        a.Physobs("vector_magnetic_field")
    )
    # Print the results for the HMI query.
    print("SDO/HMI vector magnetic field query results:")
    print(hmi_query)

    # To download the HMI data, uncomment the following line:
    # hmi_files = client.fetch(hmi_query)

    # Query 2: MDI data (LOS magnetic field) from SOHO.
    # We select a sample interval within the MDI available period (e.g., 2005-06-01 to 2005-06-02).
    # The query uses the instrument "MDI" from the source "SOHO" and requests LOS magnetic field measurements.
    mdi_query = client.search(
        a.Time("2005-06-01", "2005-06-02"),
        a.Source("SOHO"),
        a.Instrument("MDI"),
        a.Physobs("LOS_magnetic_field")
    )
    # Print the results for the MDI query.
    print("\nSOHO/MDI LOS magnetic field query results:")
    print(mdi_query)

    # To download the MDI data, uncomment the following line:
    # mdi_files = client.fetch(mdi_query)

if __name__ == "__main__":
    main()
