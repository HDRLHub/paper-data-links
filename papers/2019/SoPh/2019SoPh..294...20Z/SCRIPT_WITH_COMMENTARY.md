# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query solar data corresponding
to the observational periods and instruments described in the paper.
The queries are constructed using only the required values:
- Time range
- Instrument

In the provided VSO interface, the available instruments include:
    • SDO/AIA
    • SOHO/CDS
    • SOHO/EIT
    • SOHO/SUMER

The script creates separate queries for each instrument as follows:

1. SDO/AIA: Querying a north polar macrospicule observation on 3 August 2010 in the 304 Å channel.
2. SOHO/CDS: Querying observations in the extended session from 9 April 1996 to 4 April 1997.
3. SOHO/EIT: Querying the detection of a giant macrospicule on 15 July 1999.
4. SOHO/SUMER: Querying a coordinated observation (using a representative date) from 02:36 UT to 02:46 UT.

Note:
The Fido.fetch commands are provided as comments so that no downloads are initiated.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

def query_sdo_aia():
    # Query for SDO/AIA using the 304 Å channel on 3 August 2010.
    # Available wavelengths for AIA in the VSO interface include 304 Å.
    time_range = a.Time("2010-08-03T00:00:00", "2010-08-03T23:59:59")
    instrument = a.Instrument("AIA")
    wavelength = a.Wavelength(300*u.AA, 310*u.AA)  # narrow band around 304 Å
    query_result = Fido.search(time_range, instrument, wavelength)
    print("SDO/AIA query result:")
    print(query_result)
    # Uncomment the following line to download the data:
    # downloaded_files = Fido.fetch(query_result)
    print("\n")

def query_soho_cds():
    # Query for SOHO/CDS using the GIS detector between 9 April 1996 and 4 April 1997.
    time_range = a.Time("1996-04-09T00:00:00", "1997-04-04T23:59:59")
    instrument = a.Instrument("CDS")
    detector = a.Detector("GIS")
    query_result = Fido.search(time_range, instrument, detector)
    print("SOHO/CDS query result:")
    print(query_result)
    # Uncomment the following line to download the data:
    # downloaded_files = Fido.fetch(query_result)
    print("\n")

def query_soho_eit():
    # Query for SOHO/EIT for the macrospicule limb imaging observation on 15 July 1999.
    time_range = a.Time("1999-07-15T00:00:00", "1999-07-15T23:59:59")
    instrument = a.Instrument("EIT")
    detector = a.Detector("EIT")
    query_result = Fido.search(time_range, instrument, detector)
    print("SOHO/EIT query result:")
    print(query_result)
    # Uncomment the following line to download the data:
    # downloaded_files = Fido.fetch(query_result)
    print("\n")

def query_soho_sumer():
    # Query for SOHO/SUMER for coordinated spectroscopic observations,
    # using a representative observation interval from 02:36 UT to 02:46 UT on 1 January 2007.
    time_range = a.Time("2007-01-01T02:36:00", "2007-01-01T02:46:00")
    instrument = a.Instrument("SUMER")
    detector = a.Detector("A, B, RSC")  # as provided in the VSO interface
    query_result = Fido.search(time_range, instrument, detector)
    print("SOHO/SUMER query result:")
    print(query_result)
    # Uncomment the following line to download the data:
    # downloaded_files = Fido.fetch(query_result)
    print("\n")

if __name__ == '__main__':
    print("Starting VSO queries based on the provided context and interface.\n")
    query_sdo_aia()
    query_soho_cds()
    query_soho_eit()
    query_soho_sumer()
    print("All queries complete.")
