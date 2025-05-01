# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query solar data from the Virtual Solar Observatory (VSO)
using the SunPy Fido interface. It constructs separate queries for different instruments,
based on the observational periods and contexts described in the paper.

The instruments and corresponding observations queried are:
1. UVCS (Ultraviolet Coronagraph Spectrometer) for coronal UV spectroscopy during 
   August 1, 1996 – September 2, 1996.
2. EIT (Extreme ultraviolet Imaging Telescope) for EUV disk imaging (Fe XII 195 Å) 
   during August 30, 1996 – September 2, 1996.
3. LASCO C2 (Coronagraph) for white-light corona imaging at the east limb during 
   August 30, 1996 – September 2, 1996.
4. SUMER (Solar Ultraviolet Measurements of Emitted Radiation) for obtaining 
   the HI Lyα reference line profile in July 1996.

Note: The queries only use the time range and instrument (with detector when applicable)
as required by the context. The actual fetching of data (Fido.fetch) is provided as 
commented-out code since execution is not requested.
"""

from sunpy.net import Fido, attrs as a

def query_uvcs():
    # Query UVCS data for the period when equatorial streamer belt observations were made.
    # Time Range: August 1, 1996 to September 2, 1996.
    # Instrument: UVCS. (This query will include any available detectors in UVCS.)
    uvcs_time_start = "1996-08-01"
    uvcs_time_end = "1996-09-02"
    uvcs_query = Fido.search(a.Time(uvcs_time_start, uvcs_time_end),
                             a.Instrument("UVCS"))
    print("UVCS Query Results:")
    print(uvcs_query)
    # To fetch the data, uncomment the following line:
    # uvcs_data = Fido.fetch(uvcs_query)

def query_eit():
    # Query EIT data for composite imaging of the equatorial streamer.
    # Time Range: August 30, 1996 to September 2, 1996.
    # Instrument: EIT.
    eit_time_start = "1996-08-30"
    eit_time_end = "1996-09-02"
    eit_query = Fido.search(a.Time(eit_time_start, eit_time_end),
                            a.Instrument("EIT"))
    print("\nEIT Query Results:")
    print(eit_query)
    # To fetch the data, uncomment the following line:
    # eit_data = Fido.fetch(eit_query)

def query_lasco_c2():
    # Query LASCO C2 data for white-light observations of the equatorial streamer.
    # Time Range: August 30, 1996 to September 2, 1996.
    # Instrument: LASCO with Detector: C2.
    lasco_time_start = "1996-08-30"
    lasco_time_end = "1996-09-02"
    lasco_query = Fido.search(a.Time(lasco_time_start, lasco_time_end),
                              a.Instrument("LASCO"),
                              a.Detector("C2"))
    print("\nLASCO C2 Query Results:")
    print(lasco_query)
    # To fetch the data, uncomment the following line:
    # lasco_data = Fido.fetch(lasco_query)

def query_sumer():
    # Query SUMER data for the reference HI Lyα line profile.
    # Time Range: July 1996 (using the entire month as an approximation).
    # Instrument: SUMER.
    sumer_time_start = "1996-07-01"
    sumer_time_end = "1996-07-31"
    sumer_query = Fido.search(a.Time(sumer_time_start, sumer_time_end),
                              a.Instrument("SUMER"))
    print("\nSUMER Query Results:")
    print(sumer_query)
    # To fetch the data, uncomment the following line:
    # sumer_data = Fido.fetch(sumer_query)

if __name__ == "__main__":
    # Execute each query separately and print the results.
    query_uvcs()
    query_eit()
    query_lasco_c2()
    query_sumer()
