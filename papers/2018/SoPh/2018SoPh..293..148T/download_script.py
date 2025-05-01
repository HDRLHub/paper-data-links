# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query several instruments from the Virtual Solar Observatory.
The queries are based on event times and instruments used in the study of DH type IV radio bursts,
EUV waves, and white-light CMEs as described in the provided context.

The following queries are implemented:
1. STEREO-A/WAVES: Query for a DH type IV burst event observed on 4 June 2011 from 07:12 UT to 08:00 UT.
2. STEREO-B/WAVES: Query for a DH type IV burst event observed on 22 September 2011 from 11:10 UT to 12:15 UT.
3. SDO/AIA: Query for EUV imaging data associated with the 27 January 2012 event from 18:30 UT to 19:30 UT.
4. SOHO/LASCO (Detector C2): Query for white-light coronagraph data for the 4 June 2011 event from 06:48 UT to 07:30 UT.
Note: We are only using the time range and instrument (and detector where applicable) as required.
  
The actual data fetch commands (Fido.fetch) are provided but commented out, as per instructions.
"""

from sunpy.net import Fido, attrs as a

def query_stereo_a_waves():
    # Query for STEREO-A/WAVES data (DH type IV event on 4 June 2011: 07:12 UT to 08:00 UT)
    stereo_a_query = Fido.search(
        a.Time("2011-06-04T07:12:00", "2011-06-04T08:00:00"),
        a.Source("STEREO_A"),
        a.Instrument("SWAVES")
    )
    print("STEREO-A/WAVES Query Results:")
    print(stereo_a_query)
    # To download the data, uncomment the line below:
    # files_stereo_a = Fido.fetch(stereo_a_query)
    
def query_stereo_b_waves():
    # Query for STEREO-B/WAVES data (DH type IV event on 22 September 2011: 11:10 UT to 12:15 UT)
    stereo_b_query = Fido.search(
        a.Time("2011-09-22T11:10:00", "2011-09-22T12:15:00"),
        a.Source("STEREO_B"),
        a.Instrument("SWAVES")
    )
    print("STEREO-B/WAVES Query Results:")
    print(stereo_b_query)
    # To download the data, uncomment the line below:
    # files_stereo_b = Fido.fetch(stereo_b_query)

def query_sdo_aia():
    # Query for SDO/AIA EUV imaging data (27 January 2012 event: 18:30 UT to 19:30 UT)
    sdo_aia_query = Fido.search(
        a.Time("2012-01-27T18:30:00", "2012-01-27T19:30:00"),
        a.Source("SDO"),
        a.Instrument("AIA")
    )
    print("SDO/AIA Query Results:")
    print(sdo_aia_query)
    # To download the data, uncomment the line below:
    # files_sdo_aia = Fido.fetch(sdo_aia_query)

def query_soho_lasco():
    # Query for SOHO/LASCO white-light coronagraph data.
    # Using Detector 'C2' for the 4 June 2011 event from 06:48 UT to 07:30 UT.
    soho_lasco_query = Fido.search(
        a.Time("2011-06-04T06:48:00", "2011-06-04T07:30:00"),
        a.Source("SOHO"),
        a.Instrument("LASCO"),
        a.Detector("C2")
    )
    print("SOHO/LASCO (C2) Query Results:")
    print(soho_lasco_query)
    # To download the data, uncomment the line below:
    # files_soho_lasco = Fido.fetch(soho_lasco_query)

def main():
    print("Starting VSO queries based on the scientific instrumentation context:\n")
    query_stereo_a_waves()
    print("\n-----------------------------------\n")
    query_stereo_b_waves()
    print("\n-----------------------------------\n")
    query_sdo_aia()
    print("\n-----------------------------------\n")
    query_soho_lasco()
    print("\nQuerying completed. Uncomment the Fido.fetch lines to download data.")

if __name__ == "__main__":
    main()
