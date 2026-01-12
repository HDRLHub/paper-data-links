# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query data from the Virtual Solar Observatory (VSO)
using SunPy for a series of solar observations described in the research paper.
Specifically, the queries include:
  1. SDO/AIA EUV images in the 171 Å channel (capturing coronal loops and filament structure)
     at 2013-07-09 14:29:24 UT.
  2. SDO/AIA EUV images in the 304 Å channel (highlighting filament channels and flare ribbons)
     at 2013-07-09 15:29:08 UT.
  3. SDO/HMI photospheric magnetograms (to capture magnetic polarity details) at 2013-07-09 14:30 UT.
  4. STEREO-A SECCHI/COR2 white-light coronagraph images (for CME structure observations)
     at 2013-07-09 16:00 UT.
  5. SOHO LASCO/C2 coronagraph data (complementary white-light CME imaging) at 2013-07-09 16:00 UT.

Each query is constructed with explicit time and instrument settings as specified.
Note: The Fido.fetch commands are commented out to prevent automatic downloading.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

def main():
    # 1. Query SDO/AIA for EUV imaging in the 171 Å channel
    # This captures the coronal loops and the inverse-S shaped filament at 2013-07-09 14:29:24 UT.
    query_aia_171 = Fido.search(
        a.Time("2013-07-09T14:29:24", "2013-07-09T14:29:24"),
        a.Source("SDO"),
        a.Instrument("AIA"),
        a.Wavelength(171 * u.AA)
    )
    print("SDO/AIA 171 Å query result:")
    print(query_aia_171)
    # To download the data, uncomment the next line:
    # files_aia_171 = Fido.fetch(query_aia_171)
    
    # 2. Query SDO/AIA for EUV imaging in the 304 Å channel
    # This observation shows the filament channel and flare ribbons at 2013-07-09 15:29:08 UT.
    query_aia_304 = Fido.search(
        a.Time("2013-07-09T15:29:08", "2013-07-09T15:29:08"),
        a.Source("SDO"),
        a.Instrument("AIA"),
        a.Wavelength(304 * u.AA)
    )
    print("\nSDO/AIA 304 Å query result:")
    print(query_aia_304)
    # To download the data, uncomment the next line:
    # files_aia_304 = Fido.fetch(query_aia_304)
    
    # 3. Query SDO/HMI for a photospheric magnetogram
    # This magnetogram at 2013-07-09 14:30 UT provides the magnetic field configuration.
    query_hmi = Fido.search(
        a.Time("2013-07-09T14:30:00", "2013-07-09T14:30:00"),
        a.Source("SDO"),
        a.Instrument("HMI")
    )
    print("\nSDO/HMI query result:")
    print(query_hmi)
    # To download the data, uncomment the next line:
    # files_hmi = Fido.fetch(query_hmi)
    
    # 4. Query STEREO-A SECCHI/COR2 for coronagraph imaging
    # This query retrieves white-light coronagraph images capturing the CME's appearance
    # as first seen at 2013-07-09 16:00 UT.
    query_stereo_cor2 = Fido.search(
        a.Time("2013-07-09T16:00:00", "2013-07-09T16:00:00"),
        a.Source("STEREO_A"),
        a.Instrument("SECCHI"),
        a.Detector("COR2")
    )
    print("\nSTEREO-A SECCHI/COR2 query result:")
    print(query_stereo_cor2)
    # To download the data, uncomment the next line:
    # files_stereo_cor2 = Fido.fetch(query_stereo_cor2)
    
    # 5. Query SOHO LASCO/C2 for coronagraph imaging
    # Complementary white-light observations of the CME from SOHO at 2013-07-09 16:00 UT.
    query_lasco_c2 = Fido.search(
        a.Time("2013-07-09T16:00:00", "2013-07-09T16:00:00"),
        a.Source("SOHO"),
        a.Instrument("LASCO"),
        a.Detector("C2")
    )
    print("\nSOHO LASCO/C2 query result:")
    print(query_lasco_c2)
    # To download the data, uncomment the next line:
    # files_lasco_c2 = Fido.fetch(query_lasco_c2)

if __name__ == "__main__":
    main()
